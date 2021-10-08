## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

## -------------------------------------------------------------------------
## Insertion: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
def Insertion( S ):
  for j in range( 1, len( S ) ):
    k = S[ j ]
    i = j - 1
    while 0 <= i and k < S[ i ]:
      S[ i + 1 ] = S[ i ]
      i = i - 1
    # end while
    S[ i + 1 ] = k
  # end for
# end def

## eof - Insertion.py
