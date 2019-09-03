import numpy as np


def find_best_score(pre_max, fut_mat):
    row = fut_mat.shape[0]
    col = fut_mat.shape[1]
    best_score = np.zeros(row)
    for i in range(row):
        for j in range(col):
            if fut_mat[i][j] > pre_max[i]:
                best_score[i] = fut_mat[i][j]
                continue
    return np.mean(best_score)


total_num = 1000
skip_per = [i for i in range(total_num) if i > 0]
test_num = 500

for i in skip_per:
    score = np.random.randn(test_num, total_num)
    skip_set = score[:, :i]
    skip_max = np.max(skip_set, 1)
    test_set = score[:, i:]
    print(i, find_best_score(skip_max, test_set))
