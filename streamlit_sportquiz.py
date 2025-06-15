# Erweiterte Version des Sportethik-Quiz mit Fortschrittsbalken, Farbe und Auswertung

import streamlit as st
import time

# Seitenlayout + Style
st.set_page_config(page_title="Sportethik-Quiz", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid=\"stAppViewContainer\"] > .main {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .cool-score {
        font-size: 2rem;
        font-weight: bold;
        color: #007acc;
    }
    .stProgress > div > div > div > div {
        background-color: #007acc;
    }
    .question-block {
        background-color: #ffffffcc;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Titel und Einleitung
st.title("🏅 Sportethik-Quiz")
st.markdown("**Hey Sportsfreundin oder Sportsfreund!**\n\nWas Fairplay wirklich bedeutet? Finde es heraus – und sei ehrlich zu dir selbst. 💬")
spielername = st.text_input("Wie heißt du?")

# Fragen vorbereiten (siehe vorherige vollständige Liste – hier ausgelassen zur Kürze)
fragen = [
    {
        "bild": "https://shootscoresoccer.com/wp-content/uploads/2022/01/How-to-Tackle-in-Soccer.jpg",
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort, Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige, wir müssen den Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://img.zeit.de/sport/2017-03/arjen-robben-schwalbe/wide__1000x562__desktop__scale_2",
        "text": "Du könntest mit einer Schwalbe einen Elfer bekommen.",
        "antworten": [
            ("✅ Ich bleibe aufrecht.", 5),
            ("😐 Ich lasse mich leicht fallen…", 3),
            ("❌ Ich täusche klar, Elfer ist Elfer!", 1)
        ]
    },
    {
        "bild": "https://cdn.dmcl.biz/media/image/99697/o/GettyImages-501532292.jpg",
        "text": "Ein Freund will, dass du seine Dopingprobe vertauschst.",
        "antworten": [
            ("✅ Kommt nicht in Frage, das ist unfair!", 5),
            ("😐 Ich denke darüber nach…", 3),
            ("❌ Klar, wir müssen gewinnen!", 1)
        ]
    },
    {
        "bild": "https://www.dbs-npc.de/assets/images/6/20160911-sw-102323-15400-okr_hp-59a2adee.jpg",
        "text": "Ein Teamkollege springt beim Staffelstart zu früh ins Wasser, aber der Schiedsrichter merkt es nicht. Was tust du?",
        "antworten": [
            ("✅ Ich melde den Frühstart, Ehrlichkeit zählt.", 5),
            ("😐 Ich frage zuerst den Rest des Teams, ob wir es zugeben wollen.", 3),
            ("❌Ich sage nichts, Pech für die anderen.", 1)
        ]
    },
    {
        "bild": "https://cdn.arstechnica.net/wp-content/uploads/2019/04/basketballTOP.jpg",
        "text": "Du merkst das du den Basketball noch berührt hast bevor er ins aus ging, doch der Schiri gibt euch den Einwurf, was tust du?",
        "antworten": [
            ("✅ Ich sage dem Schiri, dass ich ihn noch berührt habe.", 5),
            ("😐 Ich warte und schaue ob jemand protestiert.", 3),
            ("❌ Ich nehme es dankend an und nutze die Chance.", 1)
        ]
    },
    {
        "bild": "https://e6.365dm.de/23/02/1600x900/skysport_de-shiffrin-riesenslalom_6059422.jpg?20230216133332",
        "text": "Beim Riesenslalom bemerkt niemand, dass du ein Tor ausgelassen hast. Du wärst mit der Zeit unter den Top 3. Was tust du?",
        "antworten": [
            ("✅ Ich melde es sobald ich unten angekommen bin.", 5),
            ("😐 Ich hoffe, dass es niemand gesehen hat.", 3),
            ("❌ Ich sage nichts und hol mir meine Medallie. ", 1)
        ]
    },
    {
        "bild": "https://static01.nyt.com/images/2014/07/05/sports/sub-brazilcup1/sub-brazilcup1-master1050.jpg",
        "text": "Ein Gegner liegt verletzt, aber ihr greift an.",
        "antworten": [
            ("✅ Ich spiele den Ball ins Aus.", 5),
            ("😐 Ich zögere erstmal.", 3),
            ("❌ Ich spiele sofort weiter, wir haben Überzahl!", 1)
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
        "bild": "https://www.felsland-teamtage.de/media/k2/items/cache/867519228d1d5325856fc61d710ded0e_L.jpg",
        "text": "Du bemerkst, dass dein Zielstand falsch kalibriert ist, der nächste Schütze könnte benachteiligt sein. Was tust du?",
        "antworten": [
            ("✅ Ich melde das sofort dem Kampfrichter.", 5),
            ("😐 Ich sage es nur, wenn es jemanden auffällt.", 3),
            ("❌ Ich ignoriere es, betrifft mich nicht.", 1)
        ]
    },
    {
        "bild": "https://th.bing.com/th/id/R.313f17bdcb36bd1ca50daff3bd2db3e4?rik=cJuPucJIX1YEYQ&pid=ImgRaw&r=0",
        "text": "Du weisst das dein Gegner im Ring schon mehrfach sein rechtes Bein gebrochen hat und es nie ganz verheilt ist, was tust du?.",
        "antworten": [
            ("✅ Ich trete ihm extra nicht dagegen.", 5),
            ("😐 Wenn er zu Krass die Oberhand hat, trete ich vielleicht einmal dagegen. ", 3),
            ("❌ Ich fokussiere mich nur auf das Bein!", 1)
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
        "bild": "https://th.bing.com/th/id/R.035ac5351116b3f8d593f50f6019fbdb?rik=QQes4iNVI3m5WA&pid=ImgRaw&r=0",
        "text": "Beim Bodenturnen lief dir Wettbewerb nicht gut, aber du hast gesehen wie dein Trainer der Jury Geld zusteckte und gewinnst Gold, was tust du?",
        "antworten": [
            ("✅ Ich melde es dem Verband und erkenne den unfairen Sieg nicht an. ", 5),
            ("😐 Ich warte ab ob jemand sich beklagt und gib es dann zu.", 3),
            ("❌ Ich sage gar nichts, ich habe nichts gesehen...", 1)
        ]
    },
    {
        "bild": "https://www.middleeasteye.net/sites/default/files/styles/article_page/public/images-story/Qatar-World-Cup-Argentina-December-2022-AFP.jpg.webp?itok=zZCpLq3-",
        "text": "Im Finale sollst du unfair spielen – was tun?",
        "antworten": [
            ("✅ Ich bleibe meinem Gewissen treu.", 5),
            ("😐 Ich mache mit Bauchweh mit.", 3),
            ("❌ Ich ziehe’s voll durch!", 1)
        ]
    }
]  # Hier steht deine komplette Fragenliste (wie zuvor aktualisiert)

# Fortschritt und Zustand
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []
    st.session_state.timer_start = time.time()

elapsed_time = int(time.time() - st.session_state.timer_start)
st.markdown(f"⏱️ **Verstrichene Zeit:** {elapsed_time} Sekunden  ")
st.caption("(Nur zur Orientierung – kein Zeitlimit, nimm dir ruhig Zeit zum Nachdenken!)")

if spielername:
    frage_index = st.session_state.frage_index
    total_fragen = len(fragen)

    if frage_index < total_fragen:
        frage = fragen[frage_index]

        # Fortschrittsbalken anzeigen
        st.progress((frage_index + 1)
        st.markdown("<style>.element-container:has(.stProgress) + div {display: none;}</style>", unsafe_allow_html=True) / total_fragen)

        with st.container():
            st.markdown(f"<div class='question-block'>", unsafe_allow_html=True)
            st.markdown(f"#### Frage {frage_index + 1} von {total_fragen}")
            st.markdown(f"### {frage['text']}")
            st.image(frage["bild"], use_container_width=True)

            auswahl = st.radio("Wähle deine Antwort:", [a[0] for a in frage["antworten"]], key=frage_index)
            if st.button("👉 Weiter zur nächsten Frage", type="primary"):
                for text, wert in frage["antworten"]:
                    if auswahl == text:
                        st.session_state.punkte.append(wert)
                        break
                st.session_state.frage_index += 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        avg = sum(st.session_state.punkte) / total_fragen
        if avg >= 4.5:
            typ = "🏅 Vorbildsportler"
            athlet = "Roger Federer"
            bild = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Roger_Federer_%28184150819%29.jpg"
        elif avg >= 3.5:
            typ = "📐 Moralischer Stratege"
            athlet = "Lionel Messi"
            bild = "https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltf7695f98c1f01bd9/62cbfb91c9db8842cf76cb5b/GHP_MESSI-BOOTS_16-9.jpg"
        elif avg >= 2.5:
            typ = "⚖️ Kontrollierter Pragmatiker"
            athlet = "Serena Williams"
            bild = "https://th.bing.com/th/id/OIP.E6ceK3TePOweDrQrvQCMBwHaFj"
        elif avg >= 1.5:
            typ = "🎭 Opportunist"
            athlet = "Diego Maradona"
            bild = "https://upload.wikimedia.org/wikipedia/commons/5/5f/Maradona_versus_Belgium_1982.jpg"
        else:
            typ = "🤑 Egoist"
            athlet = "Flavio Briatore"
            bild = "https://www.monaco-tribune.com/wp-content/uploads/2020/11/flavio-briatore-min.jpg"

        st.success(f"**Ergebnis für {spielername}:**")
        st.image(bild, caption=athlet, width=300)
        st.markdown(f"**Typ:** {typ}")
        st.markdown(f"**Beispiel-Athlet:** {athlet}")
        st.markdown(f"**Durchschnittlicher Score:** {avg:.2f} von 5")
        st.markdown(f"**⏱️ Gesamtzeit:** {elapsed_time} Sekunden")

        import datetime
from fpdf import FPDF

# PDF-Zertifikat erzeugen
class Zertifikat(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Sportethik-Quiz Zertifikat", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Erstellt am {datetime.date.today()}", 0, 0, "C")

    def inhalt(self, name, typ, punkte, athlet, dauer):
        self.set_font("Arial", size=12)
        self.ln(10)
        self.multi_cell(0, 10, f"Teilnehmer: {name}

Typ: {typ}
Durchschnittlicher Score: {punkte:.2f} / 5
Beispiel-Athlet: {athlet}
Dauer: {dauer} Sekunden")

pdf = Zertifikat()
pdf.add_page()
pdf.inhalt(spielername, typ, avg, athlet, elapsed_time)
zertifikat_pfad = f"{spielername}_zertifikat.pdf"
pdf.output(zertifikat_pfad)

with open(zertifikat_pfad, "rb") as f:
    st.download_button("📄 Zertifikat herunterladen", f, file_name=zertifikat_pfad, mime="application/pdf") as f:
            f.write(f"Spieler: {spielername}\nScore: {avg:.2f}\nTyp: {typ}\nAthlet: {athlet}\nZeit: {elapsed_time} Sekunden")
