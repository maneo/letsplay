
To prepare training data run

```
python3 shmup-train.py > training.log
```

This should output numeric data about your gameplay. 

```
tail -n +3 training.log > train.csv
```

You can play with data and tweak model in ai_model.ipynb notebook. This notebook shoulld output ai_model.pkl, which is used by shmup-play.py.

To launch your model use:

```
python3 shmup-play.py
```

preso
* nagrywanie akcja w oparciu o czas
* model w oparciu o odleglosc w x od skaly
* akcja w oparciu o odleglosc od skraju planszy i ciagle strzelanie
* do modelu dodac pamiec klatek
* reinforcement learning niech sam wymyśli optymalny algorytm

todo
* dodać licznik punktów
* dodac odleglosc w x i y
* dodać pamiec poprzednich klatek

done
* model w oparciu o sieć neuronową
* dodac dwa nowe stany, przesun sie w prawo i strzel, przesun sie w lewo i strzel


TODOsy
* uporządkować kody
* generowanie losowych ruchów jako model i jego ewaluacja
* zrobić slajdy początkowe - jak postrzega świat algorytm MLowy?
* slajdy do jak wpiąć się w gre?
* slajdy do baseline 1
* slajdy do baseline 2
* slajdy do zbieramy dane
* kodas do ewolucji - generator ruchów
* slajdy do reinforcmenet leanirngu
* zdecydować czy zmergować ewolucje z RL?
* slajdy do ewolucji
* kodas do reinforcement learningu

DONE
* wypchnąć do prywatnego repo na github
