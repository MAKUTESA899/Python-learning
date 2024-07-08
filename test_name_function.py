import unittest
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    """test for name'name_function.py'. """
    def test_first_last_name(self):
        """do names like 'alex kamau' work?"""
        formatted_name = get_formatted_name('alex', 'kamau')
        self.assertEqual(formatted_name,'Alex Kamau')
                         
if __name__ == '__main__' :
    unittest.main()