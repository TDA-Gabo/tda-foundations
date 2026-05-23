import numpy as np
from persim import bottleneck
from gtda.diagrams import PersistenceLandscape, PersistenceEntropy


def compute_landscapes(diagrams_gtda, n_layers=2, n_bins=100):
    """
    Compute persistence landscapes from Giotto-TDA diagrams.

    Parameters
    ----------
    diagrams_gtda : np.ndarray, shape (n_samples, n_features, 3)
    n_layers : int
    n_bins : int

    Returns
    -------
    landscapes : np.ndarray
    """
    PL = PersistenceLandscape(n_layers=n_layers, n_bins=n_bins)
    return PL.fit_transform(diagrams_gtda)


def compute_entropy(diagrams_gtda):
    """
    Compute persistence entropy from Giotto-TDA diagrams.

    Parameters
    ----------
    diagrams_gtda : np.ndarray, shape (n_samples, n_features, 3)

    Returns
    -------
    entropies : np.ndarray, shape (n_samples, n_homology_dimensions)
    """
    PE = PersistenceEntropy()
    return PE.fit_transform(diagrams_gtda)


def compute_bottleneck(diagram1, diagram2):
    """
    Compute bottleneck distance between two persistence diagrams.

    Parameters
    ----------
    diagram1 : np.ndarray, shape (n_features, 2)
        Birth-death pairs from ripser output
    diagram2 : np.ndarray, shape (n_features, 2)

    Returns
    -------
    distance : float
    """
    return bottleneck(diagram1, diagram2)