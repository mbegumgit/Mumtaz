# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:42:11 2021

@author: User
"""

ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]
import numpy as np
ages_mean=np.mean(ages)
print(ages_mean)
## Lets take sample

sample_size=10
age_sample=np.random.choice(ages,sample_size)

# One Sample T-test
# 30 is the mean value of the population
from scipy.stats import ttest_1samp
ttest,p_value=ttest_1samp(age_sample,30)
print(p_value)

if p_value < 0.05:    # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")