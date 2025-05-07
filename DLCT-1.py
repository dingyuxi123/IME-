from random import randrange
import random
ntc=pd.read_csv('ntc01.csv')
ntc =ntc.iloc[401:850,:]
random.seed(27979)
L = []
i=0
j=0
for i in range(20):
    num = randrange(10)
    L.append(num)
print(L)
random.seed(5)
F=0.9
pc=0.5
for j in range(100):
    trial_vector=[]
    for i in range(20):
        L_new = L[:i] + L[i+1:]   
        vect = random.sample(L_new, 3)
        donar_vector=vect[0]+F*(vect[1]-vect[2])
        r=random.random()
        trial_vector.append(donar_vector)
    sum1=0
    sum2=0
    for i in range(20):
        
        if(trial_vector[i]>10):
            trial_vector[i]=10
        if(trial_vector[i]<1):
            trial_vector[i]=1
            
        y=ntc.iloc[:,1]/(ntc.iloc[:,1]+(L[i]*1000))
        m,b = np.polyfit(ntc.iloc[:,0], y, 1)
        y_fit = m*ntc.iloc[:,0] + b
        nl1=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))  
        sum1=sum1+nl1
        y=ntc.iloc[:,1]/(ntc.iloc[:,1]+(trial_vector[i]*1000))
        m,b = np.polyfit(ntc.iloc[:,0], y, 1)
        y_fit = m*ntc.iloc[:,0] + b
        nl2=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
        sum2=sum2+nl2
        if(nl2<nl1):
            L[i]=trial_vector[i]
            
y=ntc.iloc[:,1]/(ntc.iloc[:,1]+(1.93*1000))
m,b = np.polyfit(ntc.iloc[:,0], y, 1)
y_fit = m*ntc.iloc[:,0] + b
nl1=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
plt.figure()
plt.plot(ntc.iloc[:,0],y_fit)
plt.plot(ntc.iloc[:,0],y)

y=ntc.iloc[:,1]/(ntc.iloc[:,1]+(np.mean(L)*1000))
m,b = np.polyfit(ntc.iloc[:,0], y, 1)
y_fit = m*ntc.iloc[:,0] + b
plt.figure()
nl2=np.max(np.abs(y-y_fit))/(np.max(y)-np.min(y))
plt.plot(ntc.iloc[:,0],y)
plt.plot(ntc.iloc[:,0],y_fit)
print(nl1,nl2)
L