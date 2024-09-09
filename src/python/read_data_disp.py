#
# @file read_data_disp.py
# @author Keitaro Naruse
# @data 2024-09-09
# @licence MIT
# @brief Read data file
#

import math
import matplotlib.pyplot as plt

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
    # [ X[ i ], Y[ i ], Q[ i ] ] = 
    X[ i ], Y[ i ], Q[ i ] = map( float, input().split() )
    M[ i ] = int( input() )
    S_Q[ i ] = [ 0 ] * M[ i ]
    S_D[ i ] = [ 0 ] * M[ i ]

    S_Q[ i ] = [ float( x ) for x in input().split() ]
    S_D[ i ] = [ float( x ) for x in input().split() ]

# Output read data
for i in range( N ):
    x = []
    y = []
    for j in range( M[ i ] ):
        if S_D[ i ][ j ] != -1:
            r = math.radians( S_Q[ i ][ j ] )   
            x.append( math.cos( r ) * S_D[ i ][ j ] )
            y.append( math.sin( r ) * S_D[ i ][ j ] )
    plt.scatter( x, y )
    plt.xlim( -1000, 1000 )
    plt.ylim( -1000, 1000 )
    plt.title( i )
    plt.show( )
