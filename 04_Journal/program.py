def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------------")
    print("-       Journal App      -")
    print("--------------------------")


def run_event_loop():
    print("Was möchtest Du machen?")

    cmd = None
    journal_data = []

    while cmd != 'x':
        cmd = input("[L]iste der Einträge, [A]nfügen eines Eintrags, [X] Beenden? ").strip().lower()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Entschuldigung, das Kommando {} kenne ich nicht".format(cmd))
    print("Auf Wiedersehen")


def list_entries(data):
    print("Deine Journal Einträge:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("{}. {}".format(idx + 1,entry))


def add_entry(data):
    text = input("Gib den neuen Eintrag ein. <Enter> beendet Eingabe: ")
    data.append(text)


main()