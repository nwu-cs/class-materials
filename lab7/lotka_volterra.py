#! /usr/bin/python

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

prey = 25
predators = 25
prey_carrying_capacity = 10000
prey_growth_rate = 0.4
predator_death_rate = 0.05
predation = 0.01
kills_per_predator_offspring = 90

print('prey_carrying_capacity', 'prey_growth_rate', 'predator_death_rate', 'predation', 'kills_per_predator_offspring')
print(prey_carrying_capacity, prey_growth_rate, predator_death_rate, predation, kills_per_predator_offspring)
print()

print('day', 'prey', 'predators')
daylist=[]
preylist=[]
predlist=[]
for day in range(1000):
    print(day, prey, predators)
    daylist.append(float(day))
    preylist.append(prey)
    predlist.append(predators)
    new_prey = max(prey * (1 + prey_growth_rate * (prey_carrying_capacity - prey) / prey_carrying_capacity - predation * predators), 0)
    new_predators = max(predators * (1 - predator_death_rate + (predation / kills_per_predator_offspring) * prey), 0)
    prey = new_prey
    predators = new_predators

plt.plot(daylist,preylist,daylist,predlist)
plt.show()
