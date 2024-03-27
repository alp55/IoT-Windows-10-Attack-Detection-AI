# IoT Windows 10 Attack Detection AI

## Description
This artificial intelligence system performs network traffic analysis on IoT (Internet of Things) devices running the Windows 10 operating system. It monitors network traffic using the IoT_windows_10 dataset, identifies attack types, and classifies whether these attacks are malicious or benign. It particularly focuses on detecting potential attacks targeting IoT devices.

## Usage
According to this dataset, a classification process has been conducted using the following models:

Logistic Regression
Support Vector Machine (SVM)
CatBoost
LightGBM
The steps involved in the training process are as follows:

Data Loading and Preprocessing:

The dataset was loaded using the Pandas library and converted into a DataFrame.
String values within the dataset were converted into numerical values.
The correlation between the 'label' column and other columns was analyzed to assess their relationship.
Feature Selection:

Based on the correlation analysis, columns with no significant correlation with the 'label' column were removed.
A new DataFrame was created using the selected features and the 'label' column.
Data Splitting:

The dataset was divided into training and testing sets using the train_test_split function.
Model Training:

Different classification models, including Logistic Regression, Support Vector Machine, CatBoost, and LightGBM, were trained on the training set.
Each model was trained on the training set and evaluated on the test set.
Model Evaluation:

The performance of each model was evaluated using metrics such as accuracy, precision, and recall.
Additionally, confusion matrices were plotted to visualize the decision boundaries of each model.
Following these steps, the performance of each model was assessed, and the results were reported.

existing Git repository with the following command:

```
cd existing_repo
git remote add origin http://gitlab.koddeposu.gov.tr/alperen-uluta-sanem-sakarya-ortak-proje/iot-windows-10-attack-detection.git
git branch -M main
git push -uf origin main
```


## Support

email: alperenulutas1@gmail.com , email: sanemsakarya45@gmail.com

## Roadmap

Here are the planned features and improvements to be added to the project in the future:

Training the model with a more extensive dataset covering a wider range of attack types, aiming to enhance the model's capability to detect various attacks comprehensively.

Focusing on specialized training data to improve the model's ability to recognize specific attack types commonly observed in IoT devices.

Developing and integrating a suitable infrastructure to enable the model to operate in real-time, allowing for timely detection and response to potential threats.


## referance

[1] Kalutharage, C. S., Liu, X., Chrysoulas, C., Pitropakis, N., & Papadopoulos, P. (2023). Explainable AI-based DDOS attack identification method for IoT networks. Computers, 12(2), 32.
