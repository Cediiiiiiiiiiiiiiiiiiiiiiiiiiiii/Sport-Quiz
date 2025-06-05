import streamlit as st

# --- Fragenliste ---
fragen = [
    {
        "bild": "https://via.placeholder.com/600x120.png?text=Foul+Situation",
        "text": "Ein Spieler foult – was tust du?",
        "antworten": [
            ("✅ Ich melde es sofort – Fairplay!", 5),
            ("😐 Ich warte, ob der Schiri was sieht.", 3),
            ("❌ Ich schweige – Vorteil nutzen!", 1)
        ]
    },
    {
        "bild": "https://via.placeholder.com/600x120.png?text=Schwalbe",
        "text": "Du könntest mit einer Schwalbe einen Elfer bekommen.",
        "antworten": [
            ("✅ Ich bleibe aufrecht – keine Lüge.", 5),
            ("😐 Ich lasse mich leicht fallen…", 3),
            ("❌ Ich täusche klar – Elfer ist Elfer!", 1)
        ]
    },
    # ... weitere Fragen (können beliebig ergänzt werden)
]

# --- Streamlit App Aufbau ---
st.set_page_config(page_title="Sportethisches Quiz", layout="centered")
st.title("⚽ Sportethisches Entscheidungsquiz")
st.markdown("""
Beantworte die folgenden Fragen ehrlich – du bekommst am Ende deinen sportmoralischen Typ und einen passenden Vorbild-Athleten!
""")

# --- Nutzername ---
spielername = st.text_input("Wie heißt du?")

if spielername:
    punkte = []

    for i, frage in enumerate(fragen):
        st.markdown(f"### Frage {i+1}: {frage['text']}")
        st.image(frage["bild"], use_column_width=True)
        antwort = st.radio("", [a[0] for a in frage["antworten"]], key=i)

        if antwort:
            for text, wert in frage["antworten"]:
                if antwort == text:
                    punkte.append(wert)

    if len(punkte) == len(fragen):
        avg = sum(punkte) / len(punkte)

        if avg >= 4.5:
            typ = "🏅 Vorbildsportler"
            athlet = "Roger Federer"
        elif avg >= 3.5:
            typ = "📐 Moralischer Stratege"
            athlet = "Lionel Messi"
        elif avg >= 2.5:
            typ = "⚖️ Kontrollierter Pragmatiker"
            athlet = "Serena Williams"
        elif avg >= 1.5:
            typ = "🎭 Opportunist"
            athlet = "Diego Maradona"
        else:
            typ = "🤑 Egoist"
            athlet = "Flavio Briatore"

        st.success(f"**Auswertung für {spielername}:**")
        st.write(f"**Durchschnittlicher Score:** {avg:.2f}")
        st.write(f"**Typ:** {typ}")
        st.write(f"**Beispiel-Athlet:** {athlet}")

        # Optional: speichern (lokal auf Server)
        with open(f"{spielername}_ergebnis.txt", "w", encoding="utf-8") as f:
            f.write(f"Spieler: {spielername}\nScore: {avg:.2f}\nTyp: {typ}\nAthlet: {athlet}")
