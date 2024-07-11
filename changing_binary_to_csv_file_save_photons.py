import numpy as np

# reading the binary file
with open("D:\\11_07_2024\\11_07_2024_10ns_delay_40ns_width_final",'rb') as binary_file:
    binary_data = binary_file.read()

# changing the file to text string
text_data = binary_data.decode('utf-8')

# splitting the string into rows and deleting last, empty row
rows = text_data.split('\r\n')
rows = rows[:-1]

# splitting strings into columns
matrix = [row.split('\t') for row in rows]

# making the matrix
matrix = np.array(matrix, dtype=float)

# saving to csv 
np.savetxt('data\\11_07_2024_10ns_delay_40ns_width_final.csv', matrix, delimiter=',', fmt='%f')