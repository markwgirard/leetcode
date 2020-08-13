class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.masks = gen_bit_masks(len(characters), combinationLength)

    def next(self) -> str:
        return mask_to_string(self.masks.pop(), self.chars)

    def hasNext(self) -> bool:
        return bool(self.masks)

def gen_bit_masks(n, k):
    masks = [(0,0)]
    for r in range(n-1,-1,-1):
        masks = [((m<<1)+b, w+b) for m,w in masks for b in [0,1] if 0<=k-w-b<=r]
    return [mask for mask,_ in masks]

def mask_to_string(mask, characters):
    i, s = 1, ''
    while mask:
        if mask%2: s = characters[-i] + s
        i, mask = i + 1, mask >> 1
    return s

''' Alternative solution that generates combinations instead of masks'''
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combs = combs(characters, combinationLength)

    def next(self) -> str:
        return self.combs.pop()

    def hasNext(self) -> bool:
        return self.combs

def combs(characters, k):
    strs, n = [''] , len(characters)
    for i, c in enumerate(characters):
        strs = [s+x for s in strs  for x in ['',c] if 0<=k-len(s+x)<=n-i-1]
    return strs
