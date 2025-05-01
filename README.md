# 🧪 Metric Integrity Auditor

A complete A/B test auditing suite built to detect misleading uplift, segment bias and insufficient sample size. This project simulates and analyzes 60K synthetic user interactions to flag flaws that could lead to false product decisions.

---

## 🔍 What This Project Covers

- Generate realistic A/B test data with built-in bias
- Analyze conversion patterns by group, device, region and time
- Detect false positives, power issues and unreliable cohorts
- Visualize insights through two interactive Tableau dashboards

---

## 📊 Dashboards (View on Tableau Public)

📍 **View both dashboards here:**  
🔗 [Akanksha Ashokrao Bable's Tableau Public – Metric Integrity Auditor Series](https://public.tableau.com/app/profile/akanksha.bable2555/vizzes)

- **Core Dashboard:** Conversion rate, uplift trend, device and region breakdown  
- **Advanced Analysis:** Cohort matrix, segment risk heatmap, false positive zone

---

## 📁 Folder Structure

```plaintext
metric_integrity_auditor/
├── data/
│   └── simulated_ab_test_data.csv        # 60,000-row synthetic A/B test data
├── notebooks/
│   └── exploratory_data_analysis.ipynb   # EDA & A/B test validation logic
├── scripts/
│   └── data_generator.py                 # Code to create the flawed dataset
└── .gitignore
