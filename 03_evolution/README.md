# TODO
- nauczyc ewolucje na podstawie synth-time
- sprawdzic model na 4 klatkach

# Eksperyment 20192009_14

reprezentacja: macierz 6x10 - asteroidy, macierz 6x10 - kule, 2 klatki

dane treningowe: train.csv, ~3800 (klikane)


training
* mlp: Training accuracy: 1.00, evaluation accuracy: 0.80
* forest: evaluate_model(X_train, y_train, X_test, y_test, forest_model)
* xgb: Training accuracy: 0.98, evaluation accuracy: 0.90
* logit: Training accuracy: 0.66, evaluation accuracy: 0.60

wyniki
* evaluation logit with 10 attempts, resulted with, avg time: 1.5 and avg score: 0.2
* evaluation xgb with 10 attempts, resulted with, avg time: 1.7 and avg score: 2.6
* evaluation mlp with 10 attempts, resulted with, avg time: 4.5 and avg score: 21.1333
* evaluation forest with 10 attempts, resulted with, avg time: 2.2 and avg score: 0.1

# Eksperyment 20192009_12

reprezentacja: macierz 6x10, 2 klatki

dane treningowe: train.csv, 2359 (klikane)

logit: Training accuracy: 0.52, evaluation accuracy: 0.43
mlp: Training accuracy: 1.00, evaluation accuracy: 0.58

evaluation logit with 10 attempts, resulted with, avg time: 7,1 and avg score: 16
evaluation xgb with 10 attempts, resulted with, avg time: 7,4 and avg score: 13,7
evaluation mlp with 10 attempts, resulted with, avg time: 7,5 and avg score: 43,3
evaluation forest with 10 attempts, resulted with, avg time: 3 and avg score: 0,1

```
mlp_model = MLPClassifier(solver='adam', alpha=1e-5, 
                    hidden_layer_sizes=(60, 24, 24), 
                          random_state=1, verbose=True)
```

wersja extended: train_extended.csv, ~8k klikane (poprzednia iteracja włączona)

```
mlp_model = MLPClassifier(solver='adam', alpha=1e-5, 
                    hidden_layer_sizes=(24, 24, 24), 
                          random_state=1, verbose=True, max_iter=1000)

mlp_model.fit(X_train_all, y_train_all)
```

evaluation mlp with 10 attempts, resulted with, avg time: 9,48 and avg score: 27,18

model xgb o rząd wielkosci wiekszy jezeli chodzi o rozmiar


# Eksperyment 20192009_11

- macierz 6x10 w kazdej macierzy ile jest asteroidów.

dane: ewolucyjne.

logit: Training accuracy: 0.31, evaluation accuracy: 0.30
xgb: Training accuracy: 0.41, evaluation accuracy: 0.32
forest: Training accuracy: 0.99, evaluation accuracy: 0.36
mlp: Training accuracy: 0.49, evaluation accuracy: 0.30

evaluation logit with 10 attempts, resulted with, avg time: 3.7 and avg score: 7.85
evaluation xgb with 10 attempts, resulted with, avg time: 7.75 and avg score: 11.65
evaluation mlp with 10 attempts, resulted with, avg time: 6 and avg score: 19.5333
evaluation forest with 10 attempts, resulted with, avg time: 11.15 and avg score: 13.25

miks danych ewolucyjnych i klikanych: 32343

logit: Training accuracy: 0.29, evaluation accuracy: 0.29
xgb: Training accuracy: 0.36, evaluation accuracy: 0.30
forest: Training accuracy: 0.99, evaluation accuracy: 0.33
mlp: Training accuracy: 0.43, evaluation accuracy: 0.27

evaluation logit with 10 attempts, resulted with, avg time: 4.1 and avg score: 9.6
evaluation xgb with 10 attempts, resulted with, avg time: 8.73333 and avg score: 13.1667
evaluation mlp with 10 attempts, resulted with, avg time: 5.525 and avg score: 19.275
evaluation forest with 10 attempts, resulted with, avg time: 11.2 and avg score: 15.8

- forest też ma objawy myslenia.


model xgb o rząd wielkosci wiekszy.

# Eksperyment 20192009_10

- macierz 6x10 w kazdej macierzy ile jest asteroidów.

```
features = ["f" + str(i) for i in range(0,61)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_10/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: 7148 (klikane)

logit: Training accuracy: 0.39, evaluation accuracy: 0.37
xgb: Training accuracy: 0.52, evaluation accuracy: 0.34
forest: Training accuracy: 1.00, evaluation accuracy: 0.37
mlp: ~ Training accuracy: 0.83, evaluation accuracy: 0.28

evaluation logit with 10 attempts, resulted with, avg time: 1 and avg score: 0
evaluation xgb with 10 attempts, resulted with, avg time: 1.7 and avg score: 2.8
evaluation mlp with 10 attempts, resulted with, avg time: 3.1 and avg score: 12.9
evaluation mlp_60_24_24 with 10 attempts, resulted with, avg time: 4.35 and avg score: 17.7
evaluation forest with 10 attempts, resulted with, avg time: 2.2 and avg score: 0.8


# Eksperyment 20192109_1

ile czlowiek naklika w 1100 klatek? 
time: 67 sec, score: 201


# Eksperyment 20192009_9

testowany wektor: player_x / 48, rich mob, 1 klatka
rich mob - speedx, speedy, dist_x, / 48 dist_y / 60

```
features = ["f" + str(i) for i in range(0,33)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_9/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```
dane treningowe: klikane (~10k)

Dataset has 2026 (19.1%) duplicate rows

wyniki:

logit: 
- Training accuracy: 0.46, evaluation accuracy: 0.45
xgb: 
- Training accuracy: 0.62, evaluation accuracy: 0.59 (estimators: 100)
- Training accuracy: 0.70, evaluation accuracy: 0.65 (estimators: 500)
mlp: 
- Training accuracy: 0.70, evaluation accuracy: 0.68
forest: 
- Training accuracy: 0.78, evaluation accuracy: 0.40 (estimators: 100)

evaluation logit with 10 attempts, resulted with, avg time: 6.26667 and avg score: 8.01667
evaluation xgb with 10 attempts, resulted with, avg time: 4.98333 and avg score: 5.45
evaluation mlp with 10 attempts, resulted with, avg time: 4.56667 and avg score: 6.58333
evaluation forest with 10 attempts, resulted with, avg time: 3.65 and avg score: 3.95

chetniej lata, ale stracil chęć do strzelania.

wyglada na to, ze jak gra czlowiek to za wolno strzela w wyniku - tego jest dużo więcej pustych
rekordów przesuwaniem, a mniej ze strzelaniem?

po recznym przepisaniu (po predykcji) stanów na strzeljące:
evaluation logit with 10 attempts, resulted with, avg time: 6.71429 and avg score: 8.85714
evaluation xgb with 10 attempts, resulted with, avg time: 5.54286 and avg score: 8.21429
evaluation mlp with 10 attempts, resulted with, avg time: 4.84286 and avg score: 8.17143
evaluation forest with 10 attempts, resulted with, avg time: 5.5 and avg score: 8.3


# Eksperyment 20192009_8

testowany wektor: player_x / 48, rich mob, 1 klatka
rich mob - speedx, speedy, dist_x, / 48 dist_y / 60


```
features = ["f" + str(i) for i in range(0,33)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_8/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (~29k)

evaluation logit with 10 attempts, resulted with, avg time: 7.26667 and avg score: 9.83333
evaluation xgb with 10 attempts, resulted with, avg time: 5.06667 and avg score: 6.83333
evaluation mlp with 10 attempts, resulted with, avg time: 4 and avg score: 6.86667

dane treningowe: ewolucyjne (47506)

evaluation logit with 10 attempts, resulted with, avg time: 7.26667 and avg score: 9.83333
evaluation xgb with 10 attempts, resulted with, avg time: 5.06667 and avg score: 6.83333
evaluation mlp with 10 attempts, resulted with, avg time: 4 and avg score: 6.86667

dane treningowe: ewolucyjne (84370)

Dataset has 19220 (22.8%) duplicate rows

evaluation logit with 10 attempts, resulted with, avg time: 7.8 and avg score: 10.05
evaluation xgb with 10 attempts, resulted with, avg time: 6.025 and avg score: 6.725
evaluation mlp with 10 attempts, resulted with, avg time: 5.05 and avg score: 7.875

dane treningowe: 112910

mlp: Training accuracy: 0.38, evaluation accuracy: 0.38
xgb Training accuracy: 0.42, evaluation accuracy: 0.38
logit: Training accuracy: 0.30, evaluation accuracy: 0.30
forest: Training accuracy: 0.78, evaluation accuracy: 0.40 (model wazy powyzej 4GB)

evaluation logit with 10 attempts, resulted with, avg time: 7.04 and avg score: 9.28
evaluation xgb with 10 attempts, resulted with, avg time: 5.6 and avg score: 6.38
evaluation mlp with 10 attempts, resulted with, avg time: 5.28 and avg score: 7.9
evaluation forest with 10 attempts, resulted with, avg time: 5 and avg score: 7.9

# Eksperyment 20192009_7

testowany wektor: player_x / 480, rich mob, 1 klatka
rich mob - speedx, speedy, dist_x, / 480 dist_y / 600

```
features = ["f" + str(i) for i in range(0,33)]
label = ["action"]

headers = features + label

df = pd.read_csv('models/20192009_7/train.csv', 
                 sep = ',', 
                 header = None,
                 names = headers)
df
```

dane treningowe: ewolucyjne (~20k)

evaluation logit with 10 attempts, resulted with, avg time: 6.9 and avg score: 9.3
evaluation xgb with 10 attempts, resulted with, avg time: 5.3 and avg score: 5.85
evaluation mlp with 10 attempts, resulted with, avg time: 4.45 and avg score: 7.7

# Eksperyment 20192009_6

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


# Eksperyment 20192009_5

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

# Eksperyment 20192009_4

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


# Eksperyment 20192009_3

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

    
# Eksperyment 20192009_2

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

# Eksperyment 20192009_1

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

