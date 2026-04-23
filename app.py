import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="La Mobilière | Doc-Audit AI",
    page_icon="🛡️",
    layout="wide"
)

# --- STYLE CSS (Identité Visuelle La Mobilière) ---
st.markdown("""
    <style>
    :root {
        --mobi-red: #E30613;
        --mobi-orange: #FF5F00;
        --mobi-gray-bg: #F8F9FA;
    }
    .stApp { background-color: #ffffff; }
    .header-container {
        background-color: var(--mobi-red);
        padding: 25px;
        border-radius: 0 0 15px 15px;
        color: white;
        margin-bottom: 30px;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: var(--mobi-red);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 20px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: var(--mobi-orange);
        border: none;
        color: white;
    }
    .result-card {
        background-color: var(--mobi-gray-bg);
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid var(--mobi-red);
    }
    </style>
""", unsafe_allow_html=True)

# --- GESTION DE LA CLÉ API (Via Streamlit Secrets) ---
# Note : Vous devrez ajouter GEMINI_API_KEY dans les "Secrets" du dashboard Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.warning("⚠️ Clé API non configurée. Veuillez l'ajouter dans les secrets Streamlit.")
    api_key = None

def run_audit(doc, reg):
    """Fonction d'audit avec le modèle Gemini 2.5 Flash"""
    if not api_key: return "Erreur : Clé API manquante."
    
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-09-2025",
        system_instruction=(
            "Tu es un Business Analyst expert en Prévoyance Suisse (BVG/LPP) à la Mobilière. "
            "Ton rôle est d'identifier les écarts entre un document client et une régulation. "
            "Formatte ta réponse en français avec des sections claires : [ANALYSE], [ÉCARTS], [CORRECTION SUGGÉRÉE]."
        )
    )
    
    prompt = f"AUDIT DE CONFORMITÉ :\n\nDOC :\n{doc}\n\nRÉGULATION :\n{reg}"
    
    # Retry logic simple
    for i in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            time.sleep(2)
    return "L'IA est momentanément indisponible. Réessayez."

# --- INTERFACE ---
st.markdown("""
    <div class="header-container">
        <h1>Mobilière Doc-Audit AI</h1>
        <p>Innovation Arena PK | Analyse intelligente de conformité documentaire</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📄 Document à vérifier")
    doc_input = st.text_area("Texte du contrat ou règlement :", height=250, key="doc", 
                             placeholder="Ex: Taux de conversion fixé à 6.8%...")
    
    if st.button("Charger exemple : Règlement Obsolète"):
        st.session_state.doc = "Article 15 : Le taux de conversion est maintenu à 6.8% pour l'ensemble des assurés actifs."
        st.rerun()

with col2:
    st.subheader("⚖️ Référentiel Légal")
    reg_input = st.text_area("Nouvelle norme ou loi :", height=250, key="reg",
                             value="Réforme LPP 21 : Le taux de conversion minimal obligatoire est abaissé à 6,0%.")

st.write("---")

if st.button("🚀 LANCER L'ANALYSE D'ÉCARTS"):
    if doc_input and reg_input:
        with st.spinner("Analyse en cours..."):
            res = run_audit(doc_input, reg_input)
            st.markdown("### 📊 Résultat de l'Audit")
            st.markdown(f'<div class="result-card">{res}</div>', unsafe_allow_html=True)
            
            st.info("💡 **Note BA :** Ce résultat est une aide à la décision et doit être validé par le service juridique de Berne.")
    else:
        st.error("Veuillez remplir les deux champs.")

st.markdown("<br><p style='text-align:center; color:gray;'>© La Mobilière - Prototype Entretien 27.04</p>", unsafe_allow_html=True)
