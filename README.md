# TDA Foundations
### Topological Data Analysis — Core Concepts & Implementation

> An exploration of TDA fundamentals — building intuition for topology through code.

---

## 📌 What This Repo Is

This repo covers the mathematical and computational foundations of TDA — before any application is introduced. Everything built here becomes the toolbox for future projects.

---

## 🧠 Topics Covered

| Topic | Description |
|-------|-------------|
| Point Clouds | Building and visualizing point clouds from raw data |
| Simplicial Complexes | Constructing Vietoris-Rips and Čech complexes |
| Persistent Homology | Computing H0 (connected components) and H1 (loops) |
| Persistence Diagrams | Reading and interpreting birth-death diagrams |
| Barcodes | Visualizing topological feature lifespans |
| Betti Numbers | Counting topological features at each scale |

---

## 📁 Repository Structure

```
tda-foundations/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_point_clouds.ipynb
│   ├── 02_simplicial_complexes.ipynb
│   ├── 03_persistent_homology.ipynb
│   └── 04_barcodes_and_diagrams.ipynb
├── src/
│   ├── __init__.py
│   ├── complexes.py
│   ├── homology.py
│   └── visualization.py
├── data/
│   └── sample_clouds/
└── tests/
    └── test_homology.py
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/TDA-Gabo/tda-foundations.git
cd tda-foundations

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 📦 Dependencies

```
numpy
pandas
matplotlib
scipy
ripser
persim
giotto-tda
jupyter
```
---

## 🚀 Quick Start
← here we show 10 lines of Python that anyone can copy, run, and see a result

```python
import numpy as np
from ripser import ripser
from persim import plot_diagrams

# Create a noisy circle
theta = np.linspace(0, 2 * np.pi, 100)
X = np.column_stack([np.cos(theta), np.sin(theta)])
X += np.random.normal(0, 0.1, X.shape)

# Compute persistent homology
diagrams = ripser(X)['dgms']

# Visualize — expect H1 (loop) to persist
plot_diagrams(diagrams, show=True)
```

---

## 🗺️ Roadmap

- [ ] Notebook 01: Point clouds & distance matrices
- [ ] Notebook 02: Simplicial complexes
- [ ] Notebook 03: Persistent homology with Ripser
- [ ] Notebook 04: Barcodes, diagrams, and Betti curves
- [ ] src/ module wrappers

---

## 📚 References

- Edelsbrunner & Harer — *Computational Topology: An Introduction*
- Carlsson (2009) — *Topology and Data*, Bulletin of the AMS
- [Ripser documentation](https://ripser.scikit-tda.org/)
- [Giotto-TDA documentation](https://giotto-ai.github.io/gtda-docs/)

---

## 👤 Author

**TDA-Gabo**
*You can't always imagine the data, but you can always describe its shape.*
