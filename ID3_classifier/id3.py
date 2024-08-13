import random
from math import log
from copy import deepcopy


class TreeNode():
    def __init__(self, attribute, next_nodes):
        self.attribute = attribute
        self.attribute_values = {}
        self.next_nodes = next_nodes
        self.class_type = None


class Record():
    def __init__(self):
        self.class_type = None
        self.attributes = None


def main(file_name):
    records = read_data(file_name)
    class_values, attributes_values = find_attributes_values(records)
    training_data, testing_data = divide_data(records, 3/5)
    global_class = most_common_class(training_data)
    starting_node = TreeNode(None, id3(class_values, attributes_values, training_data))
    first_node = starting_node.next_nodes
    correct = 0
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    temporary = 0
    for data in testing_data:
        true_class = data.class_type
        current_node = first_node
        no_data = False
        while current_node.attribute_values:
            attr_num = current_node.attribute
            if data.attributes[attr_num] not in current_node.attribute_values.keys():
                no_data = True
                temporary += 1
                break
            current_node = current_node.attribute_values[data.attributes[attr_num]]
            data.attributes.pop(attr_num)

        if no_data:
            no_data = False
            answer = global_class
        else:
            answer = current_node.class_type

        if answer == true_class and answer == class_values[0]:
            true_positive += 1
            correct += 1
        elif answer == true_class and answer == class_values[1]:
            true_negative += 1
            correct += 1
        elif answer != true_class and answer == class_values[0]:
            false_positive += 1
        else:
            false_negative += 1


def id3(class_values: list, attributes_values: list, training_data: list) -> TreeNode:
    if training_data and one_value_remains(training_data):
        leaf_node = TreeNode(None, None)
        leaf_node.class_type = training_data[0].class_type
        return leaf_node
    if not attributes_values:
        leaf_node = TreeNode(None, None)
        leaf_node.class_type = most_common_class(training_data)
        return leaf_node
    d, subsets = max_inf_gain(class_values, attributes_values, training_data)

    node = TreeNode(d, None)
    new_attributes_values = deepcopy(attributes_values)
    new_attributes_values.pop(d)

    for set in subsets:
        if not set:
            continue
        value = set[0].attributes[d]
        for record in set:
            record.attributes.pop(d)
        node.attribute_values[value] = id3(class_values, new_attributes_values, set)
    return node


def max_inf_gain(classes, attributes, data):
    dataset_entropy = calculate_set_entropy(classes, data)
    best_attribute_inf_gain = float('-inf')
    best_attribute_index = float('-inf')
    subsets_of_best_attribute = []

    for i, attribute in enumerate(attributes):
        subsets = [[] for _ in range(len(attribute))]
        for record in data:
            for j, attribute_value in enumerate(attribute):
                if record.attributes[i] == attribute_value:
                    subsets[j].append(record)
                    break
        attr_inf = 0.0
        for set in subsets:
            if set:
                attr_inf += (len(set)/len(data))*log(len(set))
            else:
                attr_inf += 0
        inf_gain = dataset_entropy - attr_inf
        if inf_gain > best_attribute_inf_gain:
            best_attribute_inf_gain = inf_gain
            best_attribute_index = i
            subsets_of_best_attribute = subsets
    return best_attribute_index, subsets_of_best_attribute


def calculate_set_entropy(classes, data):
    set_entropy = 0.0
    data_len = len(data)
    classes_frequency = [0.0 for _ in range(len(classes))]
    for record in data:
        for index, c in enumerate(classes):
            if c == record.class_type:
                classes_frequency[index] += 1
                break
    for value in classes_frequency:
        set_entropy -= (value/data_len)*log(value/data_len)
    return set_entropy


def most_common_class(data):
    class_attributes = {}
    for record in data:
        if record.class_type in class_attributes.keys():
            class_attributes[record.class_type] += 1
        else:
            class_attributes[record.class_type] = 1
    return max(class_attributes, key=class_attributes.get)


def one_value_remains(data):
    class_values = []
    for record in data:
        if record.class_type in class_values:
            pass
        else:
            class_values.append(record.class_type)
    return len(class_values) == 1


def divide_data(data, ratio):
    first_list_len = int(len(data)*ratio)
    first_list = random.sample(data, first_list_len)
    second_list = [x for x in data if x not in first_list]
    return first_list, second_list


def find_attributes_values(records):
    attributes_values = [[] for _ in range(len(records[0].attributes))]
    class_values = []
    for record in records:
        for i in range(len(record.attributes)):
            if record.attributes[i] in attributes_values[i]:
                pass
            else:
                attributes_values[i].append(record.attributes[i])
        if record.class_type in class_values:
            pass
        else:
            class_values.append(record.class_type)
    return class_values, attributes_values


def read_data(file_name):
    records = []
    with open(file_name, 'r') as file:
        for row in file:
            striped_row = row.rstrip()
            record = striped_row.split(",")
            rec = Record()
            rec.class_type = record.pop(0)
            rec.attributes = record
            records.append(rec)
    return records


if __name__ == "__main__":
    # main('breast-cancer.data')
    main('agaricus-lepiota.data')
