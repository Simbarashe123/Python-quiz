def run_quiz():
    print("Willkommen zum Python Quiz!")

    name = input("Wie heißt du? ")
    print("Hallo", name, "! Viel Erfolg beim Quiz.")

    score = 0

    questions = [
        ("Was ist die richtige Dateiendung für Python?", ".py"),
        ("Welches Schlüsselwort wird für Schleifen verwendet?", "for"),
        ("Welche Funktion gibt Text aus?", "print"),
        ("Welches Symbol wird für Kommentare verwendet?", "#"),
        ("Welches Schlüsselwort wird für Bedingungen verwendet?", "if")
    ]

    for question, answer in questions:
        user_answer = input(question + " ")

        if user_answer.lower() == answer:
            print("Richtig!")
            score += 1
        else:
            print("Falsch! Die richtige Antwort ist:", answer)

    print("\nQuiz beendet!")
    print(name, ", deine Punktzahl ist", score, "von", len(questions))


while True:
    run_quiz()

    play_again = input("Möchtest du noch einmal spielen? (ja/nein): ")

    if play_again.lower() != "ja":
        print("Danke fürs Spielen. Auf Wiedersehen!")
        break