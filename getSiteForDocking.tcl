proc get_cell {molid incr selection} {
 # Set structure and selection
 set site [atomselect $molid $selection]
 # Compute minimum and maximum for selection
 set minmax [measure minmax $site]
 # Subtract minimum from maximum
 set vec [vecsub [lindex $minmax 1] [lindex $minmax 0]]
 # Print x, y, z lengths
 puts "This is the standard box for the specified contacts: \n"
 puts "[lindex $vec 0] [lindex $vec 1] [lindex $vec 2] \n"
 # Compute selection center
 set center [measure center $site]
 # Print selection center coordinates 
 puts "This is the center of the box: \n"
 puts "$center \n"
 # Increment x, y, z dimensions by specified value
 set x [expr {[lindex $vec 0] + $incr}] 	
 set y [expr {[lindex $vec 1] + $incr}]
 set z [expr {[lindex $vec 2] + $incr}]
 # Print incremented x, y, z dimensions
 puts "You increased the box by $incr. The new coordinates are: \n"
 puts "$x $y $z \n"
 # Prepare input for Autodock4 grid reference file
 puts "Input for Autodock4 grid reference file (1A to 0.375A conversion): \n"
 puts "npts [expr {(round(100*$x/ 0.375)/100) +1}] [expr {(round(100*$y/ 0.375)/100) +1}] [expr {(round(100*$z/ 0.375)/100) + 1}]"
 puts "spacing 0.375"
 puts "gridcenter [expr {double(round(100*[lindex $center 0]))/100}] [expr {double(round(100*[lindex $center 1]))/100}] [expr {double(round(100*[lindex $center 2]))/100}]"
}

