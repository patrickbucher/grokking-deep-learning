#!/usr/bin/env python3

def elementwise_multiplication(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)

    vec_c = []
    for i in range(len(vec_a)):
        vec_c.append(vec_a[i] * vec_b[i])

    return vec_c


def elementwise_addition(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)

    vec_c = []
    for i in range(len(vec_a)):
        vec_c.append(vec_a[i] + vec_b[i])

    return vec_c


def vector_sum(vec_a):
    v_sum = 0.0

    for x in vec_a:
        v_sum += x

    return v_sum


def vector_average(vec_a):
    return vector_sum(vec_a) / len(vec_a)


if __name__ == '__main__':
    a = [13.0, 12.5, 9.7, 3.3]
    b = [11.2, 8.9, 11.9, 5.8]

    print('multiplication:', elementwise_multiplication(a, b))
    print('addition:', elementwise_addition(a, b))
    print('sum a:', vector_sum(a))
    print('sum b:', vector_sum(b))
    print('avg a:', vector_average(a))
    print('avg b:', vector_average(b))

    dot_prod = vector_sum(elementwise_multiplication(a, b))
    print('a dot b:', dot_prod)
