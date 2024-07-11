import matplotlib.pyplot as plt
import numpy as np

# loading data
data = np.loadtxt("data\\11_07_2024_10ns_delay_40ns_width_final.csv", delimiter=',')

# making scatter plot
fig, ax = plt.subplots(figsize=(10,8))

plt.scatter(data[:,[0]],data[:,[1]], s=1)
# making aesthetics
plt.xlim(0,2048)
plt.ylim(0,2048)
plt.title('Accumulation for 5 minutes 1m BNC 40ns window 10 ns delay on stanford th 150 ')
plt.xlabel('x position (pixels)')
plt.ylabel('Y position (pixels)')

plt.savefig('PLOTS_0807\\11_07_2024_10ns_delay_40ns_width_final.png', bbox_inches = 'tight')
