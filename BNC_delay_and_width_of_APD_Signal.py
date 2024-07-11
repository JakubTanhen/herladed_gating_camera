import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data\\F1Trace00003.csv')
data2 = pd.read_csv('data\\C2Trace00004.csv')

data['Time'] = data['Time'] * 10**9
data.rename(columns={'Time': 'Time (ns)', 'Ampl': 'Amplitude (V)'}, inplace=True)

#data2['Time'] = data2['Time'] * 10**9
#data2.rename(columns={'Time': 'Time (ns)', 'Ampl': 'Amplitude (V)'}, inplace=True)

fig = plt.figure(figsize=(10, 8))
sns.set_style('whitegrid')
ax = sns.lineplot(data, x='Time (ns)', y='Amplitude (V)')
#ax2 = sns.lineplot(data2, x='Time (ns)', y='Amplitude (V)')
ax.set_title('Width of the APD inpulse in time')
#plt.savefig('PLOTS\\Width_of_APD_Signal.png', bbox_inches = 'tight')
plt.show()