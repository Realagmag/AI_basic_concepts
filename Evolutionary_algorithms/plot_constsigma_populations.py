import matplotlib.pyplot as plt


with open("wyniki_f13.txt") as file:
    first_line = True
    population_vector = []
    mean_vector = []
    stdev_vector = []
    for row in file:
        row = row.rstrip()
        if row and row[0] != "-":
            if first_line:
                first_line = False
                info = row.split(",")
                population_size = info[0].split(" ")[-1]
                population_vector.append(float(population_size))
            else:
                first_line = True
                info = row.split(",")
                mean = info[2].split(" ")[-1]
                mean_vector.append(float(mean))
                stdev = info[3].split(" ")[-1]
                stdev_vector.append(float(stdev))
                
plt.plot(population_vector[1:], mean_vector[1:], marker='o', linestyle='-')
plt.xlabel('Population Size')
plt.ylabel('Mean Lowest Value')
plt.title('CEC2017 f13')
plt.grid(True)
plt.show()