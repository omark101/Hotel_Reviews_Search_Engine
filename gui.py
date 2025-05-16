import customtkinter as ctk
import pandas as pd
import pyterrier as pt
from PIL import Image, ImageTk
import requests
from io import BytesIO
from customtkinter import CTkImage
import pycountry
import webbrowser
import time

from main import initialize_index
from modules.evaluation import launch_dashboard
from modules.query_expansion import expand_query, build_dynamic_vocab


query_log = []

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


def run_gui():
    index = initialize_index()
    bm25 = pt.terrier.Retriever(index, wmodel="BM25", metadata=[
        "docno", "Hotel_Name", "Positive_Review", "Negative_Review",
        "Reviewer_Nationality", "Hotel_Address", "lat", "lng"
    ])

    df = pd.read_csv("./data/Hotel_Reviews.csv", encoding='utf-8')
    df['docno'] = df.index.astype(str)
    df['text'] = df['Positive_Review'].fillna('') + " " + df['Negative_Review'].fillna('')

    build_dynamic_vocab(df)

    root = ctk.CTk()
    root.title("Hotel Review Search Engine")
    root.geometry("1240x700")
    mode_var = ctk.StringVar(value="System")

    search_var = ctk.StringVar()
    expansion_enabled = ctk.BooleanVar(value=True)

    def get_flag_image(country_name):
        try:
            country = pycountry.countries.get(name=country_name)
            if not country:
                matches = [c for c in pycountry.countries if country_name.lower() in c.name.lower()]
                country = matches[0] if matches else None
            if not country:
                print(f"Unknown country: {country_name}")
                return None
            code = country.alpha_2.lower()
            url = f"https://flagcdn.com/w40/{code}.png"
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                img = Image.open(BytesIO(resp.content)).resize((40, 30))
                return CTkImage(light_image=img, dark_image=img, size=(40, 30))
        except Exception as e:
            print(f"Error loading flag: {e}")
        return None

    def open_map(lat, lng):
        url = f"https://www.google.com/maps?q={lat},{lng}"
        webbrowser.open(url)

    def change_mode(choice):
        ctk.set_appearance_mode(choice)

    def search():
        query = search_var.get()
        print(f"Original Query: {query}")
        start_time = time.time()

        expanded = expand_query(query) if expansion_enabled.get() else query

        results = bm25.search(expanded).head(10)
        end_time = time.time()
        query_log.append({"query": query, "time": round(end_time - start_time, 4)})

        results['docno'] = results['docno'].astype(str)
        missing = ['Hotel_Name', 'Positive_Review', 'Negative_Review', 'Reviewer_Nationality']
        if any(col not in results.columns for col in missing):
            results = results.merge(df[['docno'] + missing + ['lat', 'lng']], on='docno', how='left')

        for widget in results_frame.winfo_children():
            widget.destroy()

        if results.empty:
            ctk.CTkLabel(results_frame, text="No results found.", font=("Arial", 14)).pack(pady=10)
            return

        for _, row in results.iterrows():
            container = ctk.CTkFrame(results_frame, corner_radius=10)
            container.pack(pady=10, fill="x", padx=10)

            ctk.CTkLabel(container, text=f" {row['Hotel_Name']}", font=("Arial", 16, "bold"), anchor="w").pack(anchor='w')
            flag = get_flag_image(row.get("Reviewer_Nationality", ''))
            if flag:
                lbl = ctk.CTkLabel(container, image=flag, text="")
                lbl.image = flag
                lbl.pack(anchor='w')

            ctk.CTkLabel(container, text=f"🌍 Reviewer: {row.get('Reviewer_Nationality', 'N/A')}", anchor="w").pack(anchor='w')
            ctk.CTkLabel(container, text=f"💬 Positive: {row.get('Positive_Review', 'N/A')}", wraplength=850, anchor="w").pack(anchor='w')
            ctk.CTkLabel(container, text=f"⚡ Negative: {row.get('Negative_Review', 'N/A')}", wraplength=850, anchor="w").pack(anchor='w')

            if pd.notna(row.get("lat")) and pd.notna(row.get("lng")):
                map_btn = ctk.CTkButton(container, text="Show directions on Maps",
                                        command=lambda lat=row['lat'], lng=row['lng']: open_map(lat, lng))
                map_btn.pack(anchor='w', pady=5)

    top_frame = ctk.CTkFrame(root)
    top_frame.pack(pady=10, padx=10, fill="x")

    ctk.CTkEntry(top_frame, textvariable=search_var, width=500, font=("Arial", 14)).pack(side="left", padx=10)
    ctk.CTkButton(top_frame, text="Search", command=search).pack(side="left")
    ctk.CTkCheckBox(top_frame, text="Enable Semantic Expansion", variable=expansion_enabled).pack(side="left", padx=10)

    mode_menu = ctk.CTkOptionMenu(top_frame, values=["Light", "Dark", "System"], variable=mode_var, command=change_mode)
    mode_menu.pack(side="left", padx=10)

    ctk.CTkButton(top_frame, text="📊 Dashboard", command=lambda: launch_dashboard(query_log, df)).pack()

    scrollable = ctk.CTkScrollableFrame(root, width=950, height=550)
    scrollable.pack(pady=10)
    results_frame = scrollable

    root.mainloop()


if __name__ == "__main__":
    run_gui()
