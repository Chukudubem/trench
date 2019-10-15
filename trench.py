import os
import sys
from ETL import ETL
from Classifier import LogisticRegressor
from DataProcessor import DataProcessor as processor

sys.path.insert(0, '/mnt/hgfs/medium/scripts/')

output_file = sys.argv[1]

X_pos, _ = ETL().load_data(file_path=output_file, label=1)
print(len(X_pos))
