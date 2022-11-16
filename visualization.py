from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

def make_2d_pca(x):
    pca = PCA(n_components=2, svd_solver='full').fit_transform(x)
    return x

def compare_embeddings(x, y):
    plt.scatter(x[:, 0], x[:, 1])
    plt.scatter(y[:, 0], y[:, 1])

def get_nn(x, k):
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(x)
    return nbrs

def visualize_nearest_neighbors(nbrs, x, idx):
    distances, indices = nbrs.kneighbors(x[idx].reshape(1, -1))

    embed = make_2d_pca(x)

    plt.scatter(embed[:, 0], embed[:, 1])
    plt.scatter(embed[indices[0][0], 0], embed[indices[0][0], 1], color='g', label="Target Point")
    plt.scatter(embed[[i for i in indices[0][1:]], 0], embed[[i for i in indices[0][1:]], 1], color='r', label="Nearest Neighbors")
    plt.legend()

# def compare_nearest_neighbors(nbrs, x, idx):
#     distances, indices = nbrs.kneighbors(x[idx].reshape(1, -1))
