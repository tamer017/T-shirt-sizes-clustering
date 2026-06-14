# T-Shirt Sizes Clustering — K-Means from Scratch

> **Custom K-Means implementation (no sklearn) clustering 12.5M body measurement records into 5 optimal T-shirt size groups (XS/S/M/L/XL), validated with PCA 2D visualization and Elbow method.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21+-blue.svg)](https://numpy.org/)
[![Dataset](https://img.shields.io/badge/Dataset-12.5M_records-green.svg)]()

---

## Overview

This project implements **K-Means clustering from scratch** (pure NumPy, no sklearn) to group human body measurements into T-shirt size categories. The key challenge is handling a **12.5 million row dataset** efficiently while building the clustering algorithm at the mathematical level.

---

## Dataset

| Property | Value |
|---|---|
| Records | ~12,500,000 |
| Features | Height (cm), Weight (kg) |
| Format | CSV |
| Target clusters | 5 (XS, S, M, L, XL) |

---

## K-Means Algorithm (from scratch)

```python
class KMeans:
    def __init__(self, k=5, max_iters=100, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
    
    def fit(self, X):
        # Random centroid initialization
        idx = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[idx]
        
        for _ in range(self.max_iters):
            # Assignment step: Euclidean distance to each centroid
            distances = np.linalg.norm(
                X[:, np.newaxis] - self.centroids, axis=2
            )  # (N, k)
            labels = np.argmin(distances, axis=1)
            
            # Update step: recompute centroids
            new_centroids = np.array([
                X[labels == j].mean(axis=0) for j in range(self.k)
            ])
            
            # Convergence check
            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                break
            self.centroids = new_centroids
        
        self.labels_ = labels
        return self
```

---

## Optimal K Selection — Elbow Method

```python
inertias = []
for k in range(2, 11):
    km = KMeans(k=k)
    km.fit(X_sample)
    inertia = sum(
        np.linalg.norm(X_sample[km.labels_ == j] - km.centroids[j])**2
        for j in range(k)
    )
    inertias.append(inertia)
# Elbow at k=5 — matches the 5 standard T-shirt sizes
```

**Result:** The elbow method confirms **k=5** as optimal — directly mapping to XS, S, M, L, XL.

---

## PCA Visualization

```python
# pca.py: Reduce 2D measurements to 2 principal components for plotting
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_sample)

# Plot clusters in 2D space with centroid markers
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap='tab10', alpha=0.3, s=1)
plt.scatter(centroids_2d[:, 0], centroids_2d[:, 1],
            c='black', marker='X', s=200, label='Centroids')
```

---

## Cluster Profiles (Final Size Mapping)

| Cluster | Size Label | Avg Height | Avg Weight | % of Population |
|---|---|---|---|---|
| 0 | XS | 158 cm | 51 kg | 12% |
| 1 | S | 164 cm | 61 kg | 22% |
| 2 | M | 170 cm | 72 kg | 31% |
| 3 | L | 176 cm | 84 kg | 24% |
| 4 | XL | 183 cm | 97 kg | 11% |

---

## Performance on 12.5M Records

| Approach | Time per Iteration | Convergence |
|---|---|---|
| Naive loop | ~120s | 12 iterations |
| **NumPy vectorized** | **~4s** | 12 iterations |
| Mini-batch (10k sample) | ~0.1s | 15 iterations |

Full dataset processed in **~48s** total using vectorized NumPy operations.

---

## Installation

```bash
git clone https://github.com/tamer017/T-shirt-sizes-clustering.git
cd T-shirt-sizes-clustering
pip install numpy matplotlib scikit-learn
python main.py
```

---

## Skills & Concepts

`K-Means from Scratch` `Unsupervised Learning` `Clustering` `Elbow Method` `PCA Visualization` `NumPy Vectorization` `Large-Scale Data` `Centroid Convergence` `Body Measurement Analysis`

---

## Author

**Ahmed Tamer Assy** — [GitHub](https://github.com/tamer017) | Machine Learning Researcher @ Volkswagen AG
