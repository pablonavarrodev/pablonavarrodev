from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        cont = 0
        cont_aux = 0
        cont_aux2 = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    cont_aux=0
                    cont_aux2=0
                    for x in range(len(mat[0])):
                        if mat[i][x] == 1:
                            cont_aux += 1
                    for y in range(len(mat)):
                        if mat[y][j] == 1:
                            cont_aux2 += 1
                    if cont_aux < 2 and cont_aux2 < 2:
                        cont += 1


        return cont
