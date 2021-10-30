import unittest
from core.views import home_page

class TestViews(unittest.TestCase):
    def test_home_page(self):
        self.assertEqual(2,2)
        

if __name__ == '__main__':
    unittest.main()  
