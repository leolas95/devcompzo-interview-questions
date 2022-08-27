class Solution:
    def climb(self, n: int, cache) -> int:
        if n in cache:
            return cache[n]
        else:
            cache[n] = self.climb(n - 1, cache) + self.climb(n - 2, cache)
            return cache[n]

    def climb_stairs(self, n: int) -> int:
        # Either this or use a lru_cache
        cache = {
            1: 1,
            2: 2,
            3: 3,
        }
        return self.climb(n, cache)
