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
- [x] Project structure setup
- [ ] TRS calculation engine
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
