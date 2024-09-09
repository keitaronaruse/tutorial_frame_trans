#
# @file read_data.py
# @author Keitaro Naruse
# @data 2024-09-09
# @licence MIT
# @brief Read data file
#

# Read N, the number of cycles
N = int( input() )

# Initialize X, Y, Q, M by the size of N
X = [ 0 ] * N
Y = [ 0 ] * N
Q = [ 0 ] * N
M = [ 0 ] * N
S_Q = [ [] ] * N
S_D = [ [] ] * N

# Read every cycle
for i in range( N ):
    X[ i ], Y[ i ], Q[ i ] = map( float, input().split() )
    M[ i ] = int( input() )
    S_Q[ i ] = [ 0 ] * M[ i ]
    S_D[ i ] = [ 0 ] * M[ i ]

    S_Q[ i ] = [ float( x ) for x in input().split() ]
    S_D[ i ] = [ float( x ) for x in input().split() ]

# Output read data
print( N )
print( X )
print( Y )
print( Q )
print( M )
print( S_Q )
print( S_D )
