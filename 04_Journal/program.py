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

    while cmd != 'x':
        cmd = input("[L]iste der Einträge, [A]nfügen eines Eintrags, [X] Beenden? ").strip().lower()
        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd != 'x':
            print("Entschuldigung, das Kommando {} kenne ich nicht".format(cmd))
    print("Auf Wiedersehen")


def list_entries():
    print("Liste der Einträge")


def add_entry():
    print("Neuen Eintrag anfügen")


main()