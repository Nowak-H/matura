import math

print("Witaj w prostym kalkulatorze geometrii!")
print("Co chcesz policzyć?")
print("1. Figury płaskie")
print("2. Bryły")
wybor_glowny = input("Wybierz 1 lub 2: ")

if wybor_glowny == "1":
    print("Wybierz figurę:")
    print("1. Kwadrat")
    print("2. Prostokąt")
    print("3. Trójkąt dowolny")
    print("4. Trójkąt równoramienny")
    print("5. Romb")
    print("6. Koło")
    wybor_figura = input("Podaj numer figury: ")

    if wybor_figura == "1":
        a = float(input("Podaj bok kwadratu: "))
        pole = a * a
        obwod = 4 * a
        print("Pole kwadratu:", pole)
        print("Obwód kwadratu:", obwod)

    elif wybor_figura == "2":
        a = float(input("Podaj bok a prostokąta: "))
        b = float(input("Podaj bok b prostokąta: "))
        pole = a * b
        obwod = 2 * (a + b)
        print("Pole prostokąta:", pole)
        print("Obwód prostokąta:", obwod)

    elif wybor_figura == "3":
        a = float(input("Podaj bok a trójkąta: "))
        b = float(input("Podaj bok b trójkąta: "))
        c = float(input("Podaj bok c trójkąta: "))
        h = float(input("Podaj wysokość do boku a: "))
        pole = (a * h) / 2
        obwod = a + b + c
        # Wzór Herona
        p = (a + b + c) / 2
        pole_heron = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole trójkąta (a*h/2):", pole)
        print("Pole trójkąta (Herona):", pole_heron)
        print("Obwód trójkąta:", obwod)

    elif wybor_figura == "4":
        a = float(input("Podaj długość ramienia (a): "))
        b = float(input("Podaj długość podstawy (b): "))
        obwod = 2 * a + b
        h = math.sqrt(a**2 - (b / 2)**2)
        pole = (b * h) / 2
        print("Wysokość opuszczona na podstawę:", h)
        print("Pole trójkąta równoramiennego:", pole)
        print("Obwód trójkąta równoramiennego:", obwod)

    elif wybor_figura == "5":
        a = float(input("Podaj bok rombu: "))
        h = float(input("Podaj wysokość rombu: "))
        d1 = float(input("Podaj przekątną 1 rombu: "))
        d2 = float(input("Podaj przekątną 2 rombu: "))
        pole1 = a * h
        pole2 = (d1 * d2) / 2
        obwod = 4 * a
        print("Pole rombu (bok i wysokość):", pole1)
        print("Pole rombu (przekątne):", pole2)
        print("Obwód rombu:", obwod)

    elif wybor_figura == "6":
        r = float(input("Podaj promień koła: "))
        pole = math.pi * r * r
        obwod = 2 * math.pi * r
        print("Pole koła:", pole)
        print("Obwód koła:", obwod)

    else:
        print("Nie ma takiej figury w tym kalkulatorze.")

elif wybor_glowny == "2":
    print("Wybierz bryłę:")
    print("1. Sześcian")
    print("2. Prostopadłościan")
    print("3. Walec")
    print("4. Kula")
    print("5. Stożek")
    print("6. Graniastosłup")
    print("7. Ostrosłup")
    wybor_bryla = input("Podaj numer bryły: ")

    if wybor_bryla == "1":
        a = float(input("Podaj bok sześcianu: "))
        pole = 6 * a * a
        objetosc = a * a * a
        print("Pole powierzchni sześcianu:", pole)
        print("Objętość sześcianu:", objetosc)

    elif wybor_bryla == "2":
        a = float(input("Podaj bok a prostopadłościanu: "))
        b = float(input("Podaj bok b prostopadłościanu: "))
        c = float(input("Podaj bok c prostopadłościanu: "))
        pole = 2 * (a * b + a * c + b * c)
        objetosc = a * b * c
        print("Pole powierzchni prostopadłościanu:", pole)
        print("Objętość prostopadłościanu:", objetosc)

    elif wybor_bryla == "3":
        r = float(input("Podaj promień podstawy walca: "))
        h = float(input("Podaj wysokość walca: "))
        pole = 2 * math.pi * r * (r + h)
        objetosc = math.pi * r * r * h
        print("Pole powierzchni walca:", pole)
        print("Objętość walca:", objetosc)

    elif wybor_bryla == "4":
        r = float(input("Podaj promień kuli: "))
        pole = 4 * math.pi * r * r
        objetosc = (4/3) * math.pi * r * r * r
        print("Pole powierzchni kuli:", pole)
        print("Objętość kuli:", objetosc)

    elif wybor_bryla == "5":
        r = float(input("Podaj promień podstawy stożka: "))
        h = float(input("Podaj wysokość stożka: "))
        l = math.sqrt(r*r + h*h)
        pole = math.pi * r * (r + l)
        objetosc = (1/3) * math.pi * r * r * h
        print("Pole powierzchni stożka:", pole)
        print("Objętość stożka:", objetosc)

    elif wybor_bryla == "6":
        pp = float(input("Podaj pole podstawy graniastosłupa: "))
        obw = float(input("Podaj obwód podstawy graniastosłupa: "))
        h = float(input("Podaj wysokość graniastosłupa: "))
        pole = 2 * pp + obw * h
        objetosc = pp * h
        print("Pole powierzchni graniastosłupa:", pole)
        print("Objętość graniastosłupa:", objetosc)

    elif wybor_bryla == "7":
        pp = float(input("Podaj pole podstawy ostrosłupa: "))
        obw = float(input("Podaj obwód podstawy ostrosłupa: "))
        l = float(input("Podaj długość tworzącej ostrosłupa: "))
        h = float(input("Podaj wysokość ostrosłupa: "))
        pole = pp + (obw * l) / 2
        objetosc = (1/3) * pp * h
        print("Pole powierzchni ostrosłupa:", pole)
        print("Objętość ostrosłupa:", objetosc)

    else:
        print("Nie ma takiej bryły w tym kalkulatorze.")

else:
    print("Nie wybrano poprawnej opcji.")
