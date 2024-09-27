import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = 'Komal'
        uppper_name = to_upper(name)
        self.assertEqual(uppper_name,'KOMAL')

if __name__ == "__main__":
    unittest.main()