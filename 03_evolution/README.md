
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
- główną pętle uczenia z uruchamianiem gry (narazie jeden wątek)
- xargsem zrownloeglic
- w grze zrobić wczytywanie sekwnecji ruchów, przyjmowanie jej na wejściu
- wybór najlepszych sekwnecji ruchu z każdego pokolenia do uczenia sieci


# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot

pytania:
- uwzgledniac to czy udalo sie wykonac wszystkie ruchy
- czy strzal powinien byc domyslnym ruchem

done 
- wczytywanie sekwencji ruchow
- zapisywanie ruchow wykonanych + score + time