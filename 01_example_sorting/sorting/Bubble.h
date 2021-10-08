// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __Bubble__h__
#define __Bubble__h__

#include <algorithm>
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
  void Bubble( _TIt b, _TIt e )
  {
    unsigned long long n = std::distance( b, e );
    for( unsigned long long i = 1; i <= n; ++i )
      for( _TIt j = b + 1; j != e; ++j )
        if( *j < *( j - 1 ) )
          std::swap( *( j - 1 ), *j );
  }
} // end namespace

#endif // __Bubble__h__

// eof - Bubble.h
