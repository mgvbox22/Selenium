# 1
import unittest


# 2
class TestAbs(unittest.TestCase):
    def test_abs1(self):  # 3
        self.assertEqual(abs(-42), 42,
                         "Should be absolute value of a number")  # 4

    def test_abs2(self):  # 3
        self.assertEqual(abs(-42), -42,
                         "Should be absolute value of a number")  # 4


if __name__ == "__main__":
    unittest.main()  # 5
