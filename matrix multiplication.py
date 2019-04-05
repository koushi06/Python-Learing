from numpy import *
m1 = [[1,2,7],
      [3,4,8],
      [5,6,4]]

m2 = [[2,3,6],
      [4,5,4],
      [6,7,1]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            result[i][j] += m1[i][k] * m2[k][j]
for r in result:
    print(r)