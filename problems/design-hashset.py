class MyHashSet:

    def __init__(self):
        N = 1000000
        self.buckets = [False]*(N+1)

    def add(self, key: int) -> None:
        self.buckets[key] = True

    def remove(self, key: int) -> None:
        self.buckets[key] = False

    def contains(self, key: int) -> bool:
        return self.buckets[key]
