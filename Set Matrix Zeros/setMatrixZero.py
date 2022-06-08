class Solution:
    def setZeroes(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        pos=[]
        #traverse and mark positions of 0 in a list
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    pos.append((i,j))
        # print(pos)
        for k in pos:
            row=k[0]
            col=k[1]
            matrix[row]=[0]*c
            for l in range(r):
                matrix[l][col]=0
        return matrix
if __name__ == "__main__":
    matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(Solution().setZeroes(matrix))