# README: CS 549 Final Project
### Everett Richards, AJ Gabriel, Talia Goody

## Navigating the Project Directory
### Scripts and Files
* `download_dataset.sh`: Bash script to download the Kaggle dataset
* `malicious_phish.csv`: The Kaggle dataset, in CSV form
* `process_dataset.py`: Python script to transform the dataset into a featurized embedding + do PCA. Used for LogReg and KNN, but not for RNN.
### Model Notebooks
* `LogReg.ipynb`: Logistic Regression implementation, experiments, visualization, and results (Everett)
* `RNN.ipynb`: Recurrent Neural Network (RNN) implementation, experiments, visualization, and results (AJ)
* `KNN.ipynb`: K-Nearest Neighbors (KNN) implementation, experiments, visualization, and results (Talia)
### Documentation
* `ProjectReport.pdf`: Final project report.
* `README.md`: This "Read Me" file! :)

## Instructions
### Environment Requirements
* Modern CPU and operating system. Unix-based OS is preferred
* Recent Python installation with `pip` to install packages and `ipykernel` to run Notebooks
### Executing Code
* For each of the three models `{LogReg,RNN,KNN}.ipynb`, simply navigate to the notebook and click "Run All"
* If you are missing any packages, and the `pip install` section does not automatically install them, please install the missing packages before proceeding