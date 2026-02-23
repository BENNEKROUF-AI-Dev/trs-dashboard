# dashboard.py
# TRS Dashboard — Main Streamlit Application
# Author: Adam Bennekrouf — BENNEKROUF-AI-Dev

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

sys.path.append("src")
from calcul_trs import charger_donnees, calculer_trs, calculer_pareto_arrets 

# ─── CONFIG PAGE ───────────────────────────────────────────────
st.set_page_config(
    page_title="TRS Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# ─── STYLE ─────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .metric-card {
        background: #1e2130;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border-left: 4px solid #f97316;
    }
</style>
""", unsafe_allow_html=True)

# ─── HEADER ────────────────────────────────────────────────────
st.markdown("## ⚙️ TRS Dashboard — Suivi de Production")
st.markdown("---")

# ─── CHARGEMENT DONNÉES ────────────────────────────────────────
st.sidebar.markdown("### 📂 Source de données")
uploaded_file = st.sidebar.file_uploader(
    "Importer votre fichier (CSV ou Excel)",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.sidebar.success(f"✅ Fichier chargé : {uploaded_file.name}")
else:
    df = charger_donnees("data/sample_production_data.csv")
    st.sidebar.info("📊 Données de démonstration chargées")

# ─── CALCULS ───────────────────────────────────────────────────
resultats = calculer_trs(df)
pareto = calculer_pareto_arrets(df)
total_arrets = df["arret_minutes"].sum()

# ─── KPIs ──────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    trs = resultats["trs_percent"]
    couleur = "🟢" if trs >= 85 else "🟡" if trs >= 70 else "🔴"
    st.metric(
        label=f"{couleur} TRS Global",
        value=f"{trs}%",
        delta="Obj: 85%"
    )

with col2:
    st.metric(
        label="🏭 Production Réelle",
        value=f"{resultats['production_reelle']:,} pcs",
        delta=f"-{resultats['ecart']} vs objectif"
    )

with col3:
    st.metric(
        label="🎯 Production Théorique",
        value=f"{resultats['production_theorique']:,} pcs"
    )

with col4:
    st.metric(
        label="⏱️ Arrêts Cumulés",
        value=f"{int(total_arrets)} min",
        delta=f"{len(pareto)} causes identifiées"
    )

st.markdown("---")

# ─── GRAPHIQUES ────────────────────────────────────────────────
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("#### 📈 Production horaire vs Objectif")
    fig_prod = go.Figure()
    fig_prod.add_trace(go.Scatter(
        x=df["heure"], y=df["objectif"],
        name="Objectif",
        line=dict(color="#3b82f6", dash="dash", width=2)
    ))
    fig_prod.add_trace(go.Scatter(
        x=df["heure"], y=df["production"],
        name="Production réelle",
        line=dict(color="#f97316", width=3),
        fill="tozeroy",
        fillcolor="rgba(249,115,22,0.1)"
    ))
    fig_prod.update_layout(
        paper_bgcolor="#1e2130",
        plot_bgcolor="#1e2130",
        font_color="#94a3b8",
        legend=dict(bgcolor="#1e2130"),
        margin=dict(l=20, r=20, t=20, b=20),
        height=300
    )
    fig_prod.update_xaxes(gridcolor="#2d3748")
    fig_prod.update_yaxes(gridcolor="#2d3748")
    st.plotly_chart(fig_prod, use_container_width=True)

with col_right:
    st.markdown("#### 🔻 Pareto Arrêts")
    if not pareto.empty:
        fig_pareto = px.bar(
            pareto,
            x="duree_minutes",
            y="cause",
            orientation="h",
            color="duree_minutes",
            color_continuous_scale=["#22c55e", "#eab308", "#ef4444"],
            text="duree_minutes"
        )
        fig_pareto.update_traces(
            texttemplate="%{text} min",
            textposition="outside"
        )
        fig_pareto.update_layout(
            paper_bgcolor="#1e2130",
            plot_bgcolor="#1e2130",
            font_color="#94a3b8",
            showlegend=False,
            coloraxis_showscale=False,
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            yaxis=dict(autorange="reversed")
        )
        fig_pareto.update_xaxes(gridcolor="#2d3748")
        st.plotly_chart(fig_pareto, use_container_width=True)
    else:
        st.info("Aucun arrêt enregistré")

st.markdown("---")

# ─── TABLEAU DÉTAIL ────────────────────────────────────────────
st.markdown("#### 📋 Détail horaire")
df_display = df.copy()
df_display["atteinte_objectif"] = df_display.apply(
    lambda r: "✅" if r["production"] >= r["objectif"] else "⚠️", axis=1
)
st.dataframe(df_display, use_container_width=True, hide_index=True)

# ─── FOOTER ────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#475569; font-size:0.75rem'>"
    "TRS Dashboard · Adam Bennekrouf · "
    "<a href='https://linkedin.com/in/adam-bennekrouf' style='color:#f97316'>LinkedIn</a> · "
    "<a href='https://github.com/BENNEKROUF-AI-Dev' style='color:#f97316'>GitHub</a>"
    "</div>",
    unsafe_allow_html=True
)
