from sklearn.neighbors import NearestNeighbors

# OOP probably makes more sense here
# if computing kNN twice is computationally prohibitive, rewrite this

def jaccard(x, y):
    s1 = set(x)
    s2 = set(y)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def lns(idx, X, Y):
    nbrs_x = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(X)
    nbrs_y = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(Y)

    _, idxs_x = nbrs_x.kneighbors(X[idx].reshape(1, -1))
    _, idxs_y = nbrs_y.kneighbors(Y[idx].reshape(1, -1))

    return jaccard(idxs_x[0].tolist()[1:], idxs_y[0].tolist()[1:])

def all_lns(n, X, Y):
    lns_list = []
    for i in range(n):
        lns_list.append(lns(i, X, Y))
    return lns_list
