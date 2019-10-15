# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:18:18 2019

@author: dubem
"""
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


class LogisticRegressor:
    def __init__(self, standardize = True, C = 1e5):
        self.standardize = standardize
        self.C = C
        self.non_zero_params = []
    
    def train(self, X, y):
        X = np.array(X)
        if self.standardize:
            self.scaler = StandardScaler()
            X = self.scaler.fit_transform(X)
        
        self.lr = LogisticRegression(penalty='l1')
        self.lr.fit(X,y)
        
    def test(self, X):
        X = np.array(X)
        if self.standardize:
            X = self.scaler.transform(X)
        
        return self.lr.predict(X)
    
    def get_params(self):
        return self.lr.coef_, self.lr.intercept_
    
    
    def get_n_nonzero_params(self):
        c = 0 
        for x in self.lr.coef_[0]:
            if x != 0.0:
                c+=1
        return c