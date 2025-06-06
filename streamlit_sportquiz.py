import streamlit as st

# Seitenlayout + Style
st.set_page_config(page_title="Sportethik-Quiz", layout="centered")
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-color: #d0e7ff;
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Titel und Einleitung
st.title("⚽ Sportethik-Quiz")
st.markdown("**Mein Sportsfreund...** Mal sehen, wie fair du bist – sei ehrlich! 💬")
spielername = st.text_input("Wie heißt du?")

# Fragen vorbereiten
fragen = [
    {
        "bild": "https://images.unsplash.com/photo-1618424181686-90f6ce22a2f3",  # Fußball-Foul
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort – Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige – Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1584467735871-3d84d35f5823",  # Schwalbe
        "text": "Du könntest mit einer Schwalbe einen Elfer bekommen.",
        "antworten": [
            ("✅ Ich bleibe aufrecht – keine Lüge.", 5),
            ("😐 Ich lasse mich leicht fallen…", 3),
            ("❌ Ich täusche klar – Elfer ist Elfer!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",  # Doping
        "text": "Ein Freund will, dass du seine Dopingprobe vertauschst.",
        "antworten": [
            ("✅ Kommt nicht in Frage – unfair!", 5),
            ("😐 Ich denke darüber nach…", 3),
            ("❌ Klar – wir müssen gewinnen!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1502810190503-830027b2a58b",  # Verletzter Gegner
        "text": "Ein Gegner liegt verletzt, aber ihr greift an.",
        "antworten": [
            ("✅ Ich spiele den Ball ins Aus.", 5),
            ("😐 Ich zögere erstmal.", 3),
            ("❌ Ich spiele sofort weiter!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1563298723-dcfebaa392e3",  # Zu viele Spieler
        "text": "Ihr habt zu viele Spieler auf dem Feld.",
        "antworten": [
            ("✅ Ich sage es sofort.", 5),
            ("😐 Ich tue so, als ob nichts wär.", 3),
            ("❌ Ich verschweige es aktiv.", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1517649763962-0c623066013b",  # Ball im Aus
        "text": "Du hast gesehen, dass der Ball im Aus war.",
        "antworten": [
            ("✅ Ich sage es direkt!", 5),
            ("😐 Ich bin mir nicht ganz sicher…", 3),
            ("❌ Ich schweige – Schiri soll's sehen.", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1616789911239-45fc503f1556",  # Traineranweisung
        "text": "Dein Trainer fordert dich auf, ein Foul zu simulieren.",
        "antworten": [
            ("✅ Ich lehne das ab!", 5),
            ("😐 Ich überlege kurz…", 3),
            ("❌ Ich mache es für den Sieg!", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1593113595264-cd38b1cd8fbe",  # Interview
        "text": "Nach dem Spiel wirst du interviewt: Ehrlich oder nicht?",
        "antworten": [
            ("✅ Ich sage die Wahrheit.", 5),
            ("😐 Ich bleibe vage.", 3),
            ("❌ Ich lüge zum Schutz des Teams.", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b",  # Teambesprechung
        "text": "Sollst du deinem Team Fehlverhalten ansprechen?",
        "antworten": [
            ("✅ Ja – Verantwortung zeigen!", 5),
            ("😐 Ich rede privat mit jemandem.", 3),
            ("❌ Ich sage gar nichts.", 1)
        ]
    },
    {
        "bild": "https://images.unsplash.com/photo-1521412644187-c49fa049e84d",  # Publikum
        "text": "Im Finale sollst du unfair spielen – was tun?",
        "antworten": [
            ("✅ Ich bleibe meinem Gewissen treu.", 5),
            ("😐 Ich mache mit Bauchweh mit.", 3),
            ("❌ Ich ziehe’s voll durch!", 1)
        ]
    }
]

if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []

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
            st.rerun()

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
