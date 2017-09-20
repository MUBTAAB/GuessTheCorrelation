# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:44:40 2017

@author: mucs_b
"""

import random
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

lives = 3
Score = 0
while lives > 0:
    x = np.random.normal(0,random.randint(0,200),random.randint(10,500))
    dev = random.randint(0,300)
    y = [i+np.random.normal(0,dev) for i in x]
    df = pd.DataFrame({'x':x,'y':y})
    sns.jointplot('x', 'y', df, kind='reg',stat_func = None,
              joint_kws={'line_kws':{'color':'red'}})
    plt.show()
    corr = np.corrcoef(x,y)[0][1]
    while True:
        try:
            uinput = float(input('Guess the correlation? '))
            break
        except ValueError:
            print('Input must be float!')
            
    if abs(corr-uinput) > 0.05:
        lives -= 1
        print('False! Correlation: '+ str(corr) +' Lives: ' + str(lives))
    elif abs(corr-uinput) < 0.01:
        lives  += 1
        Score += 5
        print('Preciseley! Correlation: '+ str(corr) +' Live gained! Lives: ' + str(lives) +' Score: ' + str(Score))    
    else:
        Score += 1
        print('True! Correlation: '+ str(corr) +' Score: ' + str(Score))
        
print('Game over! Score: '+ str(Score))

