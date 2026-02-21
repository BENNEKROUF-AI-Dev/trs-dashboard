# calcul_trs.py
# TRS / OEE Calculation Engine
# Author: Adam Bennekrouf — BENNEKROUF-AI-Dev

import pandas as pd


def charger_donnees(filepath: str) -> pd.DataFrame:
    """Load production data from CSV or Excel file."""
    if filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    elif filepath.endswith((".xlsx", ".xls")):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Format non supporte. Utilisez CSV ou Excel.")


def calculer_trs(df: pd.DataFrame,
                 col_production: str = "production",
                 col_objectif: str = "objectif") -> dict:
    """
    Calculate TRS (Taux de Rendement Synthetique / OEE).
    TRS = Production reelle / Production theorique maximale
    """
    production_reelle = df[col_production].sum()
    production_theorique = df[col_objectif].sum()

    trs = round((production_reelle / production_theorique) * 100, 1)

    return {
        "trs_percent": trs,
        "production_reelle": int(production_reelle),
        "production_theorique": int(production_theorique),
        "ecart": int(production_theorique - production_reelle)
    }


def calculer_pareto_arrets(df: pd.DataFrame,
                            col_cause: str = "cause_arret",
                            col_duree: str = "arret_minutes") -> pd.DataFrame:
    """
    Build Pareto table of downtime causes.
    Returns causes ranked by total lost time.
    """
    df_arrets = df[df[col_cause].notna() & (df[col_cause] != "")]
    pareto = df_arrets.groupby(col_cause)[col_duree].sum()
    pareto = pareto.sort_values(ascending=False).reset_index()
    pareto.columns = ["cause", "duree_minutes"]
    pareto["pourcentage"] = round(
        pareto["duree_minutes"] / pareto["duree_minutes"].sum() * 100, 1
    )
    return pareto


if __name__ == "__main__":
    df = charger_donnees("data/sample_production_data.csv")
    resultats = calculer_trs(df)
    print(f"TRS : {resultats['trs_percent']}%")
    print(f"Production : {resultats['production_reelle']} / {resultats['production_theorique']} pcs")
    print(f"Ecart : {resultats['ecart']} pcs")
    pareto = calculer_pareto_arrets(df)
    print("\nPareto arrets :")
    print(pareto)
