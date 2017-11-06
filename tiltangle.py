import numpy as np
import pandas as pd
import math
import subprocess
from subprocess import call

startCA = 8
endCA = 25
count = 'mol'
start_frame = 4
stop_frame = 1379
step_frame = 4

angTOT = []

for f in range(start_frame, stop_frame+1, step_frame):
	with open('trajpdb', 'w') as outf:
		outf.write("parm %(count)s.prmtop\n"%locals())
		outf.write("trajin analysis-wrap_Prod15-isotropic_0025.nc %(f)s %(f)s" % locals())
		outf.write('\n')
		outf.write("trajout output.pdb pdb\n")
		outf.write("go\n")

	call(["cpptraj","-i","trajpdb"])


	protein = []
	with open("output.pdb") as infile:
	    for line in infile:
	        if "CA" in line:
	            protein.append(line.split())


	colname = ['ATOM', 'AtomNo', 'CA', 'AA', 'ResNo', 'X', 'Y', 'Z', 'No8', 'No9', 'Element' ]
	data = pd.DataFrame(protein, columns=colname)

	startX = float(data['X'][startCA-1])
	startY = float(data['Y'][startCA-1])
	startZ = float(data['Z'][startCA-1])
	endX = float(data['X'][endCA-1])
	endY = float(data['Y'][endCA-1])
	endZ = float(data['Z'][endCA-1])

	start = np.array([startX, startY, startZ])
	end = np.array([endX, endY, endZ])
	norm = np.array([0, 0, 1])
	delVector = end - start

	dotP = np.dot(delVector, norm)
	dist = np.linalg.norm(delVector)
	angle = math.acos( math.fabs(dotP) / dist)
	angle = math.degrees(angle)
	angTOT.append(angle)

with open("angle_summary.dat", 'w') as angsum:
	angmean = np.mean(angTOT)
	angstd = np.std(angTOT)
	angmax = np.max(angTOT)
	angmin = np.min(angTOT)
	angsum.write("mean = %s\n" % angmean)
	angsum.write("std = %s\n" % angstd)
	angsum.write("max = %s\n" % angmax)
	angsum.write("min = %s\n" % angmin)

with open("tilt_angle.dat", 'w') as angleout:
	for item in angTOT:
		angleout.write("%s\n" % item)

print("FINISHED")