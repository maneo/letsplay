
- generowanie sekwencji ruchów, która prowadzi do poprawy, 
- jeżeli doprowadziła do lepszego wyniku, to wchodzi do zbioru treningowego
- jeżeli nie to odrzucamy i gramy jeszcze raz 


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

todo:
- xargsem zrownloeglic
- zeby nieco przyspieszyc ewolucje - zabijac gre 5-10 klatek po zakonczeniu sekwencji ruchow? 
- dodać obliczanie punktów z danego pokolenia jako tool i uzależnić od niego dalszą naukę 
- uruchomić żeby sobie grało
- dodać licznik punktów do stanu gry
- Uwzględnić scorea na pewno będzie potrzebny przy RL. 
- Klasyfikator który uwzględnia funkcję celu - na tym się trzeba zastanowić 
- Stanem jest sekwencja ruchów. 

# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot

pytania:
- uwzgledniac to czy udalo sie wykonac wszystkie ruchy
- czy strzal powinien byc domyslnym ruchem

done 
- wybór najlepszych sekwnecji ruchu z każdego pokolenia do uczenia sieci
- w grze zrobić wczytywanie sekwnecji ruchów, przyjmowanie jej na wejściu
- główną pętle uczenia z uruchamianiem gry (narazie jeden wątek)
- wczytywanie sekwencji ruchow
- zapisywanie ruchow wykonanych + score + time