A March Madness bracket picker based on dice roll battle logic. 

## Usage
```
main.py [--rounds ROUNDS] [--randomness LEVEL]
```

`--rounds` determines how many times to run each simulated battle. More rounds leads to
more predictable results based on season performance and seed number. Fewer rounds makes
the bracket more prone to upsets. 3-7 seems to be a good range for fairly probable results.

`--randomness` determines how much random chance affects each battle. More randomness 
leads to more fluke DRAGON victories and more missed attacks. Range is between 1 and 5.

## Team stats
* *Health Points* -- each team starts each battle with 100 HP
* *Attack Points* -- teams' AP are determined by a combination of their average points 
scored per game in the regular season and their seed number, scaled to 5. A #1 seed who
scored the most points per game this year will have 5 AP. Attack damage is calculated by
rolling a D20 and adding the attacker's AP.
* *Defense Points* -- teams' DP are determined by combining their average allowed points 
per game in the regular season and their seed number, again scaled to 5. The team who 
allowed the fewest points per game with a #1 seed will have 5 DP. Attack damage is 
calculated by taking the attack's damage and subtracting the attacked team's DP.

## Random events
To approximate the "upset" factor common in the tournament, several random events can 
occur during battle:

* Attacks can miss with a frequency of up to (`--randomness` * 10)%
* DRAGONS may appear and destroy a team, leading to instant victory for the 
opposing team.
