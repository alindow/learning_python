import datetime

def print_header():
    print("-----------------------------")
    print("          Geburtstag")
    print("-----------------------------")
    print

def get_birthday_from_user():
    print("Wann bist Du geboren?")
    year = input("Geburtsjahr[jjjj]? ")
    month = input("Monat[mm]? ")
    day = input("Tag[tt]? ")
    return datetime.date(int(year), int(month), int(day))

def compute_days_between_days(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days

def compute_years(birthdate, target_date):
    return birthdate.year - target_date.year


def print_birthday_information(days, years):
    if days < 0:
        if(days < -1):
            print('Dein {}. Geburtstag war vor {} Tagen'.format(-years, -days))
        else:
            print('Dein {}. Geburtstag war gestern'.format(-years))
    elif days > 0:
        if(days > 1):
            print('Dein {}. Geburtstag ist in {} Tagen'.format(-years, days))
        else:
            print('Dein {}. Geburtstag ist morgen'.format(-years))
    else:
        print("Happy Birthday!!! Heute ist Dein {}. Geburtstag".format(-years))

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_days(bday, today)
    years = compute_years(bday, today)
    print_birthday_information(number_of_days, years)


main()