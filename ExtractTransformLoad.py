#!/usr/bin/env python
# coding: utf-8

import os
from DataProcessor import DataProcessor as processor


class ETL:
    def __init__(self, pos_dir, neg_dir):
        
        self.data = []
        self.labels = []
        
        if neg_dir != None:
            self.load_data(neg_dir, 0)
        if pos_dir != None:
            self.load_data(pos_dir, 1)
            
    def load_data(self, file_path, label):
        files = os.listdir(file_path)
        n_files = 0
        for file in files:
            try:
                data_processor = processor(file_path + file)
                n_files += 1
            except:
                print(f'Error: Failed to parse {file_path + file}')
                
            tmpTLS = data_processor.getTLSInfo()
            tmpBD = data_processor.getByteDistribution()
            tmpIPT = data_processor.getIndividualFlowIPTs()
            tmpPL = data_processor.getIndividualFlowPcktLengths()
            tmpMTD = data_processor.getIndividualFlowMetadata()
            
            if tmpMTD != None and tmpPL != None and tmpIPT != None:
            #if all([tmpMTD != 0, tmpPL != None, tmpIPT != None]):
                for i in range(len(tmpMTD)):
                    tmp_data = []
                
                    tmp_data.extend(tmpTLS[i])
                    tmp_data.extend(tmpBD[i])
                    tmp_data.extend(tmpIPT[i])
                    tmp_data.extend(tmpPL[i])
                    tmp_data.extend(tmpMTD[i])
                    
                    
                    self.data.append(tmp_data)
                    self.labels.append(label)
    
        print("completed processing")

