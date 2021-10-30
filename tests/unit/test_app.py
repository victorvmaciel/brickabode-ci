import unittest
from app import create_app

class test_app(unittest.TestCase):
    def test_create_app(self):
        start_app = create_app()
        self(False, True)
        AssertionError: False != True

if __name__ == '__main__':
    unittest.main()      