import random


def random_weights(dim):
    weights = [[0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if i < j:
                continue
            if i == j:
                weights[i][j] = 0
            else:
                if random.random() > 0.5:
                    weights[i][j] = random.randint(1, 15)
                    weights[j][i] = weights[i][j]
                else:
                    weights[i][j] = 1000000
                    weights[j][i] = 1000000
    return weights

if __name__ == "__main__":
    for weight in random_weights(10):
        print str(weight) + ','