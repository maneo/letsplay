

- evaluation xgb with 10 attempts, resulted with, avg time: 34.6 and avg score: 4.1 - human/1frame
- evaluation mlp with 10 attempts, resulted with, avg time: 17.8 and avg score: 7 - human/1frame
- evaluation mlp with 10 attempts, resulted with, avg time: 13.7 and avg score: 4.55  - all/1frame
- evaluation xgb with 10 attempts, resulted with, avg time: 27.9 and avg score: 6.55 - all/1frame
- evaluation xgb with 5 attempts, resulted with, avg time: 29.44 and avg score: 8.76 - evo/1frame

Eksperyment 20192109_1

ile czlowiek naklika w 1100 klatek? 
time: 67 sec, score: 201



Eksperyment 20192009_7

testowany wektor: player_x / 480, rich mob, 1 klatka
rich mob - speedx, speedy, dist_x, / 480 dist_y / 600

```
features = ["f" + str(i) for i in range(0,33)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_6/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (~20k)

evaluation logit with 10 attempts, resulted with, avg time: 6.9 and avg score: 9.3
evaluation xgb with 10 attempts, resulted with, avg time: 5.3 and avg score: 5.85
evaluation mlp with 10 attempts, resulted with, avg time: 4.45 and avg score: 7.7

Eksperyment 20192009_6

testowany wektor: player_x, rich mob, 1 klatka
rich mob - speedx, speedy, dist_x, dist_y

XGBClassifier(n_estimators=500)
MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 24), random_state=1, max_iter=200000)

```
features = ["f" + str(i) for i in range(0,33)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_6/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (26 617)

ewaluacja:
evaluation logit with 10 attempts, resulted with, avg time: 5.1 and avg score: 10.8
evaluation xgb with 10 attempts, resulted with, avg time: 8.4 and avg score: 8.1
evaluation mlp with 10 attempts, resulted with, avg time: 3.4 and avg score: 8.5


Eksperyment 20192009_5

testowany wektor: player_x, rich mob, 1 klatka
rich mob - speedx, speedy, distance, dist_x, dist_y, mob_x, mob_y

XGBClassifier(n_estimators=500)
MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 24), random_state=1, max_iter=200000)

```
features = ["f" + str(i) for i in range(0,57)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_5/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```
dane treningowe: ewolucyjne (only alive, 4100)

evaluation logit with 10 attempts, resulted with, avg time: 7.60976 and avg score: 3.4878
evaluation xgb with 10 attempts, resulted with, avg time: 5.5 and avg score: 9
evaluation mlp with 10 attempts, resulted with, avg time: 8.83333 and avg score: 15.8667

Eksperyment 20192009_4

testowany wektor: player_x, rich mob, 1 klatka
rich mob - speedx, speedy, distance, dist_x, dist_y, mob_x, mob_y

XGBClassifier(n_estimators=500)
MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 24), random_state=1, max_iter=200000)

```
features = ["f" + str(i) for i in range(0,57)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_4/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (89835)

ewaluacja:
evaluation logit with 10 attempts, resulted with, avg time: 7.93548 and avg score: 3.6129
evaluation xgb with 10 attempts, resulted with, avg time: 5.96667 and avg score: 9.03333
evaluation mlp with 10 attempts, resulted with, avg time: 11.1 and avg score: 16.7


Eksperyment 20192009_3

testowany wektor: player_x, rich mob, 1 klatka
rich mob - speedx, speedy, distance, dist_x, dist_y, mob_x, mob_y

XGBClassifier(n_estimators=500)
MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 24), random_state=1, max_iter=200000)

```
features = ["f" + str(i) for i in range(0,57)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_3/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (41 383)

ewaluacja:
evaluation logit with 10 attempts, resulted with, avg time: 6.47619 and avg score: 3.95238
evaluation xgb with 10 attempts, resulted with, avg time: 7.5 and avg score: 10.05
evaluation mlp with 10 attempts, resulted with, avg time: 8.9 and avg score: 18

    
Eksperyment 20192009_2

testowany wektor: player_speed_x, player_x, rich mob, 2 klatki
rich mob - speedx, speedy, distance, dist_x, dist_y, mob_x, mob_y

```
features = ["f" + str(i) for i in range(0,117)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_2/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
```

XGBClassifier(n_estimators=500)
MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 24), random_state=1, max_iter=200000)

dane treningowe: ewolucyjne (47 800)

evaluation logit with 10 attempts, resulted with, avg time: 12.3 and avg score: 6.3
evaluation xgb with 10 attempts, resulted with, avg time: 4.4 and avg score: 11.6
evaluation mlp with 10 attempts, resulted with, avg time: 5.5 and avg score: 20



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

