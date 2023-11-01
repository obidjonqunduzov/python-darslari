import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name(' alijon','valiyev')        
        self.assertEqual(formatted_name, ' Alijon Valiyev') # taqqoslash

    def test_otasini_ismi(self):
        name = get_full_name('hasan', 'husanov', 'olimovich')
        self.assertEqual(name, 'Hasan Husanov Olimovich')

unittest.main()