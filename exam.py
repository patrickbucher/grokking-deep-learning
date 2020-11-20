#!/usr/bin/env python3

import numpy as np

iq = np.array([98, 101, 93, 110, 95, 120, 89, 97, 127, 82])
lessons = np.array([27, 34, 37, 12, 40, 25, 38, 25, 12, 20])
studied = np.array([10, 12, 25, 32, 7, 33, 15, 5, 20, 60])

# real weights:  [0.5, 0.2, 0.3]
score = iq * 0.5 + lessons * 0.2 + studied * 0.3
print(score)

weights = np.array([1/3, 1/3, 1/3])
alpha = 0.0001

for i in range(int(1.0/alpha)):
    for j in range(len(score)):
        input = np.array([iq[j], lessons[j], studied[j]])
        goal = score[j]

        prediction = input.dot(weights)

        delta = goal - prediction
        error = delta ** 2
        weight_delta = input * delta

        weights += weight_delta * alpha

print(weights)
