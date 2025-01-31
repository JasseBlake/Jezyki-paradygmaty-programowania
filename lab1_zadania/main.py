# Zadanie 1. Problem Podziału Paczek (Prograowanie Proceduralne)

# Mamy listę paczek o różnych wagach oraz maksymalną wagę, jaką może unieść kurier w jednym kursie.
# Twoim zadaniem jest podzielić paczki na jak najmniejszą liczbę kursów, aby każda waga nie przekraczała
# maksymalnej dozwolonej wagi. Program powinien korzystać z algorytmu zachłannego do optymalizacji
# podziału paczek.
# Wymagania:
# • Napisz funkcję, która przyjmuje listę wag paczek i maksymalną wagę.
# • Użyj pętli for i instrukcji warunkowych if, else do iteracyjnego podziału paczek.
# • Program powinien zwracać minimalną liczbę kursów oraz listę paczek w każdym kursie.


# def Zadanie1(ListaPaczek,MaksymalnaWaga):
#
#     ListaPaczek.sort(reverse=True)
#     Kursy = []
#
#     while ListaPaczek:
#
#         WagaKursu = MaksymalnaWaga
#         aktualnyKurs = []
#
#         for paczka in ListaPaczek[:]:
#
#             if paczka <= WagaKursu:
#                 aktualnyKurs.append(paczka)
#                 WagaKursu-=paczka
#                 ListaPaczek.remove(paczka)
#         Kursy.append(aktualnyKurs)
#     print(f"Kursy : {Kursy}")
#     print(f"Liczba kursy : {len(Kursy)}")
#
#
# Zadanie1([1,1,1],1)

###############################################################################################################

# Zadanie 2. Wyznaczanie Najkrótszej Ścieżki (Programowanie Funkcyjne)

# Stwórz program obliczający najkrótszą ścieżkę w grafie nieważonym przy użyciu algorytmu BFS
# (Breadth-First Search).
# Implementacja powinna być zrealizowana przy użyciu programowania
# funkcyjnego z naciskiem na niemutowalne struktury danych, funkcje lambda, i mapowanie.

# Wymagania:
# • Napisz funkcję BFS przy użyciu funkcyjnego podejścia z rekurencją lub funkcjami wyższego
# rzędu.
# • Zaimplementuj graf jako słownik (dict), gdzie klucz to wierzchołek, a wartość to lista sąsiednich
# wierzchołków.
# • Funkcja powinna przyjmować graf oraz wierzchołek początkowy i końcowy, zwracając
# najkrótszą ścieżkę jako listę wierzchołków.





# # Funkcja BFS
# def bfs(graf, start, koniec):
#     from collections import deque  # Używamy deque do efektywnego dodawania/usuwania elementów
#
#     # Kolejka do przechowywania wierzchołków do odwiedzenia
#     kolejka = deque([start])
#     # Słownik do przechowywania, skąd przyszliśmy do każdego wierzchołka
#     pochodzenie = {start: None}
#
#     # Dopóki kolejka nie jest pusta
#     while kolejka:
#         obecny = kolejka.popleft()  # Bierzemy pierwszy wierzchołek z kolejki
#
#         # Jeśli dotarliśmy do końca, przerywamy
#         if obecny == koniec:
#             break
#
#         # Przechodzimy przez wszystkich sąsiadów obecnego wierzchołka
#         for sasiad in graf[obecny]:
#             if sasiad not in pochodzenie:  # Jeśli jeszcze nie odwiedziliśmy tego sąsiada
#                 kolejka.append(sasiad)  # Dodajemy go do kolejki
#                 pochodzenie[sasiad] = obecny  # Zapisujemy, skąd przyszliśmy
#
#     # Odtwarzamy ścieżkę od końca do początku
#     sciezka = []
#     while koniec is not None:
#         sciezka.append(koniec)
#         koniec = pochodzenie[koniec]
#
#     # Odwracamy ścieżkę, aby była od początku do końca
#     return sciezka[::-1]
#
# # Przykładowy graf
# graf = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# # Testujemy
# start = 'A'
# koniec = 'F'
# sciezka = bfs(graf, start, koniec)
# print(f"Najkrótsza ścieżka z {start} do {koniec}: {sciezka}")

###############################################################################################################

# Zadanie 3 Optymalizacja Rozmieszczenia Zadań (Proceduralne i Funkcyjne)

# Masz N zadań do wykonania, każde zadanie ma przypisany czas wykonania oraz nagrodę za jego
# ukończenie. Twoim celem jest zaplanowanie kolejności wykonywania zadań, aby zminimalizować
# całkowity czas oczekiwania na ich wykonanie i zmaksymalizować zysk.
# Zaimplementuj rozwiązanie przy
# użyciu programowania proceduralnego oraz funkcyjnego.
# Wymagania:
# • Proceduralnie: Stwórz listę zadań i użyj pętli do sortowania i optymalizacji ich kolejności, aby
# zminimalizować całkowity czas oczekiwania.
# • Funkcyjnie: Użyj funkcji wyższego rzędu (sorted, map, reduce) do manipulacji listą zadań, aby
# osiągnąć optymalne rozwiązanie.
# • Program powinien zwrócić optymalną kolejność zadań oraz całkowity czas oczekiwania.


#
# # Funkcja do obliczania całkowitego czasu oczekiwania
# def oblicz_czas_oczekiwania(zadania):
#     całkowity_czas = 0
#     czas_wykonania = 0
#
#     for zadanie in zadania:
#         czas_wykonania += zadanie['czas']
#         całkowity_czas += czas_wykonania - zadanie['czas']
#
#     return całkowity_czas
#
# # Funkcja do optymalizacji kolejności zadań
# def optymalizuj_kolejnosc_proceduralnie(zadania):
#     # Sortujemy zadania według czasu wykonania (najkrótsze zadania pierwsze)
#     zadania.sort(key=lambda x: x['czas'])
#     return zadania
#
# # Przykładowe zadania
# zadania = [
#     {'nazwa': 'Zadanie 1', 'czas': 2, 'nagroda': 5},
#     {'nazwa': 'Zadanie 2', 'czas': 3, 'nagroda': 10},
#     {'nazwa': 'Zadanie 3', 'czas': 1, 'nagroda': 2}
# ]
#
# # Optymalizujemy kolejność
# optymalna_kolejnosc = optymalizuj_kolejnosc_proceduralnie(zadania)
# print("Optymalna kolejność (proceduralnie):", [zadanie['nazwa'] for zadanie in optymalna_kolejnosc])
#
# # Obliczamy całkowity czas oczekiwania
# czas_oczekiwania = oblicz_czas_oczekiwania(optymalna_kolejnosc)
# print("Całkowity czas oczekiwania (proceduralnie):", czas_oczekiwania)

##############################################################################################################


# Zadanie 4: Problem Optymalizacji Zasobów – Algorytm Plecakowy (Proceduralne i Funkcyjne)
# Masz ograniczoną pojemność plecaka oraz listę przedmiotów, z których każdy ma określoną wagę i
# wartość. Celem jest wybranie przedmiotów tak, aby zmaksymalizować łączną wartość w plecaku, nie
# przekraczając jego pojemności. Problem ten wymaga implementacji algorytmu plecakowego (knapsack
# problem) przy użyciu zarówno podejścia proceduralnego, jak i funkcyjnego.
# Wymagania:
# • Proceduralnie: Użyj podejścia dynamicznego (programowanie dynamiczne) do rozwiązania
# problemu.
# • Funkcyjnie: Zaimplementuj algorytm w stylu funkcyjnym z naciskiem na funkcje rekurencyjne
# oraz mapowanie.
# • Program powinien zwracać maksymalną wartość oraz listę przedmiotów, które powinny zostać
# wybrane do plecaka.
#
#

# Funkcja do rozwiązania problemu plecakowego (proceduralnie)
# def plecak_proceduralnie(przedmioty, pojemnosc):
#     n = len(przedmioty)
#     # Tworzymy tabelę do przechowywania wyników podproblemów
#     dp = [[0] * (pojemnosc + 1) for _ in range(n + 1)]
#
#     # Wypełniamy tabelę dp
#     for i in range(1, n + 1):
#         for w in range(pojemnosc + 1):
#             if przedmioty[i - 1]['waga'] <= w:
#                 # Wybieramy lepszą opcję: wziąć przedmiot czy nie
#                 dp[i][w] = max(
#                     dp[i - 1][w],
#                     dp[i - 1][w - przedmioty[i - 1]['waga']] + przedmioty[i - 1]['wartosc']
#                 )
#             else:
#                 # Nie możemy wziąć przedmiotu, bo jest za ciężki
#                 dp[i][w] = dp[i - 1][w]
#
#     # Odtwarzamy listę wybranych przedmiotów
#     wybrane_przedmioty = []
#     w = pojemnosc
#     for i in range(n, 0, -1):
#         if dp[i][w] != dp[i - 1][w]:
#             wybrane_przedmioty.append(przedmioty[i - 1])
#             w -= przedmioty[i - 1]['waga']
#
#     # Zwracamy maksymalną wartość i listę wybranych przedmiotów
#     return dp[n][pojemnosc], wybrane_przedmioty
#
# # Przykładowe przedmioty
# przedmioty = [
#     {'nazwa': 'Przedmiot 1', 'waga': 2, 'wartosc': 10},
#     {'nazwa': 'Przedmiot 2', 'waga': 3, 'wartosc': 15},
#     {'nazwa': 'Przedmiot 3', 'waga': 5, 'wartosc': 20},
#     {'nazwa': 'Przedmiot 4', 'waga': 7, 'wartosc': 25}
# ]
#
# # Pojemność plecaka
# pojemnosc = 10
#
# # Rozwiązujemy problem
# maksymalna_wartosc, wybrane_przedmioty = plecak_proceduralnie(przedmioty, pojemnosc)
# print("Maksymalna wartość (proceduralnie):", maksymalna_wartosc)
# print("Wybrane przedmioty (proceduralnie):", [p['nazwa'] for p in wybrane_przedmioty])




# ##############################################################################################################
#
#
# Zadanie 5. Harmonogramowanie Zadań z Ograniczeniami (Programowanie Funkcyjne i Proceduralne)
# Masz zestaw zadań, gdzie każde zadanie ma określony czas rozpoczęcia, zakończenia oraz nagrodę za
# ukończenie. Twoim celem jest opracowanie harmonogramu, który maksymalizuje nagrodę, wykonując
# jak najwięcej niekolidujących zadań. Zadanie wymaga implementacji algorytmu planowania zadań,
# podobnego do problemu aktywności (Activity Selection Problem) przy użyciu podejścia proceduralnego
# i funkcyjnego.
# Wymagania:
# • Proceduralnie: Zaimplementuj algorytm zachłanny do selekcji zadań na podstawie czasu
# zakończenia.
# • Funkcyjnie: Wykorzystaj funkcje wyższego rzędu, takie jak filter, sorted, reduce, aby
# przefiltrować i posortować zadania oraz wybrać optymalny harmonogram.
# • Program powinien zwracać maksymalną możliwą nagrodę i listę zadań w optymalnym
# harmonogramie.


# Funkcja do harmonogramowania zadań (proceduralnie)
def harmonogramuj_proceduralnie(zadania):
    # Sortujemy zadania według czasu zakończenia (najwcześniej kończące się pierwsze)
    zadania.sort(key=lambda x: x['koniec'])

    wybrane_zadania = []
    ostatni_koniec = 0

    for zadanie in zadania:
        if zadanie['start'] >= ostatni_koniec:
            wybrane_zadania.append(zadanie)
            ostatni_koniec = zadanie['koniec']

    # Obliczamy łączną nagrodę
    laczna_nagroda = sum(zadanie['nagroda'] for zadanie in wybrane_zadania)
    return laczna_nagroda, wybrane_zadania

# Przykładowe zadania
zadania = [
    {'nazwa': 'Zadanie 1', 'start': 1, 'koniec': 3, 'nagroda': 5},
    {'nazwa': 'Zadanie 2', 'start': 2, 'koniec': 5, 'nagroda': 6},
    {'nazwa': 'Zadanie 3', 'start': 4, 'koniec': 6, 'nagroda': 4},
    {'nazwa': 'Zadanie 4', 'start': 6, 'koniec': 8, 'nagroda': 7},
    {'nazwa': 'Zadanie 5', 'start': 7, 'koniec': 9, 'nagroda': 2}
]

# Harmonogramujemy zadania
laczna_nagroda, wybrane_zadania = harmonogramuj_proceduralnie(zadania)
print("Maksymalna nagroda (proceduralnie):", laczna_nagroda)
print("Wybrane zadania (proceduralnie):", [z['nazwa'] for z in wybrane_zadania])


from functools import reduce

# Funkcja do harmonogramowania zadań (funkcyjnie)
def harmonogramuj_funkcyjnie(zadania):
    # Sortujemy zadania według czasu zakończenia (najwcześniej kończące się pierwsze)
    posortowane_zadania = sorted(zadania, key=lambda x: x['koniec'])

    # Funkcja do filtrowania zadań
    def filtruj_zadania(wybrane, zadanie):
        if not wybrane or zadanie['start'] >= wybrane[-1]['koniec']:
            wybrane.append(zadanie)
        return wybrane

    # Używamy reduce do wybrania zadań
    wybrane_zadania = reduce(filtruj_zadania, posortowane_zadania, [])

    # Obliczamy łączną nagrodę
    laczna_nagroda = sum(zadanie['nagroda'] for zadanie in wybrane_zadania)
    return laczna_nagroda, wybrane_zadania

# Przykładowe zadania
zadania = [
    {'nazwa': 'Zadanie 1', 'start': 1, 'koniec': 3, 'nagroda': 5},
    {'nazwa': 'Zadanie 2', 'start': 2, 'koniec': 5, 'nagroda': 6},
    {'nazwa': 'Zadanie 3', 'start': 4, 'koniec': 6, 'nagroda': 4},
    {'nazwa': 'Zadanie 4', 'start': 6, 'koniec': 8, 'nagroda': 7},
    {'nazwa': 'Zadanie 5', 'start': 7, 'koniec': 9, 'nagroda': 2}
]

# Harmonogramujemy zadania
laczna_nagroda, wybrane_zadania = harmonogramuj_funkcyjnie(zadania)
print("Maksymalna nagroda (funkcyjnie):", laczna_nagroda)
print("Wybrane zadania (funkcyjnie):", [z['nazwa'] for z in wybrane_zadania])