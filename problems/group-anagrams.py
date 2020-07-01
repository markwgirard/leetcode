class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            char_list = str(sorted(word))
            if char_list in d:
                d[char_list].append(word)
            else:
                d[char_list]=[word]
        return d.values()
