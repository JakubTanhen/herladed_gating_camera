import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# The data is in dat format, probably one file is one frame 
# To save storage on my computer data is stored on my USB drive, in the end I will upload all the data to git

# Set maximum value as frames you saved +1 
iterate = list(range(1,101))

# making function to animate
def animate(i):
    ax.clear()
    data = np.loadtxt("D:\\test_data\\test-tt"+str(iterate[i])+".dat")    # taking file
    sns.heatmap(data, annot=False, cmap='viridis', cbar=False)  # making plot
    ax.set_title('Heatmap of test-tt'+str(iterate[i])+' file')
    print("step"+str(iterate[i])+"done")
    return ax, 
fig, ax = plt.subplots(figsize=(10,8))
# Adding color bar and making animation
norm = Normalize(vmin=0, vmax=10000)
cbar = fig.colorbar(ScalarMappable(norm=norm, cmap='viridis'), ax=ax, orientation='horizontal', pad=0.05, fraction=0.046, aspect=20, shrink=0.3)
ani = FuncAnimation(fig, animate, frames=len(iterate), blit=False)

# saving animation as gif
ani.save('PLOTS\\heat_map_tes-tt.gif', writer='pillow', fps=2, dpi=300)