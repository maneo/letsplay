
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


presentation outline
* wstep jakiś
* jak przełożyć gre na problem MLowy?
** jak my postrzegamy gre, a jak postrzega ją algorytm MLowy?
* jak w praktyce pobawić się z czymś takim?
** wziąć pierwszą lepszą grę i zasadzić w niej czujki
** można też wpinać się w inny sposób - przykłady z emulatorów, przykłady ze starcrafta, przykłady z dinozaurem i selenium
* pierwsze podejście - baseline
** random algorithm - jak wygląda, jak długo gra
* drugie podejście - czy sztuczna inteligencja jest w stanie odtworzyć nasze zachowanie?
** przykład z nagrywaniem po czasie
** ale to jest hak ;-) nie dla każdej gry to się sprawdzi
** zachowanie jest dość głupie, uznajmy to za nasz baseline
* trzecie podejście - zbieramy dane
** które elementy gry są istotne?
** ile danych potrzeba?
* ewolucja
** wciąż musimy sami grać? - zróbmy generator, ruchów według koncepcji podobnej jak w algorytmach ewolucyjnych, słabszy przegrywa
* reinforcement learning
** w najgorszym razie tylko omowie koncepcje i nie pokaże przykładu


TODOsy
* wypchnąć do prywatnego repo na github
* uporządkować kody
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