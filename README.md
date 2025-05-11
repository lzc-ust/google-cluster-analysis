# Google Cluster Analysis

A comprehensive EDA and predictive analysis project using the Google Borg Cluster Trace dataset.

## 📁 Project Structure

```
├── data/                          
│   └── cleaned_borg_data.parquet
├── notebooks/                     
│   ├── 01_data_overview_basic_cleaning.ipynb
│   ├── 02_queueing_delay_analysis.ipynb
│   ├── 03_high_low_efficiency_analysis.ipynb
│   ├── 04_resource_efficiency_cluster.ipynb
│   └── 05_failure_prediction_and_clustering.ipynb
├── src/                           
│   └── feature_engineering.py
├── README.md                      
├── requirements.txt               
├── .gitignore                     
```

## 👥 Team Members

- **LI, Zhicheng** - 21133094 - zlijw@connect.ust.hk
- **WANG, Ziling** - 21086760 - zwanglm@connect.ust.hk
- **YANG, Zhuorui** - 21095046 - zyangdm@connect.ust.hk

## 📌 Contributions

- **LI, Zhicheng:** Feature engineering pipeline, model evaluation, clustering analysis
- **WANG, Ziling:** EDA visualizations, queueing delay and efficiency investigations
- **YANG, Zhuorui:** Resource request extraction, binary classification analysis

## 📊 How to Run

1. Place the raw Google trace files in the `data/` directory.  
   📦 **Note:** Due to GitHub's file size limitation (max 100MB), the raw file `borg_traces_data.csv` (313MB) is not included in the repository.  
   👉 Please manually download it from Kaggle:  
   https://www.kaggle.com/datasets/derrickmwiti/google-2019-cluster-sample  
   Then place it under the `data/` directory.

2. Run the notebook `01_data_overview_basic_cleaning.ipynb` to generate cleaned Parquet data (calls `src/feature_engineering.py` internally).

3. Explore the analysis notebooks in `notebooks/`.

4. Execute `05_failure_prediction_and_clustering.ipynb` for modeling and ROC analysis.

## ✅ Environment Setup

```bash
conda create -n cluster-analysis python=3.10
conda activate cluster-analysis
pip install -r requirements.txt
```