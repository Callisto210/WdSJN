Autorzy: Patryk Duda, Paweł Wandzel

Wymagania: Python 3.6, PLY 3.11

Uruchomienie: python3 main.py

Przykładowe wyrażenia: examples.txt

Sposób wykonania:
  Preprocessing:
    sprowadzenie liczebników do formy podstawowej (przy pomocy słownika z numerals.txt)
    algorytm przekształcający liczbę w zapisie słownym na ciąg cyfr (z obsługą liczb z kropką dziesiętną)
  Parser LALR dla gramatyki obsługującej:
    liczby z opcjonalną kropką dziesiętną
    liczby: pi i e
    dodawanie/odejmowanie/mnożenie/dzielenie
    wyrażenia w nawiasach
    operację modulo
    potęgowanie
    funkcje: sinus, cosinus, pierwiastek kwadratowy, silnia (+ możliwość łatwego dodania kolejnych)
