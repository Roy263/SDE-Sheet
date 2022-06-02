class Solution:
    def transpose(self,matrix):
        tmatrix=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return tmatrix
if __name__=='__main__':
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    obj=Solution()
    print(obj.transpose(matrix))