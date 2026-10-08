#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:06:28 2026

@author: wrennicol
"""
#############################################################
#                                                           #
#             First we enter the data                       #
#                                                           #
#############################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

arm_pos = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1]
vert_pos = [-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1]
stop_ang = [-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,1,1]
y =        [14,18,30,17,44,43,70,46,57,63,57,60,132,54,58,55,67,49,93,92,93,94,90,136]

df = pd.DataFrame({'arm_pos': arm_pos, 'vert_pos': vert_pos,
                   'stop_ang': stop_ang, 'y': y})
print(df)
#############################################################
#                                                           #
#                   Now we fit the model                    #
#                                                           #
#############################################################
Formula = 'y~arm_pos+vert_pos+stop_ang+arm_pos:vert_pos+arm_pos:stop_ang\
    +vert_pos:stop_ang+arm_pos:vert_pos:stop_ang'
g = smf.ols(formula = Formula, data=df).fit()
#############################################################
#                                                           #
#           Residual vs Fitted Plot                         #
#                                                           #
#############################################################
plt.figure()
plt.scatter(g.fittedvalues, g.resid, color='red', s=60)
plt.axhline(0, linestyle='--', color='black')
plt.xlabel('Fitted Values', fontsize=13)
plt.ylabel('Residuals', fontsize=13)
plt.title('Residuals vs Fitted')
plt.show()
#############################################################
#                                                           #
#                      QQ Plot                              #
#                                                           #
#############################################################
plt.figure()
stats.probplot(g.resid, dist="norm", plot=plt)
plt.title('Normal Q-Q Plot')
plt.show()
#############################################################
#                                                           #
#                      Transform Data                       #
#                                                           #
#############################################################
lambda1 = 0.3131548
y = np.array(y)
y_transformed = (y**lambda1 - 1) / lambda1
df['y_transformed'] = y_transformed
g2 = smf.ols("y_transformed ~ arm_pos + vert_pos + stop_ang + \
          arm_pos:vert_pos + arm_pos:stop_ang + \
          vert_pos:stop_ang + arm_pos:vert_pos:stop_ang", data=df).fit()
#############################################################
#                                                           #
#           Residual vs Fitted Plot                         #
#                                                           #
#############################################################
plt.figure()
plt.scatter(g2.fittedvalues, g2.resid, color='red', s=60)
plt.axhline(0, linestyle='--', color='black')
plt.xlabel('Fitted Values', fontsize=13)
plt.ylabel('Residuals', fontsize=13)
plt.title('Residuals vs Fitted')
plt.show()
#############################################################
#                                                           #
#                      QQ Plot                              #
#                                                           #
#############################################################
plt.figure()
stats.probplot(g2.resid, dist="norm", plot=plt)
plt.title('Normal Q-Q Plot')
plt.show()
#############################################################
#                                                           #
#        Calculate the factorial effects                    #
#                                                           #
#############################################################
eff = 2 * g2.params[1:]
print(eff)
#############################################################
#                                                           #
#           Half Normal Plot Function                       #
#                                                           #
#############################################################
from scipy.stats import norm
def halfnormal(x):
    n = len(x)
    k = np.array(list(range(1, n+1)))
    halfn = 0.5 + 0.5*(k-.5)/n
    Xs = norm.ppf(halfn)
    Ys = np.sort(abs(x))
    plt.scatter(Xs,Ys)
    plt.xlabel("half-normal quantiles")
    plt.ylabel("absolute effects")
    plt.title("Half-Normal Plot")
#############################################################
#                                                           #
#                Plot half normal for eff                   #
#                                                           #
#############################################################
halfnormal(eff)
#############################################################
#                                                           #
#              Main Effects Plots                           #
#                                                           #
#############################################################
from statsmodels.graphics.factorplots import interaction_plot
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
factor_arrays = [np.array(arm_pos), np.array(vert_pos), np.array(stop_ang)]
factor_names = ['Arm Position', 'Vertical Position', 'Stop Angle']
y_arr = np.array(y_transformed)

for i, ax in enumerate(axes):
    interaction_plot(factor_arrays[i], np.ones(len(y)), y_arr,
                     ax=ax, colors=['red'], markers=['o'])
    ax.set_xlabel(factor_names[i])
    ax.set_ylabel('Mean Distance (in.)')
    ax.get_legend().remove()
plt.suptitle('Main Effects Plot')
plt.tight_layout()
plt.show()
#############################################################
#                                                           #
#                    Interaction Plots                      #
#                                                           #
#############################################################
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
pairs = [(0,1,'Arm Pos','Vert Pos'),
         (0,2,'Arm Pos','Stop Ang'),
         (1,2,'Vert Pos','Stop Ang')]

for ax, (i, j, name_i, name_j) in zip(axes, pairs):
    interaction_plot(factor_arrays[i], factor_arrays[j], y_arr,
                     ax=ax, colors=['red','black'], markers=['o','o'])
    ax.set_xlabel(name_i)
    ax.set_ylabel('Mean Distance (in.)')
    ax.set_title(f'{name_i} x {name_j}')
plt.suptitle('Interaction Effects Plot')
plt.tight_layout()
plt.show()
#############################################################
#                                                           #
#                    Reduced Model                          #
#                                                           #
#############################################################
g_reduced = smf.ols('y_transformed ~ arm_pos + vert_pos', data=df).fit()
print(g_reduced.summary())
print(g2.summary())
