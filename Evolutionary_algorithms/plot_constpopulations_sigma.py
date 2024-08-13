import matplotlib.pyplot as plt


with open("wyniki_f13_sigma.txt") as file:
    first_line = True
    sigma_vector = []
    mean_vector = []
    stdev_vector = []
    for row in file:
        row = row.rstrip()
        if row and row[0] != "-":
            if first_line:
                first_line = False
                info = row.split(",")
                sigma = info[1].split(" ")[-1]
                sigma_vector.append(float(sigma))
            else:
                first_line = True
                info = row.split(",")
                mean = info[2].split(" ")[-1]
                mean_vector.append(float(mean))
                stdev = info[3].split(" ")[-1]
                stdev_vector.append(float(stdev))
                
plt.plot(sigma_vector[3:-30], stdev_vector[3:-30], marker='o', linestyle='-')
plt.xlabel('Sigma')
plt.ylabel('Stdev of Lowest Value')
plt.title('CEC2017 f13')
plt.grid(True)
plt.show()