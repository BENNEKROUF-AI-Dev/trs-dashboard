# TRS Dashboard — Production Performance Tracker

Interactive dashboard for industrial production monitoring.
Built with Python and Streamlit — designed for manufacturing SMEs.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

---

## 🎯 What it does

- **OEE / TRS** automatic calculation from raw Excel or CSV data
- **Hourly production** tracking vs target
- **Downtime Pareto** — top causes ranked by lost time
- **Machine status** real-time overview
- **Automated report** export ready for production meetings

---

## 🏭 Who is it for

Manufacturing SMEs drowning in Excel exports and manual reports.
No Power BI license needed. No IT department required.
You upload your GMAO export → you get your dashboard in seconds.

---

## 📁 Project Structure
```
trs-dashboard/
│
├── data/
│   └── sample_production_data.csv   # Sample dataset (fictitious)
│
├── src/
│   ├── calcul_trs.py                # OEE/TRS calculation engine
│   ├── pareto_arrets.py             # Downtime Pareto analysis
│   └── utils.py                    # Helper functions
│
├── dashboard.py                     # Main Streamlit app
├── requirements.txt                 # Dependencies
└── README.md
```

---

## 🚀 How to run it
```bash
# Clone the repo
git clone https://github.com/BENNEKROUF-AI-Dev/trs-dashboard.git
cd trs-dashboard

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run dashboard.py
```

---

## 📊 Dashboard Preview

*Screenshot coming soon — currently in development*

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Pandas** — data processing
- **Streamlit** — web dashboard
- **Plotly** — interactive charts
- **OpenPyXL** — Excel file reading

---

## 🏗️ Roadmap

- [x] Project structure setup
- [ ] TRS calculation engine
- [ ] Streamlit dashboard v1
- [ ] Excel/CSV file upload
- [ ] Pareto downtime chart
- [ ] PDF report export
- [ ] Multi-machine support
- [ ] Predictive maintenance module (ML)

---

## 👤 Author

**Adam Bennekrouf**
Master's in Industrial Systems Engineering (GSI)
Specializing in Data Analytics & AI for Industrial Operations

- LinkedIn : [adam-bennekrouf](https://linkedin.com/in/adam-bennekrouf)
- GitHub : [BENNEKROUF-AI-Dev](https://github.com/BENNEKROUF-AI-Dev)
- Based in France · Open to Luxembourg & Germany
```

Commit avec le message : `"Initial README — TRS Dashboard project"`

---

## Étape 3 — Créer la structure de fichiers

Toujours sur GitHub, crée ces fichiers un par un avec le bouton **"Add file" → "Create new file"** :

**Fichier 1 :** `requirements.txt`
```
streamlit==1.32.0
pandas==2.2.0
plotly==5.19.0
openpyxl==3.1.2
```
Commit : `"Add requirements.txt"`

---

**Fichier 2 :** `data/sample_production_data.csv`
```
heure,production,objectif,arret_minutes,cause_arret
06:00,142,150,8,Changement série
07:00,158,150,0,
08:00,149,150,12,Panne mécanique
09:00,171,150,0,
10:00,138,150,22,Attente matière
11:00,162,150,0,
12:00,95,150,45,Changement série
13:00,155,150,0,
14:00,168,150,5,Réglage
15:00,144,150,18,Panne mécanique
16:00,173,150,0,
17:00,160,150,8,Nettoyage
