import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.gridspec as gridspec

# loading the data
data = np.loadtxt("data\\11_07_2024_10ns_delay_40ns_width_final.csv", delimiter=',')
# taking first two columns as x and y positions and making it as dataFrame
data = pd.DataFrame(data[:,[0,1]], columns= ['x position', 'y position'])
data = data.astype(int)
data = data[(data >= 0).all(axis=1) & (data <= 2048).all(axis=1)]

# preparing figure size and making grid for subplots
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

# making histogram of counts
ax1 = plt.subplot(gs[0, :]) # adding that this plot will all over first row in grid
ax1 = sns.histplot(data,binwidth=5)
ax1.set_title("Histogram of counts for X and Y dimension")

# data for first spot (range of pixel taken by analizing first histogram)
data_spot1 = data[(data['x position'].between(1000,1250)) & (data['y position'].between(850,1200))]
ax2 = plt.subplot(gs[1, 0]) # bottom left plot
ax2 = sns.histplot(data_spot1, binwidth=5)
ax2.set_title("Histogram of counts for first spot")
ax2.set_xlabel("total count for spot 1: "+ str(len(data_spot1)))

# data for second spot (range of pixel taken by analizing first histogram)
data_spot2 = data[(data['x position'].between(1075,1220)) & (data['y position'].between(1450,1650))]
ax3 = plt.subplot(gs[1, 1]) # bottom right spot
ax3 = sns.histplot(data_spot2, binwidth=5)
ax3.set_title("Histogram of counts for second spot")
ax3.set_xlabel("total count for spot 2: "+ str(len(data_spot2)))

# adding text with photons/second calculation and changing tight layout to not cut this while showing
fig.text(0.5, 0.01,"photons per second: "+ str(round((len(data_spot2)+len(data_spot1))/300,2)), ha='center', fontsize=12)
plt.tight_layout(rect=[0, 0.03, 1, 0.97])

# saving plot
plt.savefig('PLOTS_0807\\11_07_2024_10ns_delay_40ns_width_final_histogran.png', bbox_inches='tight')

