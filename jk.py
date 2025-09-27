   import math

Lista do przechowwywania historiiobliczeń
historia =[]
def menu_plaskie():
print("""
=== FIGURY PŁASKIE ===
a - Koło
b - Kwadrat
c - Prostokąt
d - Trójkąt (Heron)
e - Trójkąt równoboczny
f - Trapez
g - Równoległobok
h - Romb
    elif fig == "b":
        a = float(input("Bok a = "))
        print(f"Pole kwadratu = {round(a**2, 2)}")
        print(f"Obwód kwadratu = {round(4 * a, 2)}")
        print(f"Przekątna kwadratu = {round(a * math.sqrt(2), 2)}")

    elif fig == "c":
        a = float(input("Bok a = "))
        b = float(input("Bok b = "))
        print(f"Pole prostokąta = {round(a * b, 2)}")
        print(f"Obwód prostokąta = {round(2 * (a + b), 2)}")

    elif fig == "d":
        a = float(input("Bok a = "))
        b = float(input("Bok b = "))
        c = float(input("Bok c = "))
        obw = a + b + c
        if a + b > c and a + c > b and b + c > a:
            s = obw / 2
            pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Obwód trójkąta = {round(obw, 2)}")
            print(f"Pole trójkąta = {round(pole, 2)}")
        else:
            print("Z tych boków nie da się zbudować trójkąta.")

    elif fig == "e":
        a = float(input("Bok a = "))
        pole = (a**2 * math.sqrt(3)) / 4
        obw = 3 * a
        h = (a * math.sqrt(3)) / 2
        print(f"Pole trójkąta równobocznego = {round(pole, 2)}")
        print(f"Obwód trójkąta równobocznego = {round(obw, 2)}")
        print(f"Wysokość trójkąta równobocznego = {round(h, 2)}")

    elif fig == "f":
        a = float(input("Podstawa a = "))
        b = float(input("Podstawa b = "))
        h = float(input("Wysokość h = "))
        pole = ((a + b) * h) / 2
        c = float(input("Bok c = "))
        d = float(input("Bok d = "))
        obw = a + b + c + d
        print(f"Pole trapezu = {round(pole, 2)}")
        print(f"Obwód trapezu = {round(obw, 2)}")

    elif fig == "g":
        a = float(input("Bok a = "))
        b = float(input("Bok b = "))
        h = float(input("Wysokość h do boku a = "))
        print(f"Pole równoległoboku = {round(a * h, 2)}")
        print(f"Obwód równoległoboku = {round(2 * (a + b), 2)}")

    elif fig == "h":
        print("Jak chcesz policzyć pole rombu?")
        print("1 - P = a * h (bok i wysokość)")
        print("2 - P = (e * f) / 2 (przekątne)")
        wybor = input("1 / 2 ? ")
        if wybor == "1":
            a = float(input("Bok a = "))
            h = float(input("Wysokość h = "))
            print(f"Pole rombu = {round(a * h, 2)}")
            print(f"Obwód rombu = {round(4 * a, 2)}")
        elif wybor == "2":
            a = float(input("Bok a = "))
            e = float(input("Przekątna e = "))
            f = float(input("Przekątna f = "))
            print(f"Pole rombu = {round((e * f) / 2, 2)}")
            print(f"Obwód rombu = {round(4 * a, 2)}")
        else:
            print("Nie ma takiej opcji.")
    else:
        print("Nie ma takiej figury.")
except ValueError:
    print("Błąd: podaj prawidłową liczbę.")
input("Naciśnij Enter, aby wrócić do menu...")  # PAUZA
