#!/usr/bin/env python3

import numpy as np

investments = np.array([11_324.92, 29_876.21, 54_271.28, 101_987.9, 1_207_674.2])
returns = investments * 1.0037  # 0.37% return (to be figured out)

alpha = 1e-15
weight = 1.00  # initial guess: no yield

finished = False
for i in range(1000000):
    for j in range(len(investments)):
        goal = returns[j]
        input = investments[j]
        prediction = input * weight
        delta = goal - prediction
        error = delta ** 2
        directed_error = delta * input
        adjustment = directed_error * alpha
        if abs(adjustment) < 1e-18:
            finished = True
            break
        weight += adjustment
    if finished:
        print(f'finished after {i+1} iterations')
        break

print('found weight', weight)
