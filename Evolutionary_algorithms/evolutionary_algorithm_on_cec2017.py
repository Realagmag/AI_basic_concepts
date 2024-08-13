from evolutionary_algorithm import evolutionary_algorithm
from cec2017.functions import f2, f13
import csv
from statistics import mean, stdev

for i in range(1):
    sigma = 0.4
    population_size = 64
    budget = 10000
    f = f13            # Change to f2 to use on different function
    best_values = evolutionary_algorithm(f, dimentionality=10, population_size=population_size, sigma=sigma, budget=budget)
    with open("wyniki_f13_poprawka.txt", 'a') as file:
        writer = csv.writer(file)
        writer.writerow([f'Population size: {population_size}',
                        f'sigma : {sigma:0.02f}',
                        f'budget : {budget}'])
        writer.writerow([f'Min value: {min(best_values):0.02f}',
                        f'Max value: {max(best_values):0.02f}',
                        f'Mean value: {mean(best_values):0.02f}',
                        f'Stdev value: {stdev(best_values):0.02f}'])
        writer.writerow(["---------------------------------------"])

