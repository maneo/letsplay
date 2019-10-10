Source code and samples for "Let's play" - use them responsibly.

Presentation title: Let's play! - The only AI presentation you will ever need!

Abstract:
```ML and AI technologies are a great tool to automate various business processess. 
In this short presentation I will try to automate something significant, something 
which usually takes long hours, may ruin health, lead to sleep deprevation, may 
even break up families... we will try to teach computers play games so we won't
have to. How to translate game play problem into language of ML algorithms? I 
will explore possible solutions from the simplest manually crafted algorithm 
through classical supervised learning methods to end up with reinforcement 
learning based approaches. This presentation may contain asteroids, spaceships, 
laser guns and a significant portion of poor Python code.
```

If you want to play with this source code take a look at ```conda``` folder contains conda env with all necessary dependencies. Create conda env and activate it.

Each folder contains a little bit different things :-) but in general to prepare training data run

```
python3 shmup-train.py > training.log
```

This should output numeric data about your gameplay. 

```
tail -n +3 training.log > train.csv; sed -i '' -e '$ d' train.csv
```

You can play with data and tweak model in ```ai_model.ipynb``` notebook. This notebook should output ```ai_model.pkl```, which is used by shmup-play.py.

To launch your model use:

```
python3 shmup-play.py
```

in case of 03_evolutino use ```shmup-play.sh``` plays move sequences from ```evolution``` subfolder. 

If you want to launch model use ```shmup-lay-ai.sh model_name```.
