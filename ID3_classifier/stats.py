from statistics import mean, stdev
import csv

data = []
with open("wyniki_grzyby_ograniczony.txt", 'r') as file:
    data = []
    true_positive = []
    true_negative = []
    false_positive = []
    false_negative = []

    for row in file:
        splited = row.split(",")
        accuracy = splited[0].split(" ")[1]
        tp = splited[1].split(" ")[2]
        tn = splited[2].split(" ")[2]
        fp = splited[3].split(" ")[2]
        fn = splited[4].split(" ")[2]
        data.append(float(accuracy))
        true_positive.append(float(tp))
        true_negative.append(float(tn))
        false_positive.append(float(fp))
        false_negative.append(float(fn))

with open("grzyby_stats_ograniczony.txt", 'a') as file2:
    writer = csv.writer(file2)
    writer.writerow(["accuracy:"])
    writer.writerow([f'min value: {min(data):0.04f}'])
    writer.writerow([f'max value: {max(data):0.04f}'])
    writer.writerow([f'mean value: {mean(data):0.04f}'])
    writer.writerow([f'stdev value: {stdev(data):0.04f}'])
    writer.writerow('-----------------------------------')
    writer.writerow(["true positive:"])
    writer.writerow([f'min value: {min(true_positive):0.02f}'])
    writer.writerow([f'max value: {max(true_positive):0.02f}'])
    writer.writerow([f'mean value: {mean(true_positive):0.02f}'])
    writer.writerow([f'stdev value: {stdev(true_positive):0.02f}'])
    writer.writerow('-----------------------------------')
    writer.writerow(["true negative:"])
    writer.writerow([f'min value: {min(true_negative):0.02f}'])
    writer.writerow([f'max value: {max(true_negative):0.02f}'])
    writer.writerow([f'mean value: {mean(true_negative):0.02f}'])
    writer.writerow([f'stdev value: {stdev(true_negative):0.02f}'])
    writer.writerow('-----------------------------------')
    writer.writerow(["false positive:"])
    writer.writerow([f'min value: {min(false_positive):0.02f}'])
    writer.writerow([f'max value: {max(false_positive):0.02f}'])
    writer.writerow([f'mean value: {mean(false_positive):0.02f}'])
    writer.writerow([f'stdev value: {stdev(false_positive):0.02f}'])
    writer.writerow('-----------------------------------')
    writer.writerow(["false negative:"])
    writer.writerow([f'min value: {min(false_negative):0.02f}'])
    writer.writerow([f'max value: {max(false_negative):0.02f}'])
    writer.writerow([f'mean value: {mean(false_negative):0.02f}'])
    writer.writerow([f'stdev value: {stdev(false_negative):0.02f}'])
