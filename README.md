# tiltangle
1. tiltangle.py
2. *.nc
3. mol.prmtop

Output:
1. trajpdb: the input for cpptraj
2. output.pdb: the pdb of the frame
3. tilt_angle.dat: the instantaneous tilt angles
4. angle_summary.dat: the summary of the angles values

1. tiltangle.py
#parameters: 
1). startCA, endCA: the sequence number of AminoAcid in that protein sequence
2). start_frame, stop_frame, step_frame
3). count: name of *.prmtop

4). logic: get the vector of start/endCA and the bilayer normal(z-axis), use dot product to calculate the angles.
