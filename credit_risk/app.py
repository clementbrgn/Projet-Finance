import streamlit as st
import pandas as pd
import joblib

# ─────────────────────────────────────────
# Chargement du modèle et des encodeurs
# ─────────────────────────────────────────
model = joblib.load('extra_trees_credit_model.pkl')

categorical_cols = ['Sex', 'Housing', 'Saving accounts', 'Checking account']
encoders = {col: joblib.load(f'{col}_encoder.pkl') for col in categorical_cols}

# ─────────────────────────────────────────
# Interface
# ─────────────────────────────────────────
st.title("💳 Credit Risk Prediction App")
st.write("Entrez les informations du demandeur pour prédire si le crédit est **bon** ou **mauvais**.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    age            = st.number_input("Âge", min_value=18, max_value=80, value=30)
    sex            = st.selectbox("Sexe", ["male", "female"])
    job            = st.number_input("Job (0 = non qualifié, 3 = hautement qualifié)", min_value=0, max_value=3, value=1)
    housing        = st.selectbox("Logement", ["own", "rent", "free"])

with col2:
    saving_acc     = st.selectbox("Compte épargne",  ["little", "moderate", "quite rich", "rich"])
    checking_acc   = st.selectbox("Compte courant",  ["little", "moderate", "rich"])
    credit_amount  = st.number_input("Montant du crédit (€)", min_value=0, value=1000)
    duration       = st.number_input("Durée (mois)", min_value=1, value=12)

st.divider()

# ─────────────────────────────────────────
# Préparation des données pour le modèle
# ─────────────────────────────────────────
input_df = pd.DataFrame({
    'Age':               [age],
    'Sex':               [encoders['Sex'].transform([sex])[0]],
    'Job':               [job],
    'Housing':           [encoders['Housing'].transform([housing])[0]],
    'Saving accounts':   [encoders['Saving accounts'].transform([saving_acc])[0]],
    'Checking account':  [encoders['Checking account'].transform([checking_acc])[0]],
    'Credit amount':     [credit_amount],
    'Duration':          [duration],
})

# ─────────────────────────────────────────
# Prédiction
# ─────────────────────────────────────────
if st.button("🔍 Prédire le risque"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    st.subheader("Résultat :")
    if prediction == 1:
        st.success("✅ Risque prédit : **BON** (faible risque crédit)")
    else:
        st.error("❌ Risque prédit : **MAUVAIS** (crédit à haut risque)")

    st.caption(f"Confiance du modèle — Bon : {proba[1]*100:.1f}%  |  Mauvais : {proba[0]*100:.1f}%")
