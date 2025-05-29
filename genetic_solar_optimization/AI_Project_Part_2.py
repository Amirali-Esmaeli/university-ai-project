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

def crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, 9), 2))  # دو نقطه تصادفی بین 1 و 8
    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]

    # تنظیم تعداد 1ها به 5
    ones = sum(child)
    if ones > 5:
        indices = [i for i, x in enumerate(child) if x == 1]
        for i in random.sample(indices, ones - 5):
            child[i] = 0
    elif ones < 5:
        indices = [i for i, x in enumerate(child) if x == 0]
        for i in random.sample(indices, 5 - ones):
            child[i] = 1
    return child

def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        ones = [i for i, x in enumerate(individual) if x == 1]
        zeros = [i for i, x in enumerate(individual) if x == 0]
        if ones and zeros:
            one_idx = random.choice(ones)
            zero_idx = random.choice(zeros)
            individual[one_idx], individual[zero_idx] = 0, 1
    return individual

def genetic_algorithm(exposures, population_size=10, generations=20):
    population = generate_population(population_size)
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, exposures)
            parent2 = tournament_selection(population, exposures)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    
    # پیدا کردن بهترین فرد
    best_individual = max(population, key=lambda ind: fitness(ind, exposures))
    best_fitness = fitness(best_individual, exposures)
    return best_individual, best_fitness

def main():
    # لیست نمونه نوردهی
    exposures = [2, 5, 8, 1, 3, 9, 4, 6, 7, 2]
    best_individual, best_fitness = genetic_algorithm(exposures)
    print(f"بهترین رشته باینری: {best_individual}")
    print(f"مجموع نوردهی: {best_fitness}")

if __name__ == "__main__":
    main()
    
# خروجی
# بهترین رشته باینری: [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
# مجموع نوردهی: 35