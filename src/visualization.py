import numpy as np
import matplotlib.pyplot as plt
from persim import plot_diagrams


def plot_point_cloud(X, title="Point Cloud", color="steelblue", size=50):
    """
    Plot a 2D point cloud.
    
    Parameters
    ----------
    X : np.ndarray, shape (n_points, 2)
    title : str
    color : str
    size : int
    """
    plt.figure(figsize=(5, 5))
    plt.scatter(X[:, 0], X[:, 1], c=color, s=size)
    plt.title(title)
    plt.axis("equal")
    plt.show()


def plot_persistence(diagrams, title="Persistence Diagram"):
    """
    Plot a persistence diagram from Ripser output.

    Parameters
    ----------
    diagrams : list of np.ndarray
        Output of ripser(X)['dgms']
    title : str
    """
    plot_diagrams(diagrams, show=True, title=title)


def plot_betti_curves(diagrams, max_epsilon=2.0, n_bins=500, title="Betti Curves"):
    """
    Plot Betti curves beta_0 and beta_1 across the filtration.

    Parameters
    ----------
    diagrams : list of np.ndarray
        Output of ripser(X)['dgms']
    max_epsilon : float
    n_bins : int
    title : str
    """
    epsilons = np.linspace(0, max_epsilon, n_bins)

    def betti(diagram, epsilon):
        return np.sum((diagram[:, 0] <= epsilon) & (diagram[:, 1] > epsilon))

    beta_0 = [betti(diagrams[0], e) for e in epsilons]
    beta_1 = [betti(diagrams[1], e) for e in epsilons]

    plt.figure(figsize=(10, 4))
    plt.plot(epsilons, beta_0, label="$\\beta_0$", color="steelblue")
    plt.plot(epsilons, beta_1, label="$\\beta_1$", color="darkorange")
    plt.xlabel("$\\varepsilon$")
    plt.ylabel("Betti number")
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()