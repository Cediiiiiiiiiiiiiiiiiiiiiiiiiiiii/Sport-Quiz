import streamlit as st
import time

# Seitenlayout + Style
st.set_page_config(page_title="Sportethik-Quiz", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .cool-score {
        font-size: 2rem;
        font-weight: bold;
        color: #007acc;
    }
    </style>
""", unsafe_allow_html=True)

# Titel und Einleitung
st.title("⚽ Sportethik-Quiz")
st.markdown("**Mein Sportsfreund...** Mal sehen, wie fair du bist – sei ehrlich mit dir selbst! 💬")
spielername = st.text_input("Wie heißt du?")

# Fragen vorbereiten
fragen = [
    {
        "bild": "https://shootscoresoccer.com/wp-content/uploads/2022/01/How-to-Tackle-in-Soccer.jpg",
        "text": "Ein Mitspieler foult, was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort. Fairplay geht vor!", 5),
            ("😐 Ich warte ab, ob der Schiri reagiert.", 3),
            ("❌ Ich schweige. Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://img.zeit.de/sport/2017-03/arjen-robben-schwalbe/wide__1000x562__desktop__scale_2",
        "text": "Mit einer Schwalbe könntest du einen Elfer holen, was jetzt?",
        "antworten": [
            ("✅ Ich bleibe fair und täusche nichts vor.", 5),
            ("😐 Ich falle leicht, vielleicht merkt es keiner...", 3),
            ("❌ Ich gehe klar zu Boden. Elfer ist Elfer!", 1)
        ]
    },
    {
        "bild": "https://cdn.dmcl.biz/media/image/99697/o/GettyImages-501532292.jpg",
        "text": "Ein Freund bittet dich, seine Dopingprobe zu vertauschen.",
        "antworten": [
            ("✅ Niemals! Das ist unfair und unsportlich.", 5),
            ("😐 Ich denke kurz darüber nach...", 3),
            ("❌ Ich helfe ihm – Hauptsache Sieg!", 1)
        ]
    },
    {
        "bild": "https://www.dbs-npc.de/assets/images/6/20160911-sw-102323-15400-okr_hp-59a2adee.jpg",
        "text": "Dein Teamkollege springt zu früh ins Wasser, der Schiri merkt es nicht. Was tust du?",
        "antworten": [
            ("✅ Ich melde den Frühstart sofort.", 5),
            ("😐 Ich bespreche es mit dem Team.", 3),
            ("❌ Ich sage nichts – Glück gehabt!", 1)
        ]
    },
    {
        "bild": "https://cdn.arstechnica.net/wp-content/uploads/2019/04/basketballTOP.jpg",
        "text": "Du warst noch am Ball, bevor er ins Aus ging – der Schiri gibt euch Einwurf.",
        "antworten": [
            ("✅ Ich sage dem Schiri die Wahrheit.", 5),
            ("😐 Ich warte ab, ob jemand protestiert.", 3),
            ("❌ Ich nehme es an – sein Fehler!", 1)
        ]
    },
    {
        "bild": "https://e6.365dm.de/23/02/1600x900/skysport_de-shiffrin-riesenslalom_6059422.jpg?20230216133332",
        "text": "Du hast ein Tor ausgelassen bei der Abfahrt – deine Zeit reicht für die Top 3.",
        "antworten": [
            ("✅ Ich breche ab und melde es sofort.", 5),
            ("😐 Ich hoffe, es hat niemand gesehen.", 3),
            ("❌ Ich schweige – yes endlich mal eine Medaille!", 1)
        ]
    },
    {
        "bild": "https://static01.nyt.com/images/2014/07/05/sports/sub-brazilcup1/sub-brazilcup1-master1050.jpg",
        "text": "Ein Gegner liegt verletzt. Du bist im Konter mit einer riesen Chance – wie reagierst du?",
        "antworten": [
            ("✅ Ich spiele den Ball ins Aus.", 5),
            ("😐 Ich zögere kurz.", 3),
            ("❌ Ich spiele weiter – Überzahl nutzen!", 1)
        ]
    },
    {
        "bild": "https://www.bestsellerratings.com/content/images/2023/05/Volleyball-team.jpg",
        "text": "Ihr habt einen Spieler zu viel auf dem Feld – keiner merkt es.",
        "antworten": [
            ("✅ Ich melde es sofort.", 5),
            ("😐 Ich tue so, als wüsste ich nichts.", 3),
            ("❌ Ich schweige aktiv.", 1)
        ]
    },
    {
        "bild": "https://www.felsland-teamtage.de/media/k2/items/cache/867519228d1d5325856fc61d710ded0e_L.jpg",
        "text": "Der Zielstand ist falsch kalibriert – du weißt es.",
        "antworten": [
            ("✅ Ich melde es dem Kampfrichter.", 5),
            ("😐 Nur wenn es jemandem auffällt.", 3),
            ("❌ Ich ignoriere es – betrifft mich nicht.", 1)
        ]
    },
    {
        "bild": "https://th.bing.com/th/id/R.313f17bdcb36bd1ca50daff3bd2db3e4?rik=cJuPucJIX1YEYQ&pid=ImgRaw&r=0",
        "text": "Dein Gegner hatte früher einen Beinbruch – du weißt es, da du ihn von früher kennts.",
        "antworten": [
            ("✅ Ich vermeide das Bein bewusst.", 5),
            ("😐 Wenn es eng wird, trete ich einmal hin.", 3),
            ("❌ Ich greife gezielt das Bein an.", 1)
        ]
    },
    {
        "bild": "https://www.si.com/.image/c_fill,w_2160,ar_16:9,f_auto,q_auto,g_auto/MTY4MDI3NDM4MzcwMzM0MDgw/nick-young-postgame-interviewjpg.jpg",
        "text": "Du wirst nach dem Spiel interviewt, ihr habt verloren und die Moral des Teams ist am boden zerstört, der Teamzusammenhalt ist aktuell gleich null – ehrlich oder nicht?",
        "antworten": [
            ("✅ Ich sage die Wahrheit.", 5),
            ("😐 Ich bleibe vage.", 3),
            ("❌ Ich lüge zum Schutz des Teams.", 1)
        ]
    },
    {
        "bild": "https://th.bing.com/th/id/R.035ac5351116b3f8d593f50f6019fbdb?rik=QQes4iNVI3m5WA&pid=ImgRaw&r=0",
        "text": "Dein Trainer besticht die Jury und deshalb bekommst du Gold trotz Fehlern, dir ist bewusst, die Konkurrenz hat hart dafür gearbeitet und definitv besser performt als du, was nun?",
        "antworten": [
            ("✅ Ich melde es und verzichte auf den Sieg.", 5),
            ("😐 Ich warte ab, ob jemand etwas merkt.", 3),
            ("❌ Ich sage nichts – passt schon!", 1)
        ]
    },
    {
        "bild": "https://www.middleeasteye.net/sites/default/files/styles/article_page/public/images-story/Qatar-World-Cup-Argentina-December-2022-AFP.jpg.webp?itok=zZCpLq3-",
        "text": "Beinahe durch ein Wunder gewinnt ihr das Halbfinal. Ihr seid nun der klare Underdog und vor dem Finale wird dir gesagt: Spiel unfair, das ist unsere einzige Chance. Wie entscheidest du?",
        "antworten": [
            ("✅ Ich bleibe meinem Gewissen treu.", 5),
            ("😐 Ich mache mit Bauchweh mit.", 3),
            ("❌ Ich ziehe es voll durch!", 1)
        ]
    }
]

# Zustand & Timer
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
    st.session_state.punkte = []
    st.session_state.timer_start = time.time()

elapsed = int(time.time() - st.session_state.timer_start)
st.markdown(f"⏱️ **Verstrichene Zeit:** {elapsed} Sekunden")
st.caption("(Nur zur Orientierung – du hast unbegrenzt Zeit)")

# Quizlogik
if spielername:
    frage_index = st.session_state.frage_index
    total_fragen = len(fragen)

    if frage_index < total_fragen:
        frage = fragen[frage_index]
        st.progress((frage_index + 1) / total_fragen)

        st.markdown(f"#### Frage {frage_index + 1} von {total_fragen}")
        st.markdown(f"### {frage['text']}")
        st.image(frage['bild'], use_container_width=True)

        auswahl = st.radio("Wähle deine Antwort:", [a[0] for a in frage['antworten']], key=frage_index)
        if st.button("👉 Weiter zur nächsten Frage", type="primary"):
            for text, wert in frage['antworten']:
                if auswahl == text:
                    st.session_state.punkte.append(wert)
                    break
            st.session_state.frage_index += 1
            st.rerun()

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
        st.markdown(f"**⏱️ Gesamtzeit:** {elapsed} Sekunden")

    
