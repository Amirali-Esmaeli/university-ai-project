import random

def generate_individual():
    individual = [0] * 10
    indices = random.sample(range(10), 5)
    for i in indices:
        individual[i] = 1
    return individual

def generate_population(size):
    return [generate_individual() for _ in range(size)]

def fitness(individual, exposures):
    return sum(exposures[i] for i in range(10) if individual[i] == 1)

def tournament_selection(population, exposures, k=3):
    selected = random.sample(population, k)
    return max(selected, key=lambda ind: fitness(ind, exposures))

