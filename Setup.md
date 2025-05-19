
# 🚀 Installation Guide for Hotel Reviews Search Engine

Follow these steps to set up and run the **Hotel Reviews Search Engine** on your local machine.

---

## 📂 1. Clone the Repository

```bash
git clone https://github.com/omark101/Hotel_Reviews_Search_Engine.git
cd Hotel_Reviews_Search_Engine
```

---

## 🐍 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
# Activate on Windows
.\.venv\Scripts ctivate

# Activate on macOS/Linux
source .venv/bin/activate
```

---

## 📋 3. Install Dependencies

Make sure `pip` is up to date:

```bash
pip install --upgrade pip
```

Then install all required libraries:

```bash
pip install -r requirements.txt
```

---

## ☕ 4. Install Java (Required for PyTerrier)

PyTerrier requires Java to be installed and available in your system’s environment.

### 🔽 Download and Install JDK

- [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- Or [OpenJDK](https://adoptium.net/)

Install **Java SE Development Kit 8 or later(preferably JDK-17)**.

### ⚙️ Set JAVA_HOME (on Windows)

You can temporarily set JAVA_HOME using:

```powershell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-<version>"
$env:PATH += ";$env:JAVA_HOME\bin"
```

To make it permanent, go to:

> Control Panel → System → Advanced System Settings → Environment Variables

For help: [Java Environment Setup (Windows)](https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html)

---
## 📊 5. Dataset
and here is the dataset used in this app: [Dataset](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe)




---
## ▶️ 6. Run the Application
before running the application, go to:
> main.py → Set `BUILD_INDEX` to TRUE
> 
> main.py → uncomment `return build_index(df)`
> 
Only first time, the program will take some time in building the indexes after your first succesful run you can set `BUILD_INDEX` to False and comment the return line.

```bash
python gui.py
```


---
## 🔗 References

- [PyTerrier Documentation](https://pyterrier.readthedocs.io/)
- [NLTK Data](https://www.nltk.org/data.html)
- [SentenceTransformers - BERT](https://www.sbert.net/)
- [Java Installation (Oracle)](https://docs.oracle.com/javase/8/docs/technotes/guides/install/windows_jdk_install.html)

---

Feel free to contribute or raise issues via GitHub!
