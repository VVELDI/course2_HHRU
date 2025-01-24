# import unittest
# import os
# from src.json_saver import JSONSaver
# from src.vacancy import Vacancy
#
# class TestJSONSaver(unittest.TestCase):
#     def setUp(self):
#         self.saver = JSONSaver('data/test_vacancies.json')
#
#     def tearDown(self):
#         if os.path.exists('data/test_vacancies.json'):
#             os.remove('data/test_vacancies.json')
#
#     def test_add_vacancy(self):
#         vacancy = Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")
#         self.saver.add_vacancy(vacancy)
#         self.assertEqual(len(self.saver.vacancies), 1)
#
#     def test_delete_vacancy(self):
#         vacancy = Vacancy("Python Developer", "http://example.com", 100000, "Описание вакансии")
#         self.saver.add_vacancy(vacancy)
#         self.saver.delete_vacancy(vacancy)
#         self.assertEqual(len(self.saver.vacancies), 0)
#
# if __name__ == '__main__':
#     unittest.main()