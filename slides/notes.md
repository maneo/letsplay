
presentation outline
* wstęp jakiś
* jak przełożyć grę na problem MLowy?
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
* przez jakie poziomy MLa przeszliśmy?
** sformulowanie problemu
** uczenie reprezentacji
** dobór modelu
** eksploracja przestrzeni rozwiazan
* schemat odbiornika radiowego na końcu


Only time

* step 1: one game -- too few observations - to perform generalization, plays poorly
* step 2: is neural network able to generalize that? maybe with more data? - yes, but..

drawbacks?
* when last too long (longer than longest game) model will lost his ability to decide

What is the simpletst solution?

only time % 126 and action

* minimal data set showing basic strategy --> looped

drawbacks?
* does not take into account position of rocks, cannot escape from side attack - simple, record, replay!

Comaprision

evaluation only_time (forest) with 10 attempts, resulted with, avg time: 77.1 and avg score: 109.3
evaluation synth_126 (forest) with 10 attempts, resulted with, avg time: 154.2 and avg score: 237.7

evaluation only_time (mlp) with 10 attempts, resulted with, avg time: 83.3 and avg score: 122
evaluation synth_126 (mlp) with 10 attempts, resulted with, avg time: 193.7 and avg score: 296

evaluation only_time (xgb) with 10 attempts, resulted with, avg time: 37.5 and avg score: 92.8
evaluation synth_126 (xgb) with 10 attempts, resulted with, avg time: 94.9 and avg score: 250.3

