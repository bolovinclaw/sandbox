import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_named(self):
        self.assertEqual(greet("world"), "hello, world")

    def test_sandbox(self):
        self.assertEqual(greet("sandbox"), "hello, sandbox")


if __name__ == "__main__":
    unittest.main()
