// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <streambuf>
#include <string>
#include <vector>

#include "sorting/Bubble.h"
#include "sorting/Insertion.h"
#include "sorting/Quick.h"

int main( int argc, char** argv )
{
  // Read command-line input values
  if( argc < 3 )
  {
    std::cerr
      << "Usage: " << argv[ 0 ]
      << " data [bubble] [insertion] [quick] [native]" << std::endl;
    return( EXIT_FAILURE );
  } // end if
  std::string data_fname = argv[ 1 ];
  std::vector< std::string > algos( argv + 2, argv + argc );
  bool a_b = std::find( algos.begin( ), algos.end( ), "bubble" ) != algos.end( );
  bool a_i = std::find( algos.begin( ), algos.end( ), "insertion" ) != algos.end( );
  bool a_q = std::find( algos.begin( ), algos.end( ), "quick" ) != algos.end( );
  bool a_n = std::find( algos.begin( ), algos.end( ), "native" ) != algos.end( );

  // Read data
  auto sR = std::chrono::high_resolution_clock::now( );
  std::ifstream data_str( data_fname.c_str( ) );
  std::string data_buf;
  data_str.seekg( 0, std::ios::end );
  data_buf.reserve( data_str.tellg( ) );
  data_str.seekg( 0, std::ios::beg );
  data_buf.assign(
    ( std::istreambuf_iterator< char >( data_str ) ),
    std::istreambuf_iterator< char >( )
    );
  data_str.close( );
  auto eR = std::chrono::high_resolution_clock::now( );
  auto tR = std::chrono::duration_cast< std::chrono::nanoseconds >( eR - sR );
  std::cerr << "Read time: " << tR.count( ) << "ns (" << data_buf.size( ) << "b)" << std::endl;

  unsigned int n_samples = reinterpret_cast< unsigned int* >( data_buf.data( ) )[ 0 ];
  std::vector< unsigned int > sizes(
    reinterpret_cast< unsigned int* >( data_buf.data( ) ) + 1,
    reinterpret_cast< unsigned int* >( data_buf.data( ) ) + n_samples + 1
    );
  float* data =
    reinterpret_cast< float* >(
      reinterpret_cast< unsigned int* >( data_buf.data( ) ) + n_samples + 1
      );

  for( const unsigned int& s: sizes )
  {
    std::cout << s;

    if( a_b )
    {
      std::vector< float > B( data, data + s );
      auto sB = std::chrono::high_resolution_clock::now( );
      sorting::Bubble( B.begin( ), B.end( ) );
      auto eB = std::chrono::high_resolution_clock::now( );
      auto tB = std::chrono::duration_cast< std::chrono::nanoseconds >( eB - sB );
      std::cout << " " << std::is_sorted( B.begin( ), B.end( ) ) << " " << tB.count( );
    } // end if

    if( a_i )
    {
      std::vector< float > I( data, data + s );
      auto sI = std::chrono::high_resolution_clock::now( );
      sorting::Insertion( I.begin( ), I.end( ) );
      auto eI = std::chrono::high_resolution_clock::now( );
      auto tI = std::chrono::duration_cast< std::chrono::nanoseconds >( eI - sI );
      std::cout << " " << std::is_sorted( I.begin( ), I.end( ) ) << " " << tI.count( );
    } // end if

    if( a_q )
    {
      std::vector< float > Q( data, data + s );
      auto sQ = std::chrono::high_resolution_clock::now( );
      sorting::Quick( Q.begin( ), Q.end( ) );
      auto eQ = std::chrono::high_resolution_clock::now( );
      auto tQ = std::chrono::duration_cast< std::chrono::nanoseconds >( eQ - sQ );
      std::cout << " " << std::is_sorted( Q.begin( ), Q.end( ) ) << " " << tQ.count( );
    } // end if

    if( a_n )
    {
      std::vector< float > N( data, data + s );
      auto sN = std::chrono::high_resolution_clock::now( );
      std::sort( N.begin( ), N.end( ) );
      auto eN = std::chrono::high_resolution_clock::now( );
      auto tN = std::chrono::duration_cast< std::chrono::nanoseconds >( eN - sN );
      std::cout << " " << std::is_sorted( N.begin( ), N.end( ) ) << " " << tN.count( );
    } // end if
    std::cout << std::endl;

    data += s;
  } // end for

  return( EXIT_SUCCESS );
}

// eof - test_all.cxx
