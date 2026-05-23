import numpy as np
from ripser import ripser
import gudhi
from gtda.homology import VietorisRipsPersistence


def compute_persistence_ripser(X):
    """
    Compute persistent homology using Ripser.

    Parameters
    ----------
    X : np.ndarray, shape (n_points, n_dimensions)

    Returns
    -------
    diagrams : list of np.ndarray
        Birth-death pairs for each homology dimension
    """
    return ripser(X)['dgms']


def compute_persistence_gudhi(X, max_edge_length=2.0, max_dimension=2):
    """
    Compute persistent homology using GUDHI.

    Parameters
    ----------
    X : np.ndarray, shape (n_points, n_dimensions)
    max_edge_length : float
    max_dimension : int

    Returns
    -------
    persistence : list of tuples (dimension, (birth, death))
    """
    rips = gudhi.RipsComplex(points=X, max_edge_length=max_edge_length)
    simplex_tree = rips.create_simplex_tree(max_dimension=max_dimension)
    simplex_tree.compute_persistence()
    return simplex_tree.persistence()


def compute_persistence_giotto(X, homology_dimensions=[0, 1]):
    """
    Compute persistent homology using Giotto-TDA.

    Parameters
    ----------
    X : np.ndarray, shape (n_points, n_dimensions)
    homology_dimensions : list of int

    Returns
    -------
    diagrams : np.ndarray, shape (1, n_features, 3)
    """
    VR = VietorisRipsPersistence(homology_dimensions=homology_dimensions)
    X_gtda = X.reshape(1, *X.shape)
    return VR.fit_transform(X_gtda)