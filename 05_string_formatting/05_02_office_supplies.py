'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

list_items = []
names = []

for library in office:
    for key, value in library.items():
        if key == "full_name":
            names.append(value)
        if key == "item":
            list_items.append(value)

list_name = []

for name in names:
    list_name.append(name.split())

list_name_moved = []

for n in list_name:
    if len(n) == 2:
        list_name_moved.append(n[1].upper() + ", " + n[0])
    if len(n) == 3:
        list_name_moved.append(n[2] + ", " + n[0] + " " + n[1])


for count in range(0, len(list_items)):
    print(f'{(list_name_moved[count])}{(24-(len(list_name_moved[count])))*(" "):>} {(list_items[count].capitalize())}')

