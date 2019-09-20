Eksperyment 20192009_1

testowany wektor: player_speed_x, player_x, rich mob, 2 klatki
rich mob - speedx, speedy, distance, dist_x, dist_y, mob_x, mob_y

dane treningowe: ewolucyjne (?k), human (~?k)

XGBClassifier(n_estimators=500)
Training accuracy: 0.61, evaluation accuracy: 0.52

XGBClassifier(n_estimators=100)
Training accuracy: 0.53, evaluation accuracy: 0.53

Model do testu wytrenowany na pełnych danych.
- evaluation xgb with 10 attempts, resulted with, avg time: 1.3 and avg score: 0.65
- evaluation mlp with 10 attempts, resulted with, avg time: 1.66667 and avg score: 1.83333
- evaluation logit with 10 attempts, resulted with, avg time: 4.64516 and avg score: 13
(ciagle strzela i stoi w miejscu)

