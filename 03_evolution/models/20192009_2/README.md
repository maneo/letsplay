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

