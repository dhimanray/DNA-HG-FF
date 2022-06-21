#:/bin/bash

mdconvert -o HG_1.xtc -t ../dry_CHARMM.pdb -i 1000:5999 ../HG_no_water.xtc 
mdconvert -o HG_2.xtc -t ../dry_CHARMM.pdb -i 2000:6999 ../HG_no_water.xtc 
mdconvert -o HG_3.xtc -t ../dry_CHARMM.pdb -i 3000:7999 ../HG_no_water.xtc 
mdconvert -o HG_4.xtc -t ../dry_CHARMM.pdb -i 4000:8999 ../HG_no_water.xtc 
mdconvert -o HG_5.xtc -t ../dry_CHARMM.pdb -i 5000:9999 ../HG_no_water.xtc 

