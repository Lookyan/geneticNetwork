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


def pretty_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) + ',' for x in lens)
    table = ['[ ' + fmt.format(*row) + ' ],' for row in s]
    print '\n'.join(table)

if __name__ == "__main__":
    # for weight in random_weights(10):
    #     print str(weight) + ','
    pretty_matrix(random_weights(10))