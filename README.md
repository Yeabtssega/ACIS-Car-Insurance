# ACIS Car Insurance Risk & Rating Analysis

**Prepared by Yeabtsega Tilahun**  
**Date:** June 2025  

---

## 🚗 Overview

**ACIS** (AlphaCare Insurance Solutions) project aims to explore and predict car insurance risk and rating through data-driven analysis. This repo covers:

- **Task 1: Exploratory Data Analysis (EDA)**  
  Understanding dataset structure, cleaning, and visualizing key insights.

- **Task 2: Data Versioning with DVC and Git LFS**  
  Managing large cleaned datasets efficiently for reproducibility.

- **Task 3: Predictive Modeling (Upcoming)**  
  Build and evaluate a model to estimate insurance risk score.

---

## ✅ Task 1: EDA Highlights

- **Dataset:** `historical_claims.csv` – 616,314 rows and 52 columns.  
- **Cleaning Steps:** Dropped fully null columns (`CrossBorder`, `NumberOfVehiclesInFleet`), resolved missing values in others.  
- **Outputs:**  
  - `cleaned_data_task1.csv` – Cleaned dataset (Git LFS tracked).  
  - `task1_eda.py` – Script includes:
    - Data loading, null-checks, descriptive stats.
    - Visuals:  
      ![Premium vs Claims Histogram](premium_claims_histograms.png)  
    - Top banks by policy volume:  
      ![Top Banks Bar Plot](top10_banks.png)
  - `eda_output.txt` – Command-line summary log.

---

## ✅ Task 2: Data Versioning

- Tracked large data files with Git LFS; see `.gitattributes`.
- Maintained clean commit history:
  - “Track large files with Git LFS”
  - “Complete Task 1: EDA with visualizations and output summary”
- Branches:
  - `main` – Task 1 files
  - `task-2` – Includes Versioned large files and setup

---

## 📚 Requirements

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
dvc
