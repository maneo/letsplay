

- evaluation xgb with 10 attempts, resulted with, avg time: 34.6 and avg score: 4.1 - human/1frame
- evaluation mlp with 10 attempts, resulted with, avg time: 17.8 and avg score: 7 - human/1frame
- evaluation mlp with 10 attempts, resulted with, avg time: 13.7 and avg score: 4.55  - all/1frame
- evaluation xgb with 10 attempts, resulted with, avg time: 27.9 and avg score: 6.55 - all/1frame
- evaluation xgb with 5 attempts, resulted with, avg time: 29.44 and avg score: 8.76 - evo/1frame



    
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

