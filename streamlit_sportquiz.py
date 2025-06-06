streamlit as st

# Seitenlayout + Style
st.set_page_config(page_title="Sportethik-Quiz", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] > .main {
        background-color: #d0e7ff;
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Titel und Einleitung
st.title("⚽ Sportethik-Quiz")
st.markdown("**Mein Sportsfreund...** Mal sehen, wie fair du bist – sei ehrlich! 💬")
spielername = st.text_input("Wie heißt du?")

# Fragen vorbereiten mit stabilen Bildquellen
fragen = [
    {
        "bild": "https://shootscoresoccer.com/wp-content/uploads/2022/01/How-to-Tackle-in-Soccer.jpg",
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort – Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige – Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://img.zeit.de/sport/2017-03/arjen-robben-schwalbe/wide__1000x562__desktop__scale_2",
        "text": "Du könntest mit einer Schwalbe einen Elfer bekommen.",
        "antworten": [
            ("✅ Ich bleibe aufrecht – keine Lüge.", 5),
            ("😐 Ich lasse mich leicht fallen…", 3),
            ("❌ Ich täusche klar – Elfer ist Elfer!", 1)
        ]
    },
    {
        "bild": "https://thumbs.dreamstime.com/z/test-rohr-mit-blutprobe-f%C3%BCr-doping-test-78831563.jpg?ct=jpeg",
        "text": "Ein Freund will, dass du seine Dopingprobe vertauschst.",
        "antworten": [
            ("✅ Kommt nicht in Frage – unfair!", 5),
            ("😐 Ich denke darüber nach…", 3),
            ("❌ Klar – wir müssen gewinnen!", 1)
        ]
    },
    {
        "bild": "https://shootscoresoccer.com/wp-content/uploads/2022/01/How-to-Tackle-in-Soccer.jpg",
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort – Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige – Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://img.zeit.de/sport/2017-03/arjen-robben-schwalbe/wide__1000x562__desktop__scale_2",
        "text": "Du könntest mit einer Schwalbe einen Elfer bekommen.",
        "antworten": [
            ("✅ Ich bleibe aufrecht – keine Lüge.", 5),
            ("😐 Ich lasse mich leicht fallen…", 3),
            ("❌ Ich täusche klar – Elfer ist Elfer!", 1)
        ]
    },
    {
        "bild": "https://thumbs.dreamstime.com/z/test-rohr-mit-blutprobe-f%C3%BCr-doping-test-78831563.jpg?ct=jpeg",
        "text": "Ein Freund will, dass du seine Dopingprobe vertauschst.",
        "antworten": [
            ("✅ Kommt nicht in Frage – unfair!", 5),
            ("😐 Ich denke darüber nach…", 3),
            ("❌ Klar – wir müssen gewinnen!", 1)
        ]
    },
    {
        "bild": "",
        "text": "Ein Gegner liegt verletzt, aber ihr greift an.",
        "antworten": [
            ("✅ Ich spiele den Ball ins Aus.", 5),
            ("😐 Ich zögere erstmal.", 3),
            ("❌ Ich spiele sofort weiter!", 1)
        ]
    },
    {
        "bild": "https://www.bestsellerratings.com/content/images/2023/05/Volleyball-team.jpg",
        "text": "Ihr habt zu viele Spieler auf dem Feld.",
        "antworten": [
            ("✅ Ich sage es sofort.", 5),
            ("😐 Ich tue so, als ob nichts wär.", 3),
            ("❌ Ich verschweige es aktiv.", 1)
        ]
    },
    {
        "bild": "https://www.susanzaro.com/site/wp-content/uploads/2015/06/ball-out-300x224.jpg",
        "text": "Du hast gesehen, dass der Ball im Aus war.",
        "antworten": [
            ("✅ Ich sage es direkt!", 5),
            ("😐 Ich bin mir nicht ganz sicher…", 3),
            ("❌ Ich schweige – Schiri soll's sehen.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Soccer_coach.jpg",
        "text": "Dein Trainer fordert dich auf, ein Foul zu simulieren.",
        "antworten": [
            ("✅ Ich lehne das ab!", 5),
            ("😐 Ich überlege kurz…", 3),
            ("❌ Ich mache es für den Sieg!", 1)
        ]
    },
    {
        "bild": "https://www.si.com/.image/c_fill,w_2160,ar_16:9,f_auto,q_auto,g_auto/MTY4MDI3NDM4MzcwMzM0MDgw/nick-young-postgame-interviewjpg.jpg",
        "text": "Nach dem Spiel wirst du interviewt: Ehrlich oder nicht?",
        "antworten": [
            ("✅ Ich sage die Wahrheit.", 5),
            ("😐 Ich bleibe vage.", 3),
            ("❌ Ich lüge zum Schutz des Teams.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/2/25/Football_team_huddle.jpg",
        "text": "Sollst du deinem Team Fehlverhalten ansprechen?",
        "antworten": [
            ("✅ Ja – Verantwortung zeigen!", 5),
            ("😐 Ich rede privat mit jemandem.", 3),
            ("❌ Ich sage gar nichts.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/3/34/Olympic_flag_with_crowd.jpg",
        "text": "Im Finale sollst du unfair spielen – was tun?",
        "antworten": [
            ("✅ Ich bleibe meinem Gewissen treu.", 5),
            ("😐 Ich mache mit Bauchweh mit.", 3),
            ("❌ Ich ziehe’s voll durch!", 1)
        ]
    }
]

# Fortschritt und Zustand
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []

if spielername:
    frage_index = st.session_state.frage_index

    if frage_index < len(fragen):
        frage = fragen[frage_index]
        st.markdown(f"#### Frage {frage_index + 1} von {len(fragen)}")
        st.markdown(f"### {frage['text']}")
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
",
        "text": "Ein Gegner liegt verletzt, aber ihr greift an.",
        "antworten": [
            ("✅ Ich spiele den Ball ins Aus.", 5),
            ("😐 Ich zögere erstmal.", 3),
            ("❌ Ich spiele sofort weiter!", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/f/fc/7_players_on_field.jpg",
        "text": "Ihr habt zu viele Spieler auf dem Feld.",
        "antworten": [
            ("✅ Ich sage es sofort.", 5),
            ("😐 Ich tue so, als ob nichts wär.", 3),
            ("❌ Ich verschweige es aktiv.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Referee_flags_offside.jpg",
        "text": "Du hast gesehen, dass der Ball im Aus war.",
        "antworten": [
            ("✅ Ich sage es direkt!", 5),
            ("😐 Ich bin mir nicht ganz sicher…", 3),
            ("❌ Ich schweige – Schiri soll's sehen.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Soccer_coach.jpg",
        "text": "Dein Trainer fordert dich auf, ein Foul zu simulieren.",
        "antworten": [
            ("✅ Ich lehne das ab!", 5),
            ("😐 Ich überlege kurz…", 3),
            ("❌ Ich mache es für den Sieg!", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Sports_interview.jpg",
        "text": "Nach dem Spiel wirst du interviewt: Ehrlich oder nicht?",
        "antworten": [
            ("✅ Ich sage die Wahrheit.", 5),
            ("😐 Ich bleibe vage.", 3),
            ("❌ Ich lüge zum Schutz des Teams.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/2/25/Football_team_huddle.jpg",
        "text": "Sollst du deinem Team Fehlverhalten ansprechen?",
        "antworten": [
            ("✅ Ja – Verantwortung zeigen!", 5),
            ("😐 Ich rede privat mit jemandem.", 3),
            ("❌ Ich sage gar nichts.", 1)
        ]
    },
    {
        "bild": "https://upload.wikimedia.org/wikipedia/commons/3/34/Olympic_flag_with_crowd.jpg",
        "text": "Im Finale sollst du unfair spielen – was tun?",
        "antworten": [
            ("✅ Ich bleibe meinem Gewissen treu.", 5),
            ("😐 Ich mache mit Bauchweh mit.", 3),
            ("❌ Ich ziehe’s voll durch!", 1)
        ]
    }
]

# Fortschritt und Zustand
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []

if spielername:
    frage_index = st.session_state.frage_index

    if frage_index < len(fragen):
        frage = fragen[frage_index]
        st.markdown(f"#### Frage {frage_index + 1} von {len(fragen)}")
        st.markdown(f"### {frage['text']}")
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
