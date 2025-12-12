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

Note on RNN:
The "RNN.ipynb" file runs a Recurrent Neural Network model, heavily inspired by a similar model in Assignment 4.
The model itself runs by randomly choosing rows (with replacement) from the dataset in "malicious_phish.csv".
In order to run this notebook properly, you must run every code block from top to bottom. There will be comments specifying what you can and cannot change.
Once the last code block is finished running, you should be able to see the evaluations of the metrics and loss that the model developed! Furthermore, as a way to further reproduce the results, you can see the saved results of the evaluation metrics and loss values over time in the pickle files "rnn_results.pkl" and "rnn_results_2.pkl".

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

## GitHub Repository
https://github.com/EverettRichards/CS549-Project