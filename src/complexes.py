import numpy as np
from itertools import combinations


def euclidean_distance(p1, p2):
    """
    Compute Euclidean distance between two points.

    Parameters
    ----------
    p1 : np.ndarray
    p2 : np.ndarray

    Returns
    -------
    distance : float
    """
    return np.sqrt(np.sum((p1 - p2) ** 2))


def vietoris_rips_edges(points, epsilon):
    """
    Compute edges of the Vietoris-Rips complex at scale epsilon.

    Parameters
    ----------
    points : np.ndarray, shape (n_points, n_dimensions)
    epsilon : float

    Returns
    -------
    edges : list of tuples (i, j)
    """
    return [
        (i, j)
        for i, j in combinations(range(len(points)), 2)
        if euclidean_distance(points[i], points[j]) < epsilon
    ]


def vietoris_rips_triangles(points, epsilon):
    """
    Compute 2-simplices of the Vietoris-Rips complex at scale epsilon.

    Parameters
    ----------
    points : np.ndarray, shape (n_points, n_dimensions)
    epsilon : float

    Returns
    -------
    triangles : list of tuples (i, j, k)
    """
    return [
        (i, j, k)
        for i, j, k in combinations(range(len(points)), 3)
        if all(
            euclidean_distance(points[a], points[b]) < epsilon
            for a, b in combinations([i, j, k], 2)
        )
    ]


def vietoris_rips_complex(points, epsilon):
    """
    Compute the full Vietoris-Rips complex at scale epsilon.

    Parameters
    ----------
    points : np.ndarray, shape (n_points, n_dimensions)
    epsilon : float

    Returns
    -------
    edges : list of tuples (i, j)
    triangles : list of tuples (i, j, k)
    """
    edges = vietoris_rips_edges(points, epsilon)
    triangles = vietoris_rips_triangles(points, epsilon)
    return edges, triangles