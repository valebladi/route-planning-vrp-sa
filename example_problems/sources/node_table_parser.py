#Converts NodeTable.dat found in MURMEL@Cloud\00_Studentische_Arbeiten\31_Merle_Intern\Simulation\V3\scenarios to TSP format

import numpy as np

output_name = 'monbijou-james-simon' #desired name of the problem
input_filename = 'NodeTable.dat'    #file to pe parsed
scaling = 10000.0

data = np.genfromtxt(input_filename, names=True, delimiter=',',dtype=None,encoding=None)

trashbins = []
for entry in data:
    if entry[4] == 1:
        trashbins.append([entry[2]*scaling, entry[1]*scaling])

f = open(f'{output_name}.tsp', 'w')
f.write(f"NAME: {output_name}\n")
f.write("TYPE: TSP\n")
f.write(f"COMMENT: Scaled by factor {str(scaling)} to avoid rounding inaccuracies. NodeTable taken from Etienne Merle.\n")
f.write(f"DIMENSION: {str(len(trashbins))}\n")
f.write("EDGE_WEIGHT_TYPE: GEO\n")
f.write("NODE_COORD_SECTION\n")
for i in range(len(trashbins)):
    f.write(f"{str(i + 1)} {str(trashbins[i][0])} {str(trashbins[i][1])}\n")
f.write("EOF")
f.close()
