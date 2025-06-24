import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Prozessdokumentation", layout="centered")
st.title("📄 Geführte Prozessdokumentation")

st.markdown("Beantworte die folgenden Fragen, um einen Geschäftsprozess zu dokumentieren.")

# Eingabefelder
prozessname = st.text_input("1. Wie heißt der Prozess?")
ausloeser = st.text_input("2. Was löst den Prozess aus?")
ziel = st.text_input("3. Was ist das Ziel des Prozesses?")
akteure = st.text_area("4. Welche Rollen oder Abteilungen sind beteiligt?")
start = st.text_input("5. Wie beginnt der Prozess?")
schritte = st.text_area("6. Welche Zwischenschritte erfolgen?")
entscheidung = st.text_input("7. Gibt es Entscheidungsstellen? Wenn ja, welche?")
ende = st.text_input("8. Wie endet der Prozess?")
besonderheiten = st.text_area("9. Gibt es Besonderheiten oder bekannte Risiken?")

if st.button("📄 Prozessbeschreibung generieren"):
    st.subheader("📝 Ergebnis:")
    prozessbericht = f"""
### Prozess: {prozessname}

**Auslöser:** {ausloeser}  
**Ziel:** {ziel}  
**Beteiligte Rollen/Abteilungen:**  
{akteure}

**Ablauf:**  
1. **Start:** {start}  
2. **Zwischenschritte:**  
{schritte}

**Entscheidungen:** {entscheidung}  
**Prozessende:** {ende}  

**Besonderheiten / Risiken:**  
{besonderheiten}

*Erstellt am {datetime.today().strftime('%d.%m.%Y')}*
"""
    st.code(prozessbericht, language="markdown")

    st.download_button(
        label="📥 Markdown-Datei herunterladen",
        data=prozessbericht,
        file_name=f"{prozessname.replace(' ', '_')}_Prozessbeschreibung.md",
        mime="text/markdown"
    )
