#!/bin/bash

# -- Get filenames from input
in=$1
cxx=$1_cxx.out
python=$1_python.out
out_bubble=$1_cxx_python_bubble.png
out_insertion=$1_cxx_python_insertion.png
out_quick=$1_cxx_python_quick.png
out_native=$1_cxx_python_native.png

gnuplot -presist <<-EOFMarker
set terminal png noenhanced size 1024,768
set output '$out_bubble'
set title 'BubbleSort comparison ($in)'
set xlabel 'Data size'
set ylabel 'Execution time (ns)'
plot \
    '$cxx' using 1:3 with lines lw 2 title 'C++', \
    '$python' using 1:3 with lines lw 2 title 'Python'
EOFMarker

gnuplot -presist <<-EOFMarker
set terminal png noenhanced size 1024,768
set output '$out_insertion'
set title 'InsertionSort comparison ($in)'
set xlabel 'Data size'
set ylabel 'Execution time (ns)'
plot \
    '$cxx' using 1:5 with lines lw 2 title 'C++', \
    '$python' using 1:5 with lines lw 2 title 'Python'
EOFMarker

gnuplot -presist <<-EOFMarker
set terminal png noenhanced size 1024,768
set output '$out_quick'
set title 'QuickSort comparison ($in)'
set xlabel 'Data size'
set ylabel 'Execution time (ns)'
plot \
    '$cxx' using 1:7 with lines lw 2 title 'C++', \
    '$python' using 1:7 with lines lw 2 title 'Python'
EOFMarker

gnuplot -presist <<-EOFMarker
set terminal png noenhanced size 1024,768
set output '$out_native'
set title 'NativeSort comparison ($in)'
set xlabel 'Data size'
set ylabel 'Execution time (ns)'
plot \
    '$cxx' using 1:9 with lines lw 2 title 'C++', \
    '$python' using 1:9 with lines lw 2 title 'Python'
EOFMarker

## eof - combine_graph.sh
