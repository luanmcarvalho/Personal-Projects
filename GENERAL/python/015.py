class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        listwords = sentence.split()
        for i, word in enumerate(listwords):
            if word.startswith(searchWord):
                return i + 1
        return -1

            
    



