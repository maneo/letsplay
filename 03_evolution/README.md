
# początkowe pomysły

- generowanie sekwencji ruchów, która prowadzi do poprawy, 
- jeżeli doprowadziła do lepszego wyniku, to wchodzi do zbioru treningowego
- jeżeli nie to odrzucamy i gramy jeszcze raz 

# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot

numer_pokolenie = 0

while zysk z kolejnego pokolenia > 0.10: 
    sekwencje_rodziców = []
    jezeli numer_pokolenia > 0: 
     najmocniejsze_sekwencje = wybierz_najmocniejsze_sekwencje(numer_pokolenia)
    jeżeli numer_pokolenia == 0
     najmocniejsze_sekwencje 
    for sekwencja_ruchów w najmocniejsze_sekwencje: 
        proponowana_sekwencja_ruchów = generuj_kolejny_ruch(numer_pokolenia, sekwencja)
        rzeczywista_sekwencja_ruchów, score = graj(proponowana_sekwencja_ruchów, numer_pokolenia) // (jezeli sekwencja skonczy się przed śmiercią - dopełniaj ją jednym ruchem - strzałem)
        zapisz_sekwencje_wynikową
        zapisz dane treningowe
    zapisz zysk z pokolenia 
    zwiększ numer_pokolenia 
    

wybierz_najmocniejsze_sekwencje():
- weź dwie najmocniejsze sekwencje z (numer_pokolenia)
- jeżeli numer pokolenia > 0: weź jedną najmocniejszą z numer_pokolonia - 1
- zwróć trzech najmocniejszych kandydatów. 

# todo

todo
- randomowe algorytmy calkiem niezle sobie radziły, może wykorzystać je do generowania ruchów
- dodać obliczanie punktów z danego pokolenia jako tool i uzależnić od niego dalszą naukę 
- uruchomić żeby sobie grało
- wyuczyć sieć na podstawie najlepszych danych z gier ze stu najlepszych sekwencji
- zobaczyć jak będzie grała
- Klasyfikator który uwzględnia funkcję celu - na tym się trzeba zastanowić 
- Stanem jest sekwencja poprzednich stanów gry. 
- zmienić algorytm tworzenia nowych pokoleń

pytania:
- uwzgledniac to czy udalo sie wykonac wszystkie ruchy - w osobnym pliku
- czy strzal powinien byc domyslnym ruchem - nie, to zaburza ewolucje
- ile ruchów dodawać za jedną ewolucją?  

done 
- Uwzględnić scorea na pewno będzie potrzebny przy RL. 
- dodać licznik punktów do stanu gry
- zeby nieco przyspieszyc ewolucje - zabijac gre 5-10 klatek po zakonczeniu sekwencji ruchow? 
- wybór najlepszych sekwnecji ruchu z każdego pokolenia do uczenia sieci
- w grze zrobić wczytywanie sekwnecji ruchów, przyjmowanie jej na wejściu
- główną pętle uczenia z uruchamianiem gry (narazie jeden wątek)
- wczytywanie sekwencji ruchow
- zapisywanie ruchow wykonanych + score + time