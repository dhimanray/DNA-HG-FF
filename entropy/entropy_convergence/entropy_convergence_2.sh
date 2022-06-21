#:/bin/bash

cp eigenval.dat backup_eigenval.dat

touch entropy_values_2.dat
touch frames_2.dat
echo "#entropy (kcal/mol/K)" > entropy_values_2.dat
echo "#frame " > frames_2.dat 

rm eigenval.*

for i in 50 60 70 80 90 100
do
	j=$(( $i * 50 ))
	mdconvert -o traj_${i}.xtc -t ../../dry_CHARMM.pdb -i 0:$j ../HG_5.xtc
	gmx covar -f traj_${i}.xtc -s ../../dry_CHARMM.pdb -n ../../indexfile.ndx
	tail -n +18 eigenval.xvg > eigenval.dat
	python entropy.py >> entropy_values_2.dat
	echo $j >> frames_2.dat

done

paste -d' ' frames_2.dat entropy_values_2.dat > entropy_convergence_2.dat
#remove backup files
rm -f \#*\#
rm *.xtc

