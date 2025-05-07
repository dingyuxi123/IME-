from random import randrange, random, sample, seed
import pandas as pd
import numpy as np
import random
ntc = pd.read_csv('ntc01.csv')
ntc = ntc.iloc[401:, :]

seed(2)
L = [[randrange(20) for _ in range(2)] for _ in range(20)]

seed(55000)

F=0
pc=0
trial_vector = []
NL=1
while(NL>0.001):
    seed(randrange(1000000))
    F=random.random()
    pc=random.random()
    for j in range(100):
        trial_vector = []
        for i in range(20):
            L_new = L[:i] + L[i+1:]
            vect = sample(L_new, 3)
            vect = np.array(vect)
            donor_vector = vect[0] + F * (vect[1] - vect[2])
            delta = randrange(2)
            trial = []
            for k in range(2):
                r = random.random()
                if r <= pc or delta == k:
                    trial.append(donor_vector[k])
                else:
                    trial.append(L[i][k])
            trial_vector.append(trial)
        trial_vector = np.array(trial_vector)
        for i in range(20):
            trial_vector = np.clip(trial_vector, 0, 100)
            y=(ntc.iloc[:,1]/(ntc.iloc[:,1]+L[i][0]*1000))+(ntc.iloc[:,1]/(ntc.iloc[:,1]+L[i][1]*1000))
            m,b = np.polyfit(ntc.iloc[:,0], y, 1)
            y_fit = m*ntc.iloc[:,0] + b
            nl=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))  
            sum1=sum1+nl
            y=(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[i,0]*1000))+(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[i,1]*1000))
            m,b = np.polyfit(ntc.iloc[:,0], y, 1)
            y_fit = m*ntc.iloc[:,0] + b
            nl1=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
            if(nl1<nl):
                L[i]=trial_vector[i]
    y=(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[0,0]*1000))+(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[0,1]*1000))
    m,b = np.polyfit(ntc.iloc[:,0], y, 1)
    y_fit = m*ntc.iloc[:,0] + b
    NL=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
    print(NL,F,pc,trial_vector[0])
y=(ntc.iloc[:,1]/(ntc.iloc[:,1]+4.56*1000))+(ntc.iloc[:,1]/(ntc.iloc[:,1]+0.233*1000))
m,b = np.polyfit(ntc.iloc[:,0], y, 1)
y_fit = m*ntc.iloc[:,0] + b
nl1=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
plt.figure()
plt.plot(ntc.iloc[:,0],y_fit)
plt.plot(ntc.iloc[:,0],y)
y=(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[0,0]*1000))+(ntc.iloc[:,1]/(ntc.iloc[:,1]+trial_vector[0,1]*1000))
m,b = np.polyfit(ntc.iloc[:,0], y, 1)
y_fit = m*ntc.iloc[:,0] + b
plt.figure()

nl2=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
plt.plot(ntc.iloc[:,0],y)
plt.plot(ntc.iloc[:,0],y_fit)
print(nl1,nl2)
L