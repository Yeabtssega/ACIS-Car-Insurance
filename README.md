# AlphaCare Insurance Solutions (ACIS)

## 📊 Car Insurance Claim Risk Analytics Project  
Prepared by **Yeabtsega Tilahun**  
June 2025

---

## ✅ Task 1: Exploratory Data Analysis (EDA)

### Objective  
Analyze historical South African car insurance claim data to discover patterns, clean missing data, and generate actionable insights for ACIS marketing and pricing teams.

### Dataset Summary  
- **Size:** 616,314 rows × 52 columns  
- **Features:** Policy, premium, claim, region, bank info, and vehicle data  
- **Missing Value Handling:**
  - Dropped columns with 100% nulls (`CrossBorder`, `NumberOfVehiclesInFleet`)
  - Cleaned key features (`Bank`, `AccountType`, `CustomValueEstimate`, etc.)

### Key Statistics
| Column                  | Mean     | Std Dev | Min   | Max     |
|-------------------------|----------|---------|-------|---------|
| Total Premium           | 62.17    | 156.81  | 0.00  | 18,000+ |
| Total Claims            | 64.21    | 2,335.88| 0.00  | 950,000+ |
| CalculatedPremiumPerTerm| 116.10   | 218.50  | -60   | 2,000+  |

### Visualizations
- ✅ **`premium_claims_histograms.png`** – Distribution of Total Premium vs Claims  
- ✅ **`top10_banks.png`** – Top 10 banks by number of insurance policies

### Outputs
- `cleaned_data_task1.csv`: Cleaned version of the original dataset
- `task1_eda_output.txt`: EDA report summary
- `task1_eda.py`: Python script for loading, cleaning, and analyzing data

---

## 📈 Task 2: Git, Git LFS & Version Control

### Objectives  
Set up robust version control for handling large files and tracking analytics results.

### Implementation
- Initialized Git repository in `ACIS-Car-Insurance-EDA`
- Added remote: [Yeabtssega/ACIS-Car-Insurance](https://github.com/Yeabtssega/ACIS-Car-Insurance)
- Configured **Git LFS** to track:
  - `cleaned_MachineLearningRating.csv`
  - `task1_eda_output.txt`
  - `eda_output.txt`

### Outputs
- `.gitattributes`: Git LFS configuration
- Large files properly pushed using Git LFS
- Branches used:
  - `main`: Final version
  - `task-2`: LFS integration and task deliverables

---

## ✅ Submission Checklist

| Task            | Status       |
|-----------------|--------------|
| Task 1 - EDA    | ✅ Completed |
| Task 2 - Git/LFS| ✅ Completed |
| README Updated  | ✅ Yes       |
| GitHub Repo     | ✅ [View Here](https://github.com/Yeabtssega/ACIS-Car-Insurance) |

---

## 🔖 Notes
- All large files tracked and pushed successfully with Git LFS.
- Final submission meets ACIS documentation and data standards.

