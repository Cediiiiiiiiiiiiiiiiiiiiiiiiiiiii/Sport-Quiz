import streamlit as st
import random

# --- Seiten-Setup ---
st.set_page_config(page_title="Sportethik-Quiz", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
        body {background-color: #e6f0ff;}
        .question-img {border-radius: 10px; margin-bottom: 1rem;}
    </style>
""", unsafe_allow_html=True)

# --- Einleitungs-Text ---
st.title("⚽ Sportethik-Quiz")
st.markdown("**Mein Sportsfreund...** Mal sehen, wie fair du bist – sei ehrlich! 💬")
spielername = st.text_input("Wie heißt du?")

# --- Fragen mit Bildern ---
fragen = [
    {
        "bild": "https://images.unsplash.com/photo-1517649763962-0c623066013b",  # Fußball-Foul
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort – Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige – Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1547347298-4074fc3086f0",  # Schwimmen
        "text": "Du siehst, wie jemand beim Schwimmen abkürzt.",
        "antworten": [
            ("✅ Ich melde es dem Trainer.", 5),
            ("😐 Ich bin mir nicht ganz sicher…", 3),
            ("❌ Ist doch sein Problem, nicht meins.", 1)
        ]
    },
    # Weitere Fragen können hier ergänzt werden...
]

# --- Fortschritt & Zustand ---
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []

# --- Quiz anzeigen, wenn Name vorhanden ---
if spielername:
    frage_index = st.session_state.frage_index

    if frage_index < len(fragen):
        frage = fragen[frage_index]
        st.markdown(f"### Frage {frage_index + 1}: {frage['text']}")
        st.image(frage["bild"], use_container_width=True)

        auswahl = st.radio("Wähle deine Antwort:", [a[0] for a in frage["antworten"]], key=frage_index)
        if st.button("Weiter"):
            for text, wert in frage["antworten"]:
                if auswahl == text:
                    st.session_state.punkte.append(wert)
                    break
            st.session_state.frage_index += 1
            st.experimental_rerun()

    else:
        avg = sum(st.session_state.punkte) / len(st.session_state.punkte)
        if avg >= 4.5:
            typ = "🏅 Vorbildsportler"
            athlet = "Roger Federer"
            bild = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Roger_Federer_%28184150819%29.jpg"
        elif avg >= 3.5:
            typ = "📐 Moralischer Stratege"
            athlet = "Lionel Messi"
            bild = "https://upload.wikimedia.org/wikipedia/commons/8/80/Lionel_Messi_20180626.jpg"
        elif avg >= 2.5:
            typ = "⚖️ Kontrollierter Pragmatiker"
            athlet = "Serena Williams"
            bild = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Serena_Williams_2013_US_Open.jpg"
        elif avg >= 1.5:
            typ = "🎭 Opportunist"
            athlet = "Diego Maradona"
            bild = "https://upload.wikimedia.org/wikipedia/commons/5/5f/Maradona_versus_Belgium_1982.jpg"
        else:
            typ = "🤑 Egoist"
            athlet = "Flavio Briatore"
            bild = "https://upload.wikimedia.org/wikipedia/commons/7/78/Flavio_Briatore_2012.jpg"

        st.success(f"**Ergebnis für {spielername}:**")
        st.image(bild, caption=athlet, width=300)
        st.markdown(f"**Typ:** {typ}")
        st.markdown(f"**Beispiel-Athlet:** {athlet}")
        st.markdown(f"**Durchschnittlicher Score:** {avg:.2f} von 5")

        with open(f"{spielername}_ergebnis.txt", "w", encoding="utf-8") as f:
            f.write(f"Spieler: {spielername}\nScore: {avg:.2f}\nTyp: {typ}\nAthlet: {athlet}")
