# Mobilière Doc-Audit AI 🛡️

**Prototype — Innovation Arena PK | La Mobilière**

Application Streamlit d'analyse intelligente de conformité documentaire, alimentée par Gemini 2.5 Flash. Elle identifie les écarts entre un document client (contrat, règlement) et une régulation (ex. réforme LPP 21).

---

## 🚀 Déploiement sur Streamlit Community Cloud

### 1. Prérequis
- Compte [Streamlit Cloud](https://share.streamlit.io) connecté à ce dépôt GitHub
- Clé API Gemini (depuis [Google AI Studio](https://aistudio.google.com/app/apikey))

### 2. Déployer l'app
1. Aller sur [share.streamlit.io](https://share.streamlit.io) → **New app**
2. Sélectionner le dépôt `Trippykit/mobiliere-doc-audit`, branche `main`, fichier `app.py`
3. Cliquer sur **Deploy**

### 3. Configurer la clé API
Dans le dashboard Streamlit → **Settings** → **Secrets**, ajouter :

```toml
GEMINI_API_KEY = "votre_cle_api_ici"
```

---

## 💻 Exécution locale

```bash
git clone https://github.com/Trippykit/mobiliere-doc-audit.git
cd mobiliere-doc-audit
pip install -r requirements.txt
```

Créer le fichier `.streamlit/secrets.toml` :

```toml
GEMINI_API_KEY = "votre_cle_api_ici"
```

Puis lancer :

```bash
streamlit run app.py
```

---

## 📁 Structure

- `app.py` — Application Streamlit principale
- `requirements.txt` — Dépendances Python

## ⚖️ Note

Ce prototype est une aide à la décision. Tout résultat doit être validé par le service juridique.

---

© La Mobilière — Prototype Entretien 27.04
