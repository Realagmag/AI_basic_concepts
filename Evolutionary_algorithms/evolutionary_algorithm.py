import random
import copy


def evolutionary_algorithm(fun, dimentionality=10, population_size=10, sigma=3, budget=10000):
    best_values = []
    best_entities = []
    for _ in range(50):
        t = 0
        t_max = budget//population_size
        population = [[random.uniform(-100, 100) for gene in range(dimentionality)] for individual in range(population_size)]
        values = list(map(fun, population))
        best_value = min(values)
        index = values.index(best_value)
        best_entity = population[index]
        while t < t_max:
            new_generation = []
            # tournament selection
            for _ in range(population_size):
                individual_index = random.randint(0, population_size-1)
                enemy_index = random.randint(0, population_size-1)
                if values[individual_index] < values[enemy_index]:
                    new_generation.append(copy.deepcopy(population[individual_index]))
                else:
                    new_generation.append(copy.deepcopy(population[enemy_index]))
            # mutation
            for i in range(len(new_generation)):
                for j in range(len(new_generation[i])):
                    new_generation[i][j] = min(max(new_generation[i][j] + sigma*random.gauss(0, 1), -100), 100)

            # succession
            population = copy.deepcopy(new_generation)
            values = list(map(fun, population))

            # picking best
            for i in range(population_size):
                if values[i] < best_value:
                    best_value = values[i]
                    best_entity = population[i]

            t += 1
        best_entities.append(best_entity)
        best_values.append(best_value)

    best_of_bests_values = min(best_values)
    print("best value : ", best_of_bests_values)
    index = best_values.index(best_of_bests_values)
    print("best entity: ", best_entities[index])
    return best_values
