'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
quotes = []
names = []

for library in famous_quotes:
    for key, value in library.items():
        if key == "full_name":
            names.append(value)
        if key == "quote":
            quotes.append(value)

list_name = []
for name in names:
    list_name.append(name.split())

list_name_moved = []
for n in list_name:
    if len(n) == 2:
        list_name_moved.append(n[1] + ", " + n[0])
    if len(n) == 3:
        list_name_moved.append(n[2] + ", " + n[0] + " " + n[1])
print(list_name_moved)

for count in range(1, len(quotes)):
    print(f'"{quotes[count]}" - {list_name_moved[count]}')




