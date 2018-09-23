import numpy as np
import pandas as pd
import re
import os

f = open('DatasetA_train_20180813/class_wordembeddings.txt')
class_wordembeddings = f.read()
class_wordembeddings = class_wordembeddings.split('\n')

g = open('DatasetA_train_20180813/label_list.txt')
label_list = (g.read()).split('\n')

h = open('DatasetA_train_20180813/train.txt')
train = (h.read()).split('\n')


class_attr_vectors = []
"""
class_attr_vectors (list)	: contains a dictionary for each class
dictionary attributes		: 'class', 'attribute-vector'
"""
for i in range(len(class_wordembeddings)):
	temp_dict = {}
	temp_list = class_wordembeddings[i].split(' ')
	temp_dict['class'] = temp_list[0]
	temp_dict['attribute-vector'] = [float(j) for j in temp_list[1:]]
	class_attr_vectors.append(temp_dict)

train_file_names = []
"""
train_file_names (list)	: contains a dictionary for each training image
dictionary attributes	: 'file-name', 'label'
"""
for i in range(len(train)):
	t, q = {}, train[i].split('\t')
	if q != ['']:
		t['file-name'] = q[0]
		t['label'] = q[1]
		train_file_names.append(t)

train_labels = [q['label'] for q in train_file_names]

list_of_indices_with_no_classes = [17, 20, 27, 33, 74, 112, 134, 136, 148, 155] # Obtained through an independent program
class_indices_all = list(set([i for i in range(1,241)]) - set(list_of_indices_with_no_classes))
class_indices_seen = np.sort(np.array([int(x[3:]) for x in list(set(train_labels))]))
class_indices_unseen = list(set(class_indices_all) - set(class_indices_seen))

print("Number of examples of all classes: ", len(class_indices_all))
print("Number of examples of seen (training) classes: ", len(class_indices_seen))
print("Number of examples of unseen (test) classes: ", len(class_indices_unseen))

train_images = []
"""
train_images (list)		: contains a dictionary coresponding to each class
dictionary attributes	: 'class-index', 'images'
"""