# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    weight = 0
    # Get list of values per unit weight
    val_per_wgt = []
    for i in range(len(weights)):
        val_per_wgt.append(values[i] / weights[i])

    while val_per_wgt:
        i = val_per_wgt.index(max(val_per_wgt))

        # Continue until item completely taken or full capacity
        while weights[i] > 0 and weight < capacity:
            weights[i] -= 1
            weight += 1
            value += val_per_wgt[i]

        del val_per_wgt[i]
        del weights[i]
        del values[i]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
