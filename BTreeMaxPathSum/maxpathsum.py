class Solution:
	def maxPathSum(self,root):
		maxpath=float("-inf")
		def maxPath(node):
			nonlocal maxpath
			if node:
				leftmax=max(maxPath(node.left),0)
				rightmax=max(maxPath(node.right),0)

				currMaxPath=node.val+leftmax+rightmax
				
				maxpath=max(maxpath,currMaxPath)
				return node.val+ max(leftmax,rightmax)
			else:
				return 0
		maxPath(root)
		return maxpath

if __name__=="__main__":
	obj=Solution()
	root=[-10,9,20,None,None,15,7]
	result=obj.maxPathSum(root)
	print(result)
