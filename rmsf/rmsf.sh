#:/bin/bash
cd WC_trajectories

for i in {1..5}
do
	cd entropy_$i
	gmx rmsf -f ../WC_${i}.xtc -s ../../dry_AMBER.pdb -n ../../indexfile.ndx
	tail -n +18 rmsf.xvg > rmsf.dat

	#remove backup files
	rm -f \#*\#
	cd ..
done
cd ..

cd HG_trajectories

for i in {1..5}
do
        cd entropy_$i
        gmx rmsf -f ../HG_${i}.xtc -s ../../dry_AMBER.pdb -n ../../indexfile.ndx
        tail -n +18 rmsf.xvg > rmsf.dat

        #remove backup files
        rm -f \#*\#
        cd ..
done
cd ..


