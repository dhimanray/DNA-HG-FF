#:/bin/bash
for i in {1..5}
do
	mkdir entropy_$i
	cd entropy_$i
	echo "#entropy (kcal/mol/K)" > entropy.dat
	gmx covar -f ../HG_${i}.xtc -s ../../dry_CHARMM.pdb -n ../../indexfile.ndx
	tail -n +18 eigenval.xvg > eigenval.dat
	python ../entropy2.py >> entropy.dat

	#remove backup files
	rm -f \#*\#
	cd ..
done


