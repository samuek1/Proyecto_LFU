import unittest
from src.lfu_cache import LFUCache

class TestLFUCache(unittest.TestCase):
    def test_put_and_get(self):
        cache = LFUCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')

        self.assertEqual(cache.get(1), 'A')
        cache.put(3, 'C')

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 'C')
        self.assertEqual(cache.get(1), 'A')

    def test_eviction_policy(self):
        cache = LFUCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')
        cache.get(1)
        cache.put(3, 'C')

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 'A')
        self.assertEqual(cache.get(3), 'C')

if __name__ == '__main__':
    unittest.main()