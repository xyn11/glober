import unittest
import glober

class TestGlobber(unittest.TestCase):
    def test_check(self):
        self.assertEqual(glober.check('asdfer.py', '*'), True)

    def test_check_multi_as(self):
        self.assertEqual(glober.check('asd_fer.py', '*_*.*'), True)

    def test_check_ques(self):
        self.assertEqual(glober.check('asdfer.py', 'as?fer.?y'), True)
    
    def test_check_false(self):
        self.assertEqual(glober.check('asdfer.py', '*d????.py'), False)

    def test_check_combine(self):
        self.assertEqual(glober.check('asDfer.py', '**?fer.*'), True)

    def test_star(self):
        self.assertEqual(glober.search('./fortesting', '*.py'), ['four.py', 'bar.py', 'foo.py'])

    def test_star_missing(self):
        self.assertEqual(glober.search('./fortesting', '*.doc'), [])

    def test_question(self):
        self.assertEqual(glober.search('./fortesting', 'fo?.py'), ['foo.py'])

    def test_questions(self):
        self.assertEqual(glober.search('./fortesting', 'f?u?.py'), ['four.py'])

    def test_multi(self):
        self.assertEqual(glober.search('./fortesting','*u?.py'), ['four.py'])

    def test_multip(self):
        self.assertEqual(glober.search('./fortesting','*o*.py'), ['four.py', 'foo.py'])    

if __name__ == '__main__':
    unittest.main()
