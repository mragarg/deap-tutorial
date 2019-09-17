import random

from deap import base
from deap import creator
from deap import tools

IND_SIZE = 5

creator.create("FitnessMin", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)

# building the first individual
ind1 = toolbox.individual()

print(ind1)
print(ind1.fitness.valid)