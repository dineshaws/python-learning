'''
this file to test cap function
'''
import unittest
import cap

class TestCap(unittest.TestCase):
    '''
    test cases for capitalization
    '''
    def test_single_word_cap(self):
        '''
        single word capitalization \
        '''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multi_word_cap(self):
        '''
        multi word first letter cap
        '''
        text = 'python rocks'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python Rocks')


if __name__ == '__main__':
    unittest.main()
