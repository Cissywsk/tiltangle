# tiltangle
1. tiltangle.py
2. *.nc
3. mol.prmtop

Output:
*trajpdb: the input for cpptraj
*output.pdb: the pdb of the frame
*tilt_angle.dat: the instantaneous tilt angles
*angle_summary.dat: the summary of the angles values

1. tiltangle.py
#parameters: 
*startCA, endCA: the sequence number of AminoAcid in that protein sequence
*start_frame, stop_frame, step_frame
*count: name of *.prmtop
#logic: get the vector of start/endCA and the bilayer normal(z-axis), use dot product to calculate the angles.
