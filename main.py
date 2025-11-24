import math
PI = math.pi

#-------------------------------------

def pp_szescianu(a:float)->float:
    return 6*a**2

def obw_szescianu(a:float)->float:
    return a**3

def wzory_na_szescian()->None:
    while True:
        print("a-pp_szescianu \n b-obw_szescianu \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_szescianu = {pp_szescianu(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_szescianu = {obw_szescianu(a)}")
        elif inp == "e":
            break

#-------------------------------------

def pp_prostopadłoscianu(a:float,b:float,c:float)->float:
    return 2*a*b+2*a*c+2*b*c

def obw_prostopadłoscianu(a:float,b:float,c:float)->float:
    return a*b*c

def wzory_na_prostopadłoscianu()->None:
    while True:
        print("a-pp_prostopadłoscianu \n b-obw_prostopadłoscianu \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_prostopadłoscianu = {pp_prostopadłoscianu(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_prostopadłoscianu = {obw_prostopadłoscianu(a)}")
        elif inp == "e":
            break

#-------------------------------------

def pp_graniatosłupa(Pp:float,Pb:float)->float:
    return 2*Pp + Pb

def obw_graniatosłupa(Pp:float,h:float)->float:
    return Pp + h

def wzory_na_graniatosłupa()->None:
    while True:
        print("a-pp_graniatosłupa \n b-obw_graniatosłupa \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_graniatosłupa = {pp_graniatosłupa(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_graniatosłupa = {obw_graniatosłupa(a)}")
        elif inp == "e":
            break

#-------------------------------------

def pp_ostrosłupa(Pp:float,Pb:float)->float:
    return Pp + Pb

def obw_ostrosłupa(Pp:float,h:float)->float:
    return 1/3*Pp * h

def wzory_na_ostrosłupa()->None:
    while True:
        print("a-pp_ostrosłupa \n b-obw_ostrosłupa \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_ostrosłupa = {pp_ostrosłupa(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_ostrosłupa = {obw_ostrosłupa(a)}")
        elif inp == "e":
            break
    
#-------------------------------------

def pp_walca(r:float,h:float)->float:
    return 2*PI*r**2 + 2*PI*r*h

def obw_walca(r:float,h:float)->float:
    return PI*r**2 * h

def wzory_na_walca()->None:
    while True:
        print("a-pp_walca \n b-obw_walca \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_walca = {pp_walca(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_walca = {obw_walca(a)}")
        elif inp == "e":
            break

#-------------------------------------

def pp_stozek(r:float,l:float)->float:
    return PI*r**2 + PI*r*l

def obw_stozek(r:float,h:float)->float:
    return 1/3*PI*r**2 * h

def wzory_na_stozek()->None:
    while True:
        print("a-pp_stozek \n b-obw_stozek \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_stozek = {pp_stozek(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_stozek = {obw_stozek(a)}")
        elif inp == "e":
            break
    
#-------------------------------------

def pp_kuli(r:float)->float:
    return 4*PI*r**2

def obw_kuli(r:float)->float:
    return 4/3*PI*r**3

def wzory_na_kuli()->None:
    while True:
        print("a-pp_kuli \n b-obw_kuli \n e-exit")
        inp:str = input(": ")
        if inp == "a":
            a:float = float(input("a: "))
            print(f"pp_kuli = {pp_kuli(a)}")
        elif inp == "b":
            a:float = float(input("a: "))
            print(f"obw_kuli = {obw_kuli(a)}")
        elif inp == "e":
            break
