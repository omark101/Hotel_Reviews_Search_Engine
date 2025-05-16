# 🔍 Hotel Reviews Search Engine

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-45b8d8)](https://github.com/TomSchimansky/CustomTkinter)
[![License: Academic](https://img.shields.io/badge/license-University_Project-green)](#license)

---

## ✨ Overview

The **Hotel Reviews Search Engine** is a semantic-aware, intelligent search engine designed to help users search for relevant hotel reviews using natural language queries. Powered by **BM25** ranking and **BERT-based semantic expansion**, it provides meaningful, context-rich search results with an interactive and visually appeling **CustomTkinter** GUI.

This project was developed as a university capstone by:
- 👤 [Omar Ayman](https://github.com/omark101)
- 👤 [Mohamed El Sherbini](https://github.com/mosherby10)

---

## 🚀 Features

- 🔍 **Semantic Query Expansion** using BERT embeddings (`all-MiniLM-L6-v2`)
- 📌 **BM25 Ranking** from PyTerrier
- 🌍 **Country Flag** fetched as text from the dataset and dynamically integrate it in GUI using `flagcdn` per reviewer 
- 📍 **Google Maps Integration** for hotel location
- 💡 **Dark/Light Mode Toggle**
- 📈 **Real-Time Query Evaluation Dashboard**
- 📊 **Metrics**: latency, query frequency, top hotels, etc.

---

## 🖼 Screenshots

| Dashboard View |
|------------|
![Screenshot 2025-05-15 173807](https://github.com/user-attachments/assets/0479c75a-8896-496e-82ad-92439265ec75)
![Screenshot 2025-05-15 173915](https://github.com/user-attachments/assets/e3190e1e-9e5d-4d8e-b429-9d6833f955a4)
![Screenshot 2025-05-15 174121](https://github.com/user-attachments/assets/b238f924-5b76-4816-9189-808e40c315eb)
![Screenshot 2025-05-15 175246](https://github.com/user-attachments/assets/294da269-f541-448f-b457-ab40f0a9128f)
![Screenshot 2025-05-15 175336](https://github.com/user-attachments/assets/da8b88d6-fd38-4997-bc7b-e37066317732)

---

- Search using natural language queries.
- Enable/disable semantic expansion.
- Click 📍 to open hotel location in Google Maps.
- View interactive metrics by clicking `📊 Dashboard`.

---

## 📁 Folder Structure

```bash
Hotel_Reviews_Search_Engine/
├── data/                    # (excluded) Raw dataset (CSV)
├── index/                   # (excluded) Terrier indexing files
├── modules/
│   ├── query_expansion.py   # BERT-based expansion logic
│   ├── evaluation.py        # Dashboard visualizations
├── gui.py                   # Main GUI script
├── cleaning.py              # Dataset cleaning code
├── indexing.py              # initial indexing code
├── main.py                  # main function control indexing or loading the program
├── requirements.txt         # All dependencies
├── README.md                # This file
```

---

## 🤝 Contributing

Pull requests are welcome.

if you are intersted please refer to the "Setup" file 
---

<span style="color:green;font-weight:700;font-size:20px">
    markdown color font styles
</span>


## 📝 License

This is a **university research project** and provided as-is for educational purposes.

---

## 📣 Acknowledgements

- [Sentence-Transformers](https://www.sbert.net/)
- [PyTerrier](https://github.com/terrier-org/pyterrier)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---
