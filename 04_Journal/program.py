import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------------")
    print("-       Journal App      -")
    print("--------------------------")


def run_event_loop():
    print("Was möchtest Du machen?")

    cmd = 'Empty'
    journal_name = 'default'

    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input("[L]iste der Einträge, [A]nfügen eines Eintrags, [X] Beenden? ").strip().lower()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Entschuldigung, das Kommando {} kenne ich nicht".format(cmd))
    print("Auf Wiedersehen")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Deine Journal Einträge:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("{}. {}".format(idx + 1,entry))


def add_entry(data):
    text = input("Gib den neuen Eintrag ein. <Enter> beendet Eingabe: ")
    journal.add_entry(text, data)

if __name__ == '__main__':
    main()