import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
#Examples using N = 5, M = 4
print(np.eye(N, M, k = 0)) #Returns a matrix with diagonal elements = 1 and the rest = 0. The diagonal can be main(0), upper(+n) or lower(-n), set by k EX: [[ 1.  0.  0.  0.]
#                                                                                                                                                           [ 0.  1.  0.  0.]
#                                                                                                                                                           [ 0.  0.  1.  0.]
#                                                                                                                                                           [ 0.  0.  0.  1.]
#                                                                                                                                                           [ 0.  0.  0.  0.]]
print(np.eye(N, M, k = 1))#[[ 0.  1.  0.  0.]
#                           [ 0.  0.  1.  0.]
#                           [ 0.  0.  0.  1.]
#                           [ 0.  0.  0.  0.]
#                           [ 0.  0.  0.  0.]]

print(np.eye(N, M, k = 2))#[[ 0.  0.  1.  0.]
#                           [ 0.  0.  0.  1.]
#                           [ 0.  0.  0.  0.]
#                           [ 0.  0.  0.  0.]
#                           [ 0.  0.  0.  0.]]

print(np.eye(N, M, k = -1))#[[ 0.  0.  0.  0.]
#                           [ 1.  0.  0.  0.]
#                           [ 0.  1.  0.  0.]
#                           [ 0.  0.  1.  0.]
#                           [ 0.  0.  0.  1.]]

print(np.eye(N, M, k = -2))#[[ 0.  0.  0.  0.]
#                           [ 0.  0.  0.  0.]
#                           [ 1.  0.  0.  0.]
#                           [ 0.  1.  0.  0.]
#                           [ 0.  0.  1.  0.]]

print(np.identity(N)) #Returns a square matrix with diagonal elements = 1 and the rest = 0 EX:[[ 1.  0.  0.  0.  0.]
#                                                                                              [ 0.  1.  0.  0.  0.]
#                                                                                              [ 0.  0.  1.  0.  0.]
#                                                                                              [ 0.  0.  0.  1.  0.]
#                                                                                              [ 0.  0.  0.  0.  1.]]

