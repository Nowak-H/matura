import math

def get_float(prompt):
while True:
try:
value = float(input(prompt))
if value > 0:
return value
print("Podaj liczbę większą od 0.")
except ValueError:
print("To nie jest liczba!")

def figury_plaskie():
print("a - Koło\nb - Kwadrat\nc - Prostokąt\nd - Trójkąt\ne - Trapez\nf - Równoległobok\ng - Romb")
wybor = input("Wybierz figurę: ").lower()
if wybor == "a":
r = get_float("Promień: ")
print("Pole koła:", round(math.pi * r2, 2))
print("Obwód koła:", round(2 * math.pi * r, 2))
elif wybor == "b":
a = get_float("Bok: ")
print("Pole kwadratu:", round(a2, 2))
print("Obwód kwadratu:", round(4 * a, 2))
elif wybor == "c":
a = get_float("Bok a: ")
b = get_float("Bok b: ")
print("Pole prostokąta:", round(a * b, 2))
print("Obwód prostokąta:", round(2 * (a + b), 2))
elif wybor == "d":
a = get_float("Bok a: ")
h = get_float("Wysokość: ")
b = get_float("Bok b: ")
c = get_float("Bok c: ")
print("Pole trójkąta:", round((a * h) / 2, 2))
print("Obwód trójkąta:", round(a + b + c, 2))
elif wybor == "e":
a = get_float("Podstawa a: ")
b = get_float("Podstawa b: ")
h = get_float("Wysokość: ")
c = get_float("Bok c: ")
d = get_float("Bok d: ")
print("Pole trapezu:", round(((a + b) * h) / 2, 2))
print("Obwód trapezu:", round(a + b + c + d, 2))
elif wybor == "f":
a = get_float("Bok a: ")
b = get_float("Bok b: ")
h = get_float("Wysokość do a: ")
print("Pole równoległoboku:", round(a * h, 2))
print("Obwód równoległoboku:", round(2 * (a + b), 2))
elif wybor == "g":
a = get_float("Bok: ")
h = get_float("Wysokość: ")
d1 = get_float("Przekątna 1: ")
d2 = get_float("Przekątna 2: ")
print("Pole rombu:", round((d1 * d2) / 2, 2))
print("Obwód rombu:", round(4 * a, 2))

def bryly():
print("a - Sześcian\nb - Prostopadłościan\nc - Walec\nd - Kula\ne - Stożek\nf - Graniastosłup\ng - Ostrosłup")
wybor = input("Wybierz bryłę: ").lower()
if wybor == "a":
a = get_float("Bok: ")
print("Pole powierzchni sześcianu:", round(6 * a2, 2))
print("Objętość sześcianu:", round(a3, 2))
elif wybor == "b":
a = get_float("Bok a: ")
b = get_float("Bok b: ")
c = get_float("Bok c: ")
print("Pole powierzchni prostopadłościanu:", round(2 * (ab + ac + b*c), 2))
print("Objętość prostopadłościanu:", round(a * b * c, 2))
elif wybor == "c":
r = get_float("Promień podstawy: ")
h = get_float("Wysokość: ")
print("Pole powierzchni walca:", round(2 * math.pi * r * (r + h), 2))
print("Objętość walca:", round(math.pi * r2 * h, 2))
elif wybor == "d":
r = get_float("Promień: ")
print("Pole powierzchni kuli:", round(4 * math.pi * r2, 2))
print("Objętość kuli:", round((4/3) * math.pi * r3, 2))
elif wybor == "e":
r = get_float("Promień podstawy: ")
h = get_float("Wysokość: ")
l = math.sqrt(r2 + h2)
print("Pole powierzchni stożka:", round(math.pi * r * (r + l), 2))
print("Objętość stożka:", round((1/3) * math.pi * r2 * h, 2))
elif wybor == "f":
pp = get_float("Pole podstawy: ")
obw = get_float("Obwód podstawy: ")
h = get_float("Wysokość: ")
print("Pole powierzchni graniastosłupa:", round(2 * pp + obw * h, 2))
print("Objętość graniastosłupa:", round(pp * h, 2))
elif wybor == "g":
pp = get_float("Pole podstawy: ")
obw = get_float("Obwód podstawy: ")
l = get_float("Tworząca: ")
h = get_float("Wysokość: ")
print("Pole powierzchni ostrosłupa:", round(pp + (obw * l) / 2, 2))
print("Objętość ostrosłupa:", round((1/3) * pp * h, 2))

def main():
print("\nKALKULATOR GEOMETRII")
print("a - Płaskie\nb - Bryły")
wybor = input("Wybierz a - płaskie, b - bryły: ").lower()
if wybor == "a":
figury_plaskie()
elif wybor == "b":
bryly()
else:
print("Nieprawidłowa opcja.")

if name == "main":
main()
