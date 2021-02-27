# Text, který určí celý projekt
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Registrovaní uživatelé
# Slovník, jen verze jak bude vypadat slovník registrovaných uživatelů. registr = {"USER":"PASSWORD"}
# Skutečný registr zaregistrovaných uživatelů a jejich hesel
registr = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
# ODDĚLOVAČ pro budoucí potřeby
oddelovac = "-" * 40
# SYMBOL pro potřeby grafů
symbol = "*"
# Vstup uživatele
# Vložení uživatelského jména a hesla + oddělení sekce
username = input("Username: ")
password = input("Password: ")
print(oddelovac)

# Kontrola uživatelského jména a hesla po zadání vstupu od uživatele
if registr.get(username) == password:
    print(f"Welcome to the app, {username} \nWe have {len(TEXTS)} texts to be analyzed.")
    print(oddelovac)
else:
    print("We are sorry, but only registered users can log in. If you are registered, you have entered the wrong username or password.")
    exit()

# po přihlášení - oddělení sekce + kontrola
vyber = int(input("Enter a number btw. 1 and 3 to select: "))
print(oddelovac)
if vyber <= 0:
    print("Only 3 texts available. Only numbers 1, 2, 3 can be selected between them.")
    exit()
elif vyber > 3:
    print("Only 3 texts available. Only numbers 1, 2, 3 can be selected between them.")
    exit()
# ANALÝZA TEXTU
prevod = TEXTS[vyber-1]
jednotliva_slova = prevod.split()
# pocet slov a vyčištění od jiných znaků
for slovo in jednotliva_slova:
    ciste_slovo = slovo.strip(",.!_?+-*/")

vycistena_slova = [slovo.strip(",.!_?+-*/") for slovo in jednotliva_slova]
# pomocné
slovnik = {"začínající": 0, "velká": 0, "malá": 0, "cisla": 0}
soucet = []
pocet = {}
# Selekce slov na jednotlivé znaky a součet čísel
for znak in vycistena_slova:
    if znak.istitle():
        slovnik["začínající"] += 1
    elif znak.isalpha() and znak.isupper():
        slovnik["velká"] += 1
    elif znak.islower():
        slovnik["malá"] += 1
    elif znak.isdecimal():
        slovnik["cisla"] += 1
for i in vycistena_slova:
    if i.isnumeric():
        i = int(i)
        soucet.append(i)
# Vytištění jednotlivých hodnot
print("There are " + str(len(vycistena_slova)) + " words in the selected text.")
print("There are " + str(slovnik["začínající"]) + " titlecase words.")
print("There are " + str(slovnik["velká"]) + " uppercase words.")
print("There are " + str(slovnik["malá"]) + " lowercase words.")
print("There are " + str(slovnik["cisla"]) + " numeric strings.")
print("The sum of all the numbers ", sum(soucet), ".", sep="")
print(oddelovac)
# GRAF
print("LEN| OCCURENCES |NR.")
print(oddelovac)

i = 0
while i < len(vycistena_slova):
    l = len(vycistena_slova[i])
    pocet[l] = pocet.get(l, 0) + 1
    i = i + 1

delky = sorted(pocet)
i = 0
while i < len(delky):
    delka = delky[i]
    frekvence = pocet[delka]
    if len(str(delka)) == 1:
        str_len = ' ' + str(delka)
    else:
        str_len = str(delka)
    print(f"{str_len} | {symbol * frekvence} | {frekvence}")
    i = i + 1