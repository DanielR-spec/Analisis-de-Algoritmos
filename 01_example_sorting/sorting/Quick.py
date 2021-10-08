## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import random


## -------------------------------------------------------------------------
## Quick: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
class Quick:
  '''
  --------------------------------------------------------------------------
  QuickAux: sorts a subsequence of comparable (<) elements
  @inputs: S, a reference to a secuence of comparable elements.
           p, start of the subsequence
           r, end of the subsequence
  @outputs: S[p:r], an ordered permutation of the input.
  --------------------------------------------------------------------------
    '''
  def Partition( S, p, r ):
    x = S[ r ]
    i = p
    for j in range( p, r ):
      if S[ j ] < x:
        S[ i ], S[ j ] = S[ j ], S[ i ]
        i += 1
      # end if
    # end for
    S[ i ], S[ r ] = S[ r ], S[ i ]
    return i
  # end def

  '''
  --------------------------------------------------------------------------
  QuickAux: sorts a subsequence of comparable (<) elements
  @inputs: S, a reference to a secuence of comparable elements.
           p, start of the subsequence
           r, end of the subsequence
  @outputs: S[p:r], an ordered permutation of the input.
  --------------------------------------------------------------------------
  '''
  def RandomizedPartition( S, p, r ):
    i = random.randint( p, r )
    S[ r ], S[ i ] = S[ i ], S[ r ]
    return Quick.Partition( S, p, r )
  # end def

  '''
  --------------------------------------------------------------------------
  Sort: sorts a subsequence of comparable (<) elements
  @inputs: S, a reference to a secuence of comparable elements.
           p, start of the subsequence
           r, end of the subsequence
  @outputs: S[p:r], an ordered permutation of the input.
  --------------------------------------------------------------------------
  '''
  def Sort( S, p, r ):
    if p < r:
      q = Quick.RandomizedPartition( S, p, r )
      Quick.Sort( S, p, q - 1 )
      Quick.Sort( S, q + 1, r )
    # end if
  # end def

  '''
  --------------------------------------------------------------------------
  Main method: sorts a sequence of comparable (<) elements
  @inputs: S, a reference to a secuence of comparable elements.
  @outputs: S, an ordered permutation of the input.
  --------------------------------------------------------------------------
  '''
  def __init__( self, S ):
    Quick.Sort( S, 0, len( S ) - 1 )
  # end def
# end class

## eof - Quick.py
