// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================

#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>

int main( int argc, char** argv )
{
  // Get command line arguments
  if( argc < 7 )
  {
    std::cerr
      << "Usage: "
      << argv[ 0 ] << " start end step min_val max_val outfile"
      << std::endl;
    return( EXIT_FAILURE );
  } // end if

  unsigned int start, end, step;
  double min_val, max_val;
  std::stringstream args;
  args
    << argv[ 1 ] << " " << argv[ 2 ] << " " << argv[ 3 ] << " "
    << argv[ 4 ] << " " << argv[ 5 ];
  args >> start >> end >> step >> min_val >> max_val;
  std::string outfile = argv[ 6 ];

  // Prepare random generator
  std::random_device rd;
  std::mt19937 gen( rd( ) );
  std::uniform_real_distribution< float > dis( min_val, max_val );

  // Fill vector
  std::vector< unsigned int > sizes;
  std::vector< float > data;
  for( unsigned int i = start; i <= end; i += step )
  {
    sizes.push_back( i );
    for( unsigned int s = 0; s < i; ++s )
      data.push_back( dis( gen ) );
  } // end for

  // Save data
  auto outstr = std::fstream( outfile, std::ios::out | std::ios::binary );
  unsigned int n_samples = sizes.size( );
  outstr.write(
    reinterpret_cast< const char* >( &n_samples ), sizeof( unsigned int )
    );
  outstr.write(
    reinterpret_cast< const char* >( sizes.data( ) ),
    sizeof( unsigned int ) * n_samples
    );
  outstr.write(
    reinterpret_cast< const char* >( data.data( ) ),
    sizeof( float ) * data.size( )
    );
  outstr.close( );

  return( EXIT_SUCCESS );
}

// eof - create_sorting_data.cxx
