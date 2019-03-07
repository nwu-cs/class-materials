#! /usr/bin/python

from __future__ import division, print_function

from scipy.integrate import ode


# [prey, predators]
initial_state = [25, 25]

# [prey_carrying_capacity, prey_growth_rate, predator_death_rate, predation, kills_per_predator_offspring]
parameters = [10000, 0.4, 0.05, 0.01, 95]


def derivative_at(time, state, prey_carrying_capacity, prey_growth_rate, predator_death_rate, predation, kills_per_predator_offspring):
    return [state[0] * (prey_growth_rate * (prey_carrying_capacity - state[0]) / prey_carrying_capacity - predation * state[1]), state[1] * (-predator_death_rate + (predation / kills_per_predator_offspring) * state[0])]


print('prey_carrying_capacity', 'prey_growth_rate', 'predator_death_rate', 'predation', 'kills_per_predator_offspring')
print(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])
print()

integrator = ode(derivative_at)
integrator.set_initial_value(initial_state, 0)
integrator.set_f_params(*parameters)

print('day', 'prey', 'predators')
while integrator.successful() and integrator.t < 1000:
    print(integrator.t, integrator.y[0], integrator.y[1])
    integrator.integrate(integrator.t + 1)
