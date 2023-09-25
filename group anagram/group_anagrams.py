class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_anagram=dict()
        for word in strs:
            sorted_hash=''.join(sorted(word))
            if(sorted_hash in group_anagram.keys()):
                group_anagram[sorted_hash].append(word)
            else:
                group_anagram[sorted_hash]=[word]
        print(group_anagram)
        return list(group_anagram.values())

if __name__ == "__main__":
    obj=Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(strs))
    