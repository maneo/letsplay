
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

Random

Evaluation random with 10 attempts, resulted with, avg time: 35.9 and avg score: 27.7

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

dynamics

Comaprision

evaluation only_time (forest) with 10 attempts, resulted with, avg time: 77.1 and avg score: 109.3
evaluation synth_126 (forest) with 10 attempts, resulted with, avg time: 154.2 and avg score: 237.7

evaluation only_time (mlp) with 10 attempts, resulted with, avg time: 83.3 and avg score: 122
evaluation synth_126 (mlp) with 10 attempts, resulted with, avg time: 193.7 and avg score: 296

evaluation only_time (xgb) with 10 attempts, resulted with, avg time: 37.5 and avg score: 92.8
evaluation synth_126 (xgb) with 10 attempts, resulted with, avg time: 94.9 and avg score: 250.3



Tytuł: Let's play! - The only AI presentation you will ever need!

Abstract:
ML and AI technologies are a great tool to automate various business processess. In this short presentation I will try to automate something significant, something which usually takes long hours, may ruin health, lead to sleep deprevation, may even break up families... we will try to teach computers play games so we won't have to. How to translate game play problem into language of ML algorithms? I will explore possible solutions from the simplest manually crafted algorithm through classical supervised learning methods to end up with reinforcement learning based approaches. This presentation may contain asteroids, spaceships, laser guns and a significant portion of poor Python code.

Długie bio
Search Team manager in allegro.pl, on a daily basis I work on improving search experience in the biggest ecommerce site in Poland. I am professinaly involved with Java and related technologies since 2004, currently focused on search and information retrieval. Organizer of GeeCON conference (http://geecon.org) and former leader of Poznan Java User Group (http://www.jug.poznan.pl).


krótkie bio
Search Team manager in allegro.pl

hashtag bio:
#ai #gaming #search #programming-languages 


toreads
- http://dkopczyk.quantee.co.uk/genetic-algorithm/
- https://www.toptal.com/deep-learning/pytorch-reinforcement-learning-tutorial
- https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6
- http://pybrain.org/docs/tutorial/reinforcement-learning.html
- https://hub.packtpub.com/tools-for-reinforcement-learning/
- https://github.com/deepmind/lab
- https://github.com/openai/retro
- https://github.com/kengz/SLM-Lab
- https://github.com/NervanaSystems/coach
- https://skymind.ai/wiki/python-ai#rl
- https://github.com/openai/roboschool
- https://github.com/M-J-Murray/MAMEToolkit
- https://www.analyticsvidhya.com/blog/2019/04/introduction-deep-q-learning-python/
- https://gym.openai.com/
- https://github.com/p-christ/Deep-Reinforcement-Learning-Algorithms-with-PyTorch
- https://skymind.ai/wiki/python-ai#rl
- https://github.com/manuel-calzolari/sklearn-genetic
- https://github.com/josephmisiti/awesome-machine-learning#python-reinforcement-learning


