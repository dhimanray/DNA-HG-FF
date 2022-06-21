
unset key
set xlabel 'Chi (degree)'
set ylabel 'Theta (degree)'
p '5UZF-meta-eABF.colvars.traj' u 2:5 every 5 ps 0.2
