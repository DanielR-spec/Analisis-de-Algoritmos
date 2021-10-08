// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
#ifndef __Quick__h__
#define __Quick__h__

#include <algorithm>
#include <iterator>
#include <random>

namespace sorting
{
  namespace helpers
  {
    /**
     * TODO
     * @input b Begin of the sequence.
     * @input e End of the sequence.
     * @output
     */
    template< class _TIt >
    static _TIt Partition( _TIt b, _TIt e )
    {
      auto r = std::make_reverse_iterator( e );
      auto x = *r;
      auto i = b - 1;
      for( _TIt j = b; j != e - 1; ++j )
        if( *j <= x )
          std::swap( *( ++i ), *j );
      std::swap( *( ++i ), *r );

      return( i );
    }

    /**
     * TODO
     * @input b Begin of the sequence.
     * @input e End of the sequence.
     * @output
     */
    template< class _TIt >
    static _TIt RandomizedPartition( _TIt b, _TIt e )
    {
      // Random index
      std::random_device rd;
      std::mt19937 gen( rd( ) );
      std::uniform_int_distribution< unsigned long long >
        dist( 0, std::distance( b, e ) - 1 );
      _TIt i = b + dist( gen );

      // Swap
      auto r = std::make_reverse_iterator( e );
      std::swap( *i, *r );

      // Return an iterator to pivot
      return( Partition( b, e ) );
    }
  } // end namespace

  /**
   * Sorts a sequence.
   * @input b Begin of the sequence.
   * @input e End of the sequence.
   * @output The input sequence [b,e) is sorted.
   */
  template< class _TIt >
  void Quick( _TIt b, _TIt e )
  {
    if( b != e )
    {
      auto q = helpers::RandomizedPartition( b, e );
      Quick( b, q );
      Quick( q + 1, e );
    } // end if
  }
} // end namespace

#endif // __Quick__h__

// eof - Quick.h
