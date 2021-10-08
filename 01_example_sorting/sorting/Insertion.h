// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __Insertion__h__
#define __Insertion__h__

#include <iterator>

namespace sorting
{
  /**
   * Sorts a sequence.
   * @input b Begin of the sequence.
   * @input e End of the sequence.
   * @output The input sequence [b,e) is sorted.
   */
  template< class _TIt >
  void Insertion( _TIt b, _TIt e )
  {
    if( b == e )
      return;
    auto re = std::make_reverse_iterator( b );
    for( _TIt j = b + 1; j != e; ++j )
    {
      auto k = *j;
      auto i = std::make_reverse_iterator( j );
      while( i != re && k < *i )
      {
        *( i - 1 ) = *i;
        i++;
      } // end while
      *( i - 1 ) = k;
    } // end for
  }
} // end namespace

#endif // __Insertion__h__

// eof - Insertion.h
