import os
import sys

#If Location(ETL, Classifier, DataProcessor) != Current Location; do "sys.path.insert(0, <path/to/script>)"
import pandas as pd
from ETL import ETL
from Classifier import LogisticRegressor
from DataProcessor import DataProcessor as processor

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Pass argument to python script
pos_file = sys.argv[1]
neg_file = sys.argv[2]

#Load/Process Data
print("Loading Data...")
ETL().load_data(file_path=pos_file, label=1) # Load, process, and save to file
ETL().load_data(file_path=neg_file, label=0) # Load, process, and save to file
print("Done Loading data")

df = pd.read_csv('pos_neg_output.txt')

X = df.drop([df.columns[-1]], axis=1)
y = df[df.columns[-1]]



#Prepare data
print("Preparing data for model...")
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.15,
                                                    random_state=42,
                                                    stratify=y)

#Model data
lr = LogisticRegressor()


print("Training data...")
lr.train(X_train.iloc[:,:-1], y_train) 

#lr_model = dump(lr, 'lr_trench_best_param.joblib') To save the model weights

#Test model
#lr = load('lr_trench_best_param.joblib') Uncomment to predict validation set
pred = lr.test(X_test.iloc[:,:-1])

#Evaluate model

print('='*20)
print('Model Evaluation')
print(f'Accuracy: {accuracy_score(y_test, pred)}')
print('='*20)
print(classification_report(y_test, pred))
print('='*20)
print(confusion_matrix(y_test, pred))





