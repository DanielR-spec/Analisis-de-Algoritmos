#!/bin/bash

# -- Get filenames from input
in=$1
fname=$(basename -- "$1")
ext="${fname##*.}"
fname="${fname%.*}"
out=`dirname $1`/`basename $1 $ext`png

gnuplot -presist <<-EOFMarker
set terminal png noenhanced size 1024,768
set output '$out'
set title 'Sorting algorithms comparison ($fname)'
set xlabel 'Data size'
set ylabel 'Execution time (ns)'
plot \
    '$in' using 1:3 with lines lw 2 title 'BubbleSort', \
    '$in' using 1:5 with lines lw 2 title 'InsertionSort', \
    '$in' using 1:7 with lines lw 2 title 'QuickSort', \
    '$in' using 1:9 with lines lw 2 title 'Native'
EOFMarker

## eof - print_graph.sh
