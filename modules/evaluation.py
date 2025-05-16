import matplotlib.pyplot as plt
import seaborn as sns
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
import pandas as pd

def launch_dashboard(query_log, df):
    if not query_log:
        print("No queries to evaluate.")
        return

    ctk.set_appearance_mode("System")
    dashboard = ctk.CTkToplevel()
    dashboard.title("Evaluation Dashboard")
    dashboard.geometry("1000x750")

    query_df = pd.DataFrame(query_log)
    query_df['query'] = query_df['query'].astype(str)

    total_queries = len(query_df)
    total_latency = query_df['time'].sum()
    avg_latency = query_df['time'].mean()

    all_words = " ".join(query_df['query']).lower().split()
    word_freq = Counter(all_words)
    top_words = dict(word_freq.most_common(10))
    hotel_freq = df['Hotel_Name'].value_counts().head(10)
    query_counts = query_df['query'].value_counts().head(10)

    plots = []

    def create_latency_plot():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(query_df['time'], marker='o', linestyle='-', color='blue')
        ax.set_title("Query Latency per Search")
        ax.set_xlabel("Query #")
        ax.set_ylabel("Latency (s)")
        return fig

    def create_query_freq_plot():
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=query_counts.values, y=query_counts.index, ax=ax, palette="rocket", hue=None, legend=False)
        ax.set_title("Most Frequent Queries")
        ax.set_xlabel("Count")
        ax.set_ylabel("Query")
        return fig

    def create_top_words_plot():
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=list(top_words.values()), y=list(top_words.keys()), ax=ax, palette="mako", hue=None, legend=False)
        ax.set_title("Top Words in User Queries")
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Words")
        return fig

    def create_top_hotels_plot():
        fig, ax = plt.subplots(figsize=(7.5, 5))  # adjust size slightly
        sns.barplot(x=hotel_freq.values, y=hotel_freq.index, ax=ax, palette="viridis", hue=None, legend=False)
        ax.set_title("Most Queried Hotel Names", fontsize=12)
        ax.set_xlabel("Frequency", fontsize=10)
        ax.set_ylabel("Hotel Name", fontsize=10)
        ax.tick_params(axis='both', labelsize=9)

        plt.subplots_adjust(left=0.35)  # increase left margin for Y labels
        return fig

    plots.append(create_latency_plot())
    plots.append(create_query_freq_plot())
    plots.append(create_top_words_plot())
    plots.append(create_top_hotels_plot())

    summary_text = (
        f"Total Queries: {total_queries}\n"
        f"Total Latency: {total_latency:.2f} seconds\n"
        f"Avg Latency per Query: {avg_latency:.3f} seconds"
    )
    ctk.CTkLabel(dashboard, text=summary_text, font=("Arial", 14), anchor="w", justify="left").pack(pady=10)

    plot_frame = ctk.CTkFrame(dashboard)
    plot_frame.pack(fill="both", expand=True)

    canvas_widget = None
    current_index = 0

    def show_plot(index):
        nonlocal canvas_widget
        for widget in plot_frame.winfo_children():
            widget.destroy()
        fig = plots[index]
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=ctk.BOTH, expand=True)

    def next_plot():
        nonlocal current_index
        if current_index < len(plots) - 1:
            current_index += 1
            show_plot(current_index)

    def prev_plot():
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            show_plot(current_index)

    nav_frame = ctk.CTkFrame(dashboard)
    nav_frame.pack(pady=5)

    prev_btn = ctk.CTkButton(nav_frame, text="← Previous", command=prev_plot)
    prev_btn.pack(side="left", padx=10)

    next_btn = ctk.CTkButton(nav_frame, text="Next →", command=next_plot)
    next_btn.pack(side="left", padx=10)

    show_plot(0)
