#!/usr/bin/env python3

weight = 0.0
goal_pred = 0.8
input = 1.1

for i in range(4):
    print(f'weight: {weight:.3f}')
    pred = input * weight
    delta = goal_pred - pred
    error = delta ** 2
    weight_delta = delta * input
    weight += weight_delta
    print(f'error: {error:.3f}, prediction: {pred:.3f}')
    print(f'delta: {delta:.3f}, weight delta: {weight_delta:.3f}')
    print(8*'-')
