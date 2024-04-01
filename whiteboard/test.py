import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_student_with_vowel_brian(self):
        self.assertEqual(solution("Brian"), "Bria")
    def test_student_with_vowel_hridesh(self):
        self.assertEqual(solution("Hridesh"), "Hrid")
    def test_student_with_vowel_travis(self):
        self.assertEqual(solution("Travis"), "Trav")
    def test_student_tyler(self):
        self.assertEqual(solution("Tyler"), "Tyl")
    def test_student_simon(self):
        self.assertEqual(solution("Simon"), "Sim")
    def test_student_daniel(self):
        self.assertEqual(solution("Daniel"), "Dan")
    def test_wrong_sarah(self):
        self.assertEqual(solution("Sara"),"Sar")
    def test_teacher_shoha_already_nicknamed(self):
        self.assertEqual(solution("Sho"),"Error: Name too short")
    def test_empty(self):
        self.assertEqual(solution(""),"Error: Name too short" )

if __name__ == '__main__':
    unittest.main()