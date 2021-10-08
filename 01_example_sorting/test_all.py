## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import sorting
import struct, sys, time

## -------------------------------------------------------------------------
def IsSorted( L ):
  r = 0
  if( all( L[ i ] <= L[ i + 1 ] for i in range( len( L ) - 1 ) ) ):
    r = 1
  # end if
  return r
# end def

## -------------------------------------------------------------------------
# Read command-line input values
if len( sys.argv ) < 3:
  print(
    'Usage: python ' + sys.argv[ 0 ] +
    ' data [bubble] [insertion] [quick] [native]'
    )
  sys.exit( 1 )
# end if
data_fname = sys.argv[ 1 ]
a_b = 'bubble' in sys.argv[ 2 : ]
a_i = 'insertion' in sys.argv[ 2 : ]
a_q = 'quick' in sys.argv[ 2 : ]
a_n = 'native' in sys.argv[ 2 : ]

# Read data
data_buf = None
with open( data_fname, 'rb' ) as data_str:
  data_buf = data_str.read( )
# end with
n_samples = int.from_bytes( data_buf[ 0 : 4 ], 'little', signed = False )
sizes = \
  [ \
    int.from_bytes( data_buf[ i : i + 4 ], 'little', signed = False ) \
    for i in range( 4, ( n_samples + 1 ) * 4, 4 ) \
  ]
bin_data = data_buf[ ( n_samples + 1 ) * 4 : ]
data = \
  [ \
    struct.unpack( 'f', bin_data[ i : i + 4 ] )[ 0 ] \
    for i in range( 0, len( bin_data ), 4 )
  ]

# Process data
i = 0
for s in sizes:
  # TODO: print( s, len( data[ i : i + s ] ), len( data ) )

  print( s, end = '' )

  if a_b:
    B = data[ i : i + s ]
    sB = time.time_ns( )
    sorting.Bubble( B )
    tB = time.time_ns( ) - sB
    print( ' ' + str( IsSorted( B ) ) + ' ' + str( tB ), end = '' )
  # end if

  if a_i:
    I = data[ i : i + s ]
    sI = time.time_ns( )
    sorting.Insertion( I )
    tI = time.time_ns( ) - sI
    print( ' ' + str( IsSorted( I ) ) + ' ' + str( tI ), end = '' )
  # end if

  if a_q:
    Q = data[ i : i + s ]
    sQ = time.time_ns( )
    sorting.Quick( Q )
    tQ = time.time_ns( ) - sQ
    print( ' ' + str( IsSorted( Q ) ) + ' ' + str( tQ ), end = '' )
  # end if

  if a_n:
    N = data[ i : i + s ]
    sN = time.time_ns( )
    N.sort( )
    tN = time.time_ns( ) - sN
    print( ' ' + str( IsSorted( N ) ) + ' ' + str( tN ), end = '' )
  # end if

  print( '', end = '\n' )

  i += s
# end for





#   auto sR = std::chrono::high_resolution_clock::now( );
#   std::ifstream data_str( data_fname.c_str( ) );
#   std::string data_buf;
#   data_str.seekg( 0, std::ios::end );
#   data_buf.reserve( data_str.tellg( ) );
#   data_str.seekg( 0, std::ios::beg );
#   data_buf.assign(
#     ( std::istreambuf_iterator< char >( data_str ) ),
#     std::istreambuf_iterator< char >( )
#     );
#   data_str.close( );
#   auto eR = std::chrono::high_resolution_clock::now( );
#   auto tR = std::chrono::duration_cast< std::chrono::nanoseconds >( eR - sR );
#   std::cerr << "Read time: " << tR.count( ) << "ns (" << data_buf.size( ) << "b)" << std::endl;

#   unsigned int n_samples = reinterpret_cast< unsigned int* >( data_buf.data( ) )[ 0 ];
#   std::vector< unsigned int > sizes(
#     reinterpret_cast< unsigned int* >( data_buf.data( ) ) + 1,
#     reinterpret_cast< unsigned int* >( data_buf.data( ) ) + n_samples + 1
#     );
#   float* data =
#     reinterpret_cast< float* >(
#       reinterpret_cast< unsigned int* >( data_buf.data( ) ) + n_samples + 1
#       );

#   for( const unsigned int& s: sizes )
#   {
#     std::cout << s;

#     if( a_b )
#     {
#       std::vector< float > B( data, data + s );
#       auto sB = std::chrono::high_resolution_clock::now( );
#       sorting::Bubble( B.begin( ), B.end( ) );
#       auto eB = std::chrono::high_resolution_clock::now( );
#       auto tB = std::chrono::duration_cast< std::chrono::nanoseconds >( eB - sB );
#       std::cout << " " << std::is_sorted( B.begin( ), B.end( ) ) << " " << tB.count( );
#     } // end if

#     if( a_i )
#     {
#       std::vector< float > I( data, data + s );
#       auto sI = std::chrono::high_resolution_clock::now( );
#       sorting::Insertion( I.begin( ), I.end( ) );
#       auto eI = std::chrono::high_resolution_clock::now( );
#       auto tI = std::chrono::duration_cast< std::chrono::nanoseconds >( eI - sI );
#       std::cout << " " << std::is_sorted( I.begin( ), I.end( ) ) << " " << tI.count( );
#     } // end if

#     if( a_q )
#     {
#       std::vector< float > Q( data, data + s );
#       auto sQ = std::chrono::high_resolution_clock::now( );
#       sorting::Quick( Q.begin( ), Q.end( ) );
#       auto eQ = std::chrono::high_resolution_clock::now( );
#       auto tQ = std::chrono::duration_cast< std::chrono::nanoseconds >( eQ - sQ );
#       std::cout << " " << std::is_sorted( Q.begin( ), Q.end( ) ) << " " << tQ.count( );
#     } // end if

#     if( a_n )
#     {
#       std::vector< float > N( data, data + s );
#       auto sN = std::chrono::high_resolution_clock::now( );
#       std::sort( N.begin( ), N.end( ) );
#       auto eN = std::chrono::high_resolution_clock::now( );
#       auto tN = std::chrono::duration_cast< std::chrono::nanoseconds >( eN - sN );
#       std::cout << " " << std::is_sorted( N.begin( ), N.end( ) ) << " " << tN.count( );
#     } // end if
#     std::cout << std::endl;

#     data += s;
#   } // end for

#   return( EXIT_SUCCESS );
# }

## eof - test_all.cxx
