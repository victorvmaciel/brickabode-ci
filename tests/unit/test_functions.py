import unittest
from utils.functions import get_database_connection

class test_database_connection(unittest.TestCase):
    
    def test_get_database_connection(self):
        self.assertTrue('true')