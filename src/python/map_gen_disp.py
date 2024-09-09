#
# @file map_gen_disp.py
# @author Keitaro Naruse
# @data 2024-09-09
# @licence MIT
# @brief Read data file
#

import math
import matplotlib.pyplot as plt

def frame_trans( x_local, y_local, x, y, q ):
    r = math.radians( q )
    x_world = x_local * math.cos( r ) - math.sin( r ) * y_local + x
    y_world = x_local * math.sin( r ) + math.cos( r ) * y_local + y

    return x_world, y_world

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

# Map generation
x = []
y = []
for i in range( N ):
    for j in range( M[ i ] ):
        if S_D[ i ][ j ] != -1:
            r = math.radians( S_Q[ i ][ j ] )   
            x_local = math.cos( r ) * S_D[ i ][ j ]
            y_local = math.sin( r ) * S_D[ i ][ j ]
            x_world, y_world = frame_trans( x_local, y_local, X[ i ], Y[ i ], Q[ i ] )
            # x.append( x_local )
            # y.append( y_local )
            x.append( x_world )
            y.append( y_world )

# Output read data
plt.scatter( x, y )
plt.xlim( 0, 6200 )
plt.ylim( 0, 4800 )
plt.show( )
