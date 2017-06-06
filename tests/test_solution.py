from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        dic1 = {1:10, 2:20, 3:30}
        key1 = 2
        key2 = 4
        res1 = solution(dic1, key1)
        res2 = solution(dic1, key2)

        self.assertEqual(res1.get(key1), None)
        self.assertEqual(res2, dic1)
