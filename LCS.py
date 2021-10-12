import time
import math
import pprint
#Version Recurrente
def fib (i):
    if i <= 1:
        return i
    else:
        return fib(i-1)+fib(i-2)
#Version Memoizada
def fib_M (i, M):
    if M[i] < 0:
        if i <= 1:
            M[i]=i
        else:
            M[i] = fib_M(i-1,M)+fib_M(i-2,M)
            print(M)
    return M[i]

def fib_aux(i):
    M = [-1 for k in range (i+1)]
    return fib_M(i,M)

#Version BottomUp
def fib_B (i):

    M = [-1 for k in range (i+1)]

    #Casos Base
    M[0] = 0
    M[1] = 1

    #Paso Recursivo
    for k in range (2,i+1):
         M[k] = M[k-1] + M[k-2]

    return M[i]

#Version Recurrente - Inocente
def lcsR(X,Y,i,j):
    if i == 0 or j == 0:
        return 0
    else:
        if X[i-1] == Y[j-1]:
            return lcsR(X,Y,i-1,j-1)+1
        else:
            a = lcsR(X,Y,i-1,j)
            b = lcsR(X,Y,i,j-1)
        if a > b:
            return a
        else:
            return b
#Version Memoizada
def lcsM(X,Y,i,j,C):
    if C[i][j] == -math.inf:
        if i == 0 or j == 0:
            C[i][j]=0
            pprint.pprint(C)
            print('===========================')
        else:
            if X[i-1] == Y[j-1]:
                return lcsM(X,Y,i-1,j-1,C)+1
            else:
                a = lcsM(X,Y,i-1,j,C)
                b = lcsM(X,Y,i,j-1,C)
            if a > b:
                C[i][j] = a
                pprint.pprint(C)
                print('===========================')
            else:
                C[i][j] = b
                pprint.pprint(C)
                print('===========================')
    return C[i][j]

#Version BottomUP
def lcsB(X,Y):
    C = [[0 for j in range (len(Y)+1)]for i in range(len(X)+1)]
    
    for j in range (1, len(Y)+1):
        for i in range (1, len(X)+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1]+1
            else:
                a = C[i-1][j]
                b = C[i][j-1]
                if a > b:
                    C[i][j] = a
                else:
                    C[i][j] = b
    pprint.pprint(C)
    return C[len(X)][len(Y)]

def isVowel(ch):
    if (ch == 'a' or ch == 'e' or
        ch == 'i'or ch == 'o' or
        ch == 'u'):
        return True
    return False

#Version BottomUP - BackTraking
def lcsBB( X, Y ):
  C = [ [ 0 for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]
  B = [ [ [ 0, 0 ] for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]

  for j in range( 1, len( Y ) + 1 ):
    for i in range( 1, len( X ) + 1 ):
      if X[ i - 1 ] == Y[ j - 1 ] and isVowel(X[i-1]):
        C[ i ][ j ] = C[ i - 1 ][ j - 1 ] + 1
        B[ i ][ j ] = [ -1, -1 ]
      else:
        a = C[ i - 1 ][ j ]
        b = C[ i ][ j - 1 ]
        if a > b:
          C[ i ][ j ] = a
          B[ i ][ j ] = [ -1, 0 ]
        else:
          C[ i ][ j ] = b
          B[ i ][ j ] = [ 0, -1 ]
        # end if
      # end if
    # end for
  # end for

  # Backtracking
  i = len( X )
  j = len( Y )
  Z = []
  while B[ i ][ j ][ 0 ] != 0 or B[ i ][ j ][ 1 ] != 0:
    if B[ i ][ j ][ 0 ] == -1 and B[ i ][ j ][ 1 ] == -1:
      Z = [ X[ i - 1 ] ] + Z
    # end if
    d = B[ i ][ j ]
    i += d[ 0 ]
    j += d[ 1 ]
  # end while

  if isinstance( X, ( str ) ):
    return ''.join( Z )
  else:
    return Z
  # end if
# end def

def Aux(X,Y):
    C = [[-int.math for j in range (len(Y)+1)]for i in range(len(X)+1)]
    return lcsM(X,Y,len(X),len(Y),C)

X = 'el carro es rojo y grande'
Y = 'el perro me mordio'

print('Secuancia A:',X)
print('Secuancia B:',Y)
Z = lcsBB(X,Y)

print('LCS:',Z,'Tamaño:',len(Z))

#s = time.time()
#r = fib_B(20)
#e = time.time()-s

#print(r,e)