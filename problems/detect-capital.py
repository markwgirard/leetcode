class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<=1 : return True
        this = word[1].isupper()
        if this and not word[0].isupper(): return False
        for letter in word[2:]:
            last, this = this, letter.isupper()
            if this != last: return False
        return True
