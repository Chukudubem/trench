import os
import sys

#If Location(ETL, Classifier, DataProcessor) != Current Location; do "sys.path.insert(0, <path/to/script>)"

from ETL import ETL
from Classifier import LogisticRegressor
from DataProcessor import DataProcessor as processor

#Pass argument to python script
pos_file = sys.argv[1]
neg_file = sys.argv[2]

#Load/Process Data
print("Loading Data...")
X_pos, y_pos = ETL().load_data(file_path=pos_file, label=1)
X_neg, y_neg = ETL().load_data(file_path=neg_file, label=0)
print("Done Loading data")

#Concatenate data
X_pos.extend(X_neg)
y_pos.extend(y_neg)

X = X_pos
y = y_pos


