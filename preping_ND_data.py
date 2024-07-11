import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


ND = [0, 1, 1, 3, 3, 8]
exp = [0.001, 0.01, 0.001, 0.01, 0.05, 0.05]
power =[0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
total_intensity = []

for i in range(len(ND)):
    intensity = np.loadtxt('ND_characterization\\2024_07_02_skalowanie_filtrow_Jakub\\2024_07_02_ND'+str(ND[i])+'_'+str(power[i])+'uW_'+str(exp[i])+'exp.asc')
    noise = intensity[:800]
    noise_mean = np.mean(noise)
    intensity = intensity - noise_mean
    # Find the index of the maximal value in the flattened array
    max_index = np.argmax(intensity)

    max_position = np.unravel_index(max_index, intensity.shape)
    row_index, col_index = max_position
    max_row = intensity[row_index, :]
    max_column = intensity[:, col_index]

    intensity_spot = intensity[1080:1221, 1000:1135]
    total_intensity.append(np.sum(intensity_spot))

ND0_1_0_001_value = total_intensity[2]/total_intensity[0]
print('how much to multiply from ND1 to get ND0 '+str(1/ND0_1_0_001_value))
ND_1_010_001_value = total_intensity[2]/total_intensity[1]

ND_3_1_010_value = total_intensity[3]/total_intensity[1]

ND_3_0_value = ND_3_1_010_value*ND_1_010_001_value*ND0_1_0_001_value
print('how much to multiply to go from ND3 to ND0 '+ str(ND_3_0_value))

ND_3_050_010_value = total_intensity[4]/total_intensity[3]

ND_8_3_050_value = total_intensity[5]/total_intensity[4]

ND_8_0 = ND_8_3_050_value*ND_3_050_010_value*ND_3_0_value
print('how much to multiply to go from ND8 to ND0 '+str(ND_8_0))

ND_831_0 = ND_8_0*ND_3_0_value*ND0_1_0_001_value
print('how much to multiply to go from ND8 +ND3 +ND1 to ND0: '+str(ND_831_0))