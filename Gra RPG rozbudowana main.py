import sys
import time
import random
import os

# -----------------------------------------------------------------------------
# KONFIGURACJA I NARZĘDZIA
# -----------------------------------------------------------------------------

def wyczysc_ekran():
    """Czyści terminal dla lepszej czytelności (działa na Windows i Linux/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pisz(tekst, predkosc=0.03):
    """
    Wyświetla tekst litera po literze (efekt maszyny do pisania).
    Dzięki temu gra wydaje się bardziej klimatyczna.
    """
    for litera in tekst:
        sys.stdout.write(litera)
        sys.stdout.flush()
        time.sleep(predkosc)
    print() # Nowa linia na końcu

def czekaj(sekundy):
    """Wstrzymuje działanie programu na chwilę."""
    time.sleep(sekundy)

def linia():
    print("-" * 60)

# ASCII ART - Grafiki tekstowe
ART_TYTUL = r"""
  _____ _                 _       _   _      
 / ____| |               | |     | | (_)     
| |    | | ___  _ __   __| | __ _| |_ _ __ _ 
| |    | |/ _ \| '_ \ / _` |/ _` | __| |/ _` |
| |____| | (_) | | | | (_| | (_| | |_| | (_| |
 \_____|_|\___/|_| |_|\__,_|\__,_|\__|_|\__,_|
                                              
      --- ECHO ZAPOMNIANEGO KRÓLESTWA ---
"""

ART_MIECZ = r"""
      /| ________________
O|===|* >________________>
      \|
"""

ART_DRZWI = r"""
  __________
 |  __  __  |
 | |  ||  | |
 | |  ||  | |
 | |__||__| |
 |  __  __  |
 | |  ||  | |
 | |  ||  | |
 | |__||__| |
 |__________|
"""

ART_POTWOR = r"""
   (    )
  ((((()))))
  |o_  _o|
  ( \  / )
   \ -- /
   /    \
"""

# Zmienne globalne gracza (bardzo proste statystyki)
gracz = {
    "imie": "Nieznajomy",
    "hp": 100,
    "max_hp": 100,
    "mana": 50,
    "ekwipunek": ["Zardzewiały Sztylet", "Mikstura Zdrowia"]
}

# -----------------------------------------------------------------------------
# LOGIKA GRY - ROZDZIAŁY
# -----------------------------------------------------------------------------

def intro():
    wyczysc_ekran()
    print(ART_TYTUL)
    czekaj(1)
    pisz("\nWitaj wędrowcze w świecie Cieni.")
    pisz("Tutaj twoje wybory kształtują chwilę, ale przeznaczenie jest już zapisane.")
    linia()
    
    # Pobieranie imienia
    pisz("Zanim zaczniemy... jak cię zwą w twoich stronach?", 0.05)
    imie = input("\n[WPISZ IMIĘ]: ")
    if imie.strip() == "":
        imie = "Bezimienny"
    
    gracz["imie"] = imie
    
    pisz(f"\nA zatem, {gracz['imie']}... posłuchaj historii upadku.", 0.04)
    czekaj(1)
    
    # Lore dump - Wprowadzenie fabularne
    wyczysc_ekran()
    pisz("ROK 402 ERY POPIOŁÓW", 0.1)
    linia()
    pisz("Królestwo Aethelgard upadło w jedną noc.")
    pisz("Mówi się, że król zawarł pakt z istotami zza Zasłony.")
    pisz("Chciał nieśmiertelności. Otrzymał wieczne cierpienie.")
    pisz("Twierdza, w której stoisz, jest teraz grobowcem.")
    pisz("Ale ty szukasz czegoś więcej niż skarbów. Szukasz prawdy.")
    czekaj(2)
    
    pisz("\nStoisz przed wielkimi, dębowymi wrotami twierdzy.")
    pisz("Deszcz zacina, a pioruny rozświetlają niebo.")
    linia()
    input("\n[Naciśnij ENTER, aby wejść do twierdzy...]")
    brama_wejsciowa()

def brama_wejsciowa():
    wyczysc_ekran()
    print(ART_DRZWI)
    pisz("Wrota są ogromne. Wydają się być zamknięte na głucho.")
    pisz("Na drewnie wyryto starożytne runy ostrzegawcze.")
    
    pisz("\nCo robisz?")
    print("1. Próbuję wyważyć drzwi siłą.")
    print("2. Szukam mechanizmu lub klucza w krzakach obok.")
    print("3. Pukam kulturalnie.")
    
    wybor = input("\n> ")
    
    linia()
    # Iluzja wyboru: Każda opcja prowadzi do tego samego efektu
    if wybor == "1":
        pisz(f"{gracz['imie']} napiera ramieniem na drzwi!")
        pisz("Czujesz, jak stare drewno trzeszczy...")
        pisz("Nagle zawiasy puszczają, ale nie z powodu twojej siły.")
        pisz("One po prostu przerdzewiały wieki temu.")
    elif wybor == "2":
        pisz("Przeszukujesz zarośla...")
        pisz("Znajdujesz starą czaszkę i... dźwignię ukrytą w murze.")
        pisz("Pociągasz za nią. Mechanizm zgrzyta przeraźliwie.")
    elif wybor == "3":
        pisz("Pukasz...")
        czekaj(1)
        pisz("Dźwięk niesie się echem, jakbyś uderzał w bęben.")
        pisz("Ku twojemu zdziwieniu, wrota otwierają się same.")
        pisz("Ktoś – lub coś – na ciebie czekało.")
    else:
        pisz("Stoisz bezczynnie, aż wiatr sam otwiera wrota.")
    
    pisz("\nDroga stoi otworem. Wchodzisz do środka.")
    czekaj(2)
    korytarz_glowny()

def korytarz_glowny():
    wyczysc_ekran()
    pisz("Jesteś w Wielkim Holu.")
    pisz("Powietrze jest zatęchłe, pachnie starym papierem i krwią.")
    pisz("Na ścianach wiszą portrety dawnych władców, teraz podarte.")
    
    pisz("\nWidzisz dwie ścieżki:")
    pisz("Po LEWEJ: Ciemne schody prowadzące do lochów.")
    pisz("Po PRAWEJ: Oświetlony bladym światłem korytarz do biblioteki.")
    
    pisz("\nGdzie idziesz?")
    print("1. Lewo (Lochy)")
    print("2. Prawo (Biblioteka)")
    
    wybor = input("\n> ")
    
    linia()
    # Decyzja która zmienia tylko opis przejścia, ale nie cel
    if wybor == "1":
        pisz("Schodzisz w mrok lochów...")
        pisz("Słyszysz kapanie wody i ciche szepty.")
        pisz("Potykasz się o czyjeś kości.")
        pisz("-10 HP za niezdarność!")
        gracz["hp"] -= 10
        pisz(f"Twoje HP: {gracz['hp']}/{gracz['max_hp']}")
        pisz("\nNagle podłoga się zapada! Spadasz...")
    else:
        pisz("Idziesz w stronę biblioteki.")
        pisz("Mijasz regały pełne gnijących ksiąg.")
        pisz("Nagle czujesz zapach siarki.")
        pisz("Podłoga pod tobą jest krucha...")
        pisz("\nDeski pękają! Spadasz...")
    
    czekaj(2)
    pisz("\n...lądujesz na stosie siana w podziemiach.")
    pisz("Niezależnie od drogi, przeznaczenie chciało cię tu sprowadzić.")
    sala_walki()

def system_walki(nazwa_wroga, hp_wroga):
    """
    Prosty, turowy system walki.
    Zawsze wygrywasz (chyba że się poddasz), bo to gra nastawiona na historię.
    """
    print(f"\n!!! WALKA ROZPOCZĘTA: {nazwa_wroga} !!!")
    print(ART_MIECZ)
    
    runda = 1
    
    while hp_wroga > 0 and gracz["hp"] > 0:
        print(f"\n--- RUNDA {runda} ---")
        print(f"Wróg: {nazwa_wroga} | HP: {hp_wroga}")
        print(f"Ty: {gracz['imie']} | HP: {gracz['hp']}")
        
        print("Akcje:")
        print("1. Atakuj mieczem")
        print("2. Użyj magii (Kula Ognia)")
        print("3. Próbuj rozmawiać")
        
        akcja = input("> ")
        
        # Tura Gracza
        szkody = 0
        if akcja == "1":
            szkody = random.randint(15, 25)
            pisz(f"Zadajesz cięcie! Wróg traci {szkody} HP.")
        elif akcja == "2":
            szkody = random.randint(20, 40)
            pisz(f"Strzelasz ogniem! Wróg traci {szkody} HP.")
            pisz("Czujesz, jak mana przepływa przez twoje ciało.")
        elif akcja == "3":
            pisz(f"Próbujesz przemówić do {nazwa_wroga}...")
            pisz("Wróg nie słucha. Ryk jest jedyną odpowiedzią.")
            szkody = 0
        else:
            pisz("Wahałeś się... tracisz turę.")
        
        hp_wroga -= szkody
        
        # Sprawdzenie czy wróg padł
        if hp_wroga <= 0:
            break
            
        # Tura Wroga
        pisz(f"\n{nazwa_wroga} kontratakuje!")
        obrazenia_wroga = random.randint(5, 15)
        gracz["hp"] -= obrazenia_wroga
        pisz(f"Otrzymujesz {obrazenia_wroga} obrażeń!")
        
        if gracz["hp"] <= 0:
            pisz("\nPadłeś na ziemię... Światło gaśnie...")
            pisz("Ale czekaj... to nie koniec.")
            pisz("Tajemnicza siła przywraca cię do życia z 1 HP.")
            gracz["hp"] = 1
        
        runda += 1
        czekaj(1)

    pisz(f"\n{nazwa_wroga} pada martwy na ziemię.")
    pisz("Wycierasz broń. Zwycięstwo.")
    linia()
    input("[Dalej...]")

def sala_walki():
    wyczysc_ekran()
    print(ART_POTWOR)
    pisz("Wstajesz ze stogu siana.")
    pisz("Pomieszczenie jest okrągłe, oświetlone pochodniami.")
    pisz("Na środku stoi Strażnik Cieni.")
    pisz("To zdeformowana istota, niegdyś człowiek, teraz bestia.")
    
    pisz("\nStrażnik: 'Nie przejdziesz... Pan wzywa tylko godnych.'")
    
    pisz("\nCo odpowiadasz?")
    print("1. 'Zejdź mi z drogi, potworze!'")
    print("2. 'Służę twojemu Panu, przepuść mnie.' (Kłamstwo)")
    
    wybor = input("> ")
    if wybor == "2":
        pisz("Strażnik mruży oczy...")
        pisz("'Kłamstwo... czuję bicie twojego serca. Jest sercem żywego.'")
    
    pisz("Bestia rzuca się do ataku!")
    
    # Wywołanie walki
    system_walki("Strażnik Cieni", 80)
    
    pisz("Po walce znajdujesz przy strażniku klucz.")
    pisz("Otwierasz nim jedyne wyjście z sali.")
    sala_tronowa()

def zagadka_sfinksa(bledy=0):
    """Prosta minigra logiczna."""
    pisz("\nPrzed wejściem do Sali Tronowej stoi posąg Sfinksa.")
    pisz("Kamienne usta otwierają się:")
    pisz("'Co rano chodzi na czterech nogach, w południe na dwóch, a wieczorem na trzech?'")
    
    odpowiedz = input("Twoja odpowiedź: ").lower()
    
    if "człowiek" in odpowiedz or "ludzie" in odpowiedz:
        pisz("'Mądra odpowiedź. Możesz wejść.'")
        return
    else:
        pisz("'Błąd...'")
        pisz("Posąg patrzy na ciebie z politowaniem.")
        if bledy < 2:
            pisz("'Dam ci kolejną szansę, śmiertelniku.'")
            zagadka_sfinksa(bledy + 1)
        else:
            pisz("'Jesteś beznadziejny. Ale drzwi są otwarte, wejdź i zgiń.'")
            # Gra puszcza gracza dalej mimo błędu (iluzja wyzwania)

def sala_tronowa():
    wyczysc_ekran()
    zagadka_sfinksa()
    
    wyczysc_ekran()
    pisz("Wkraczasz do Sali Tronowej.")
    pisz("Okna są wybite, wiatr hula po posadzce.")
    pisz("Na końcu sali, na tronie z czarnego obsydianu, siedzi ON.")
    
    pisz("\nUPADŁY KRÓL AETHELGARDU.")
    pisz("Nie wygląda na martwego. Wygląda na znudzonego.")
    
    pisz("\nKról: 'Kolejny bohater? Czy może złodziej?'")
    pisz("\nMasz szansę zadać mu jedno pytanie przed końcem.")
    print("1. Dlaczego sprowadziłeś klątwę na to miejsce?")
    print("2. Gdzie jest skarb?")
    print("3. Czy żałujesz?")
    
    wybor = input("> ")
    
    linia()
    # Lore dump zależny od pytania, ale prowadzący do tego samego
    if wybor == "1":
        pisz("Król śmieje się sucho.")
        pisz("'Chciałem uratować mój lud przed chorobą. Cena była jednak... wysoka.'")
        pisz("'Cienie obiecały lek. Dały go. Ale zabrały duszę.'")
    elif wybor == "2":
        pisz("Król wskazuje na stertę złota w rogu.")
        pisz("'Bierz. To tylko metal. Nie uchroni cię przed czasem.'")
        pisz("'Prawdziwym skarbem jest śmierć, której nie mogę zaznać.'")
    else:
        pisz("Król milczy przez długą chwilę.")
        pisz("'Żal to uczucie dla żywych. Ja czuję tylko pustkę.'")
    
    pisz("\nKról wstaje z tronu.")
    pisz("'Dość rozmów. Czas zakończyć ten cykl.'")
    
    final_decision()

def final_decision():
    linia()
    pisz("Król wyciąga rękę. W jego dłoni formuje się kula czarnej energii.")
    pisz("To moment ostatecznej decyzji, która zdefiniuje twoją legendę.")
    
    print("\nWYBIERZ SWÓJ LOS:")
    print("1. Walcz z Królem (Epicka śmierć)")
    print("2. Uklęknij i dołącz do niego (Wieczna służba)")
    print("3. Uciekaj (Tchórzostwo)")
    
    wybor = input("> ")
    
    wyczysc_ekran()
    linia()
    
    if wybor == "1":
        pisz("Dobywasz broni i rzucasz się na Króla z okrzykiem bojowym!")
        pisz("Twoje ostrze trafia w jego zbroję.")
        pisz("Błysk światła zalewa salę.")
        pisz("Czujesz ciepło... a potem nicość.")
        ending_text("Zginąłeś jako bohater. Twoje imię będzie zapomniane, ale czyn był wielki.")
        
    elif wybor == "2":
        pisz("Rzucasz broń i klękasz.")
        pisz("Król uśmiecha się smutno.")
        pisz("'A więc niech tak będzie. Kolejny strażnik do kolekcji.'")
        pisz("Twoja skóra twardnieje, serce zwalnia.")
        ending_text("Zostałeś nowym Strażnikiem Cieni. Czekasz na kolejnego śmiałka.")
        
    elif wybor == "3":
        pisz("Odwracasz się i biegniesz.")
        pisz("Słyszysz za sobą śmiech Króla.")
        pisz("Wypadasz przez wrota twierdzy w deszcz.")
        pisz("Nigdy nie oglądasz się za siebie.")
        ending_text("Przeżyłeś. Ale koszmary będą cię dręczyć do końca dni.")
        
    else:
        pisz("Stoisz sparaliżowany strachem.")
        pisz("Król pstryka palcami.")
        ending_text("Zniknąłeś. Po prostu przestałeś istnieć.")

def ending_text(konkluzja):
    print("\n")
    print("   KONIEC GRY   ")
    linia()
    pisz(konkluzja)
    pisz("\nDziękuję za zagranie w tę prostą przygodę.")
    pisz(f"Statystyki końcowe {gracz['imie']}:")
    print(f"HP: {gracz['hp']}")
    print(f"Ekwipunek: {', '.join(gracz['ekwipunek'])}")
    linia()
    input("[Naciśnij ENTER, aby wyjść]")
    sys.exit()

# -----------------------------------------------------------------------------
# GŁÓWNA PĘTLA PROGRAMU
# -----------------------------------------------------------------------------

def main():
    # Pętla gry - pozwala zagrać ponownie (teoretycznie, choć tu kod jest liniowy)
    try:
        intro()
    except KeyboardInterrupt:
        print("\n\nGra przerwana przez użytkownika. Do widzenia!")
        sys.exit()

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
# KOMENTARZ DLA PROGRAMISTY (Lore kodu)
# -----------------------------------------------------------------------------
# Ten kod został napisany w taki sposób, aby był łatwy do analizy.
# Główne techniki użyte tutaj:
# 1. Funkcje (def) - każda lokacja to osobna funkcja, co ułatwia zarządzanie.
# 2. Słownik (dict) - 'gracz' przechowuje zmienne, łatwo dodać nowe statystyki.
# 3. Import time - użyty do budowania napięcia (funkcja czekaj i pisz).
# 4. Instrukcje warunkowe - mimo że wybory prowadzą do tego samego, 
#    kod musi sprawdzić, co wpisał użytkownik, by wyświetlić odpowiedni tekst.
#
# Jak rozwinąć ten kod?
# - Dodać system ekwipunku (listę przedmiotów, które faktycznie coś robią).
# - Dodać losowe zdarzenia (rzut kostką).
# - Zapisać stan gry do pliku tekstowego.
# -----------------------------------------------------------------------------
