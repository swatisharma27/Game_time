import json
import datetime
from collections import Counter

birthdays = {}
fh_r = open('birthdays.json', 'r')
birthdays = json.load(fh_r)

def save_file():
    fh_w = open('birthdays.json', 'w')
    json.dump(birthdays, fh_w)

def add_entry():
    name = input("Add a name to the dictionary: ").title()
    dob = date_format()
    birthdays[name] = dob
    print("{} was added in the birthday list with date {}.".format(name, birthdays[name]))
    save_file()

def edit_entry():
    list_names()
    name = get()
    print("\nNow to change the birth date:-")
    date_of_birth = date_format()
    birthdays[name] = date_of_birth
    print("{} was edited in the birthday list with date : {}.".format(name, date_of_birth))
    save_file()

def date_format():
    inputDate = input("Enter the birth-date in format 'dd/mm/yyyy': ")
    day,month,year = inputDate.split('/')
    isValidDate = True
    try:
        datetime.datetime(int(year),int(month),int(day))
        if (len(inputDate.split('/')[2])) == 4:
            return inputDate
        else:
            print("Invalid Entry")
            return date_format()
    except ValueError:
        isValidDate = False
        print("Invalid Entry")
        return date_format()
    # Return the function, when calling it recursively

def fetch():
    list_names()
    return get()

def fetch_name():
    label = input("\nWho's birthday do you want to look up? ").title()
    return label

def get():
    name = fetch_name()
    if name in birthdays:
        print(name + "'s birthday is " + birthdays[name] + ".")
        return name
    else:
        few_ltrs = name[:len(name)]
        print("Wrong entry, maybe try again!")
        fh_r = open('birthdays.json', 'r')
        count = 1
        suggest = dict()
        for elem in birthdays:
            if elem.startswith(few_ltrs):
                print(str(count) + '-' + elem)
                suggest[count] = elem
                count += 1
                continue

        for keys in suggest.items():
            st5 = int(input("Select the number: "))
            if st5 in suggest.keys():
                print(suggest[st5] + "'s birthday is on " + birthdays[suggest[st5]] + ".")
                return suggest[st5]
            else:
                print("Wrong Entry!")
                return get()

        for elem in birthdays:
            if not elem.startswith(few_ltrs):
                return get()

def remove_entry():
    list_names()
    st4 = input("Which entry do you want to delete?: ").title()
    del birthdays[st4]
    print("{} was deleted from the Birthday Calendar.".format(st4))
    save_file()

def list_names():
    count = 1
    print("The list of names are:\n")
    for name in birthdays:
        print(count, ')', name)
        count += 1

def list_all():
    count = 1
    print("The list of names are:\n")
    for name in birthdays:
        print(count, ')', name, ':', birthdays[name])
        count += 1


def ask():
    st1 = input("\nDo you want to access 'Birthday Calendar' again? (y/n): ").lower()
    if st1 == 'y':
        print('\nPlease to help you!')
    elif st1 == 'n':
        print("\nThank you for using the 'Birthday Calendar'!")
        raise SystemExit(0)
    else:
        print("Wrong Entry! Try this!")
        return ask()

def request():
    print("Access Birthday Calendar")
    print(''' 
    1 - Add
    2 - Fetch
    3 - Edit
    4 - Remove
    5 - List
    ''')

    req = input("Select from 1 to 5: ").title()
    print('\n')
    return req

if __name__ == "__main__":
    print("Welcome to the Birthday Calendar!\n")
    while True:
        inp = request()
        if inp == 'Add' or inp == 'A' or inp == '1':
            add_entry()
            ask()
        elif inp == 'Fetch' or inp == 'F' or inp == '2':
            fetch()
            ask()
        elif inp == 'Edit' or inp == 'E' or inp == '3':
            edit_entry()
            ask()
        elif inp == 'Remove' or inp == 'R' or inp == '4':
            remove_entry()
            ask()
        elif inp == 'List' or inp == 'L' or inp == '5':
            list_all()
            ask()
        else:
            print("Wrong entry, try again!")
            continue
