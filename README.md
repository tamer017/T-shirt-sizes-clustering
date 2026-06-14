# T-Shirt Sizes Clustering — K-Means + PCA

> An unsupervised machine learning system that automatically determines optimal T-shirt size categories from customer body measurements using K-Means clustering and PCA dimensionality reduction.

[![Language](https://img.shields.io/badge/Language-Python%203.x-blue?style=flat-square)](https://www.python.org/)
[![Domain](https://img.shields.io/badge/Domain-Unsupervised%20Learning-teal?style=flat-square)]()
[![Algorithm](https://img.shields.io/badge/Algorithm-K--Means%20%2B%20PCA-orange?style=flat-square)]()

---

## Overview

A manufacturing company needs to determine the right T-shirt size distribution for production. Instead of relying on arbitrary fixed size definitions, this project uses **K-Means clustering** to group N customers into K optimal size categories based on 5 body measurement features — minimizing waste and maximizing fit accuracy across the customer population.

**Principal Component Analysis (PCA)** is applied to reduce the 5 correlated body features to 2 principal components (preserving ~95% variance), enabling 2D visualization of cluster structure and dramatically improving K-Means convergence speed.

---

## Problem Statement

Given N customer body measurements (an N×5 matrix), cluster customers into K groups to define K manufacturing size categories:

| K Value | Size Categories |
|---|---|
| K = 3 | Small (S), Medium (M), Large (L) |
| K = 5 | XS, S, M, L, XL |
| K = 7 | XXS, XS, S, M, L, XL, XXL |

---

## Features

Each customer is described by 5 body measurement features:

| Feature | Description |
|---|---|
| Height | Total body height (cm) |
| Weight | Body weight (kg) |
| BMI | Body Mass Index (kg/m²) |
| Shoulder width | Distance between shoulder joints (cm) |
| Arm length | Length from shoulder to wrist (cm) |

> **Note:** BMI exhibits high correlation with Height and Weight (redundancy), making it a prime candidate for PCA reduction.

---

## Methodology

### Step 1: Data Normalization
All 5 features are standardized using **Z-score normalization** to ensure equal contribution regardless of scale differences (cm vs. kg):
```
x_norm = (x - μ) / σ
```

### Step 2: PCA Dimensionality Reduction
- **Principal Component Analysis** compresses 5D feature space → 2D
- Retains ~95% of total variance in just 2 components
- PC1 predominantly captures overall body size; PC2 captures body shape ratio
- Enables 2D scatter plot visualization of cluster boundaries

### Step 3: K-Means Clustering
- K-Means applied on PCA-reduced 2D features
- **Elbow method** used to justify K selection (K=5 optimal for this dataset)
- Cluster centroids in PCA space mapped back to original feature space for interpretability
- Running time vs. N samples benchmarked to confirm O(N·K·I) complexity

### Step 4: Results Analysis

**Cluster distribution for K=5:**

| Cluster (Size) | Color Code | % of Population |
|---|---|---|
| XS | Green | 16.95% |
| S | Cyan | 17.79% |
| M | Magenta | 21.61% |
| L | Orange | 24.73% |
| XL | Black | 18.93% |

The distribution reveals a slightly right-skewed size distribution — L is the most common size, consistent with typical population body measurement distributions.

---

## Project Structure

```
T-shirt-sizes-clustering/
├── main.py          # K-Means clustering + running time vs N plot
├── main2.py         # Cluster percentage distribution visualization
├── data/
│   └── measurements.csv  # Customer body measurement dataset
├── figures/
│   ├── Figure_1.png    # Cluster percentage pie chart
│   └── Figure_2.png    # Running time vs N samples
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/tamer017/T-shirt-sizes-clustering.git
cd T-shirt-sizes-clustering
pip install numpy pandas matplotlib scikit-learn

# Run K-Means clustering + timing benchmark
python main.py   # Set K=5 inside the script

# Run cluster distribution analysis
python main2.py
```

---

## Key Takeaways

- PCA with 2 components preserves ~95% variance while enabling human-interpretable 2D visualization
- K-Means runtime scales linearly with N — confirmed by the running time benchmark plot
- Clustering-based size segmentation produces more balanced size distributions than fixed industry standards
- BMI redundancy with Height/Weight is captured by PCA, preventing over-weighting of correlated features

---

## Skills Demonstrated

`Unsupervised Learning` `K-Means Clustering` `PCA` `Dimensionality Reduction` `Feature Normalization` `Retail Analytics` `Python` `Scikit-learn` `NumPy` `Matplotlib`
