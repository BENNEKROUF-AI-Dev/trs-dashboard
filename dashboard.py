import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="TRS Dashboard", page_icon="⚙️", layout="wide")

# ─── CHARGEMENT DONNÉES ────────────────────────────────────────
st.sidebar.markdown("### 📂 Source de données")
uploaded_file = st.sidebar.file_uploader("Importer votre fichier (CSV ou Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.sidebar.success(f"✅ Fichier chargé : {uploaded_file.name}")
else:
    data = {
        "heure": ["06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"],
        "production": [142,120,149,171,138,162,95,155,168,144,173,160],
        "objectif": [150,150,150,150,150,150,150,150,150,150,150,150],
        "arret_minutes": [8,0,12,0,22,0,45,0,5,18,0,8],
        "cause_arret": ["Changement serie","","Panne mecanique","","Attente matiere","","Changement serie","","Reglage","Panne mecanique","","Nettoyage"]
    }
    df = pd.DataFrame(data)
    st.sidebar.info("📊 Données de démonstration chargées")

# ─── CALCULS ───────────────────────────────────────────────────
production_reelle = df["production"].sum()
production_theorique = df["objectif"].sum()
trs = round((production_reelle / production_theorique) * 100, 1)
total_arrets = df["arret_minutes"].sum()

df_arrets = df[df["cause_arret"].notna() & (df["cause_arret"] != "")]
pareto = df_arrets.groupby("cause_arret")["arret_minutes"].sum().sort_values(ascending=False).reset_index()
pareto.columns = ["cause", "duree_minutes"]

st.markdown("## ⚙️ TRS Dashboard — Suivi de Production")
st.markdown("*Dashboard de suivi TRS et performance de production destiné aux PME industrielles.*")
st.markdown("---")

# ─── KPIs ──────────────────────────────────────────────────────
with col1:
    couleur = "🟢" if trs >= 85 else "🟡" if trs >= 70 else "🔴"
    st.metric(label=f"{couleur} TRS Global", value=f"{trs}%", delta="Obj: 85%")
with col2:
    st.metric(label="🏭 Disponibilité Machine", value=f"{int(production_reelle):,} pcs")
with col3:
    st.metric(label="🎯 Performance Production", value=f"{int(production_theorique):,} pcs")
with col4:
    st.metric(label="⏱️ Arrêts Cumulés", value=f"{int(total_arrets)} min"))} min")

st.markdown("---")

# ─── GRAPHIQUES ────────────────────────────────────────────────
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("#### 📈 Production horaire vs Objectif")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["heure"], y=df["objectif"], name="Objectif", line=dict(color="#3b82f6", dash="dash", width=2)))
    fig.add_trace(go.Scatter(x=df["heure"], y=df["production"], name="Production", line=dict(color="#f97316", width=3), fill="tozeroy", fillcolor="rgba(249,115,22,0.1)"))
    fig.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130", font_color="#94a3b8", height=300, margin=dict(l=20,r=20,t=20,b=20))
    fig.update_xaxes(gridcolor="#2d3748")
    fig.update_yaxes(gridcolor="#2d3748")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("#### 🔻 Pareto Arrêts")
    fig2 = px.bar(pareto, x="duree_minutes", y="cause", orientation="h", color="duree_minutes", color_continuous_scale=["#22c55e","#eab308","#ef4444"], text="duree_minutes")
    fig2.update_traces(texttemplate="%{text} min", textposition="outside")
    fig2.update_layout(paper_bgcolor="#1e2130", plot_bgcolor="#1e2130", font_color="#94a3b8", showlegend=False, coloraxis_showscale=False, height=300, margin=dict(l=20,r=20,t=20,b=20), yaxis=dict(autorange="reversed"))
    fig2.update_xaxes(gridcolor="#2d3748")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("#### 📋 Détail horaire")
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:#475569; font-size:0.75rem'>TRS Dashboard · Adam Bennekrouf · <a href='https://linkedin.com/in/adam-bennekrouf' style='color:#f97316'>LinkedIn</a></div>", unsafe_allow_html=True)
