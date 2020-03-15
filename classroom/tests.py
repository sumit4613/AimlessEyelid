from django.test import TestCase
from mixer.backend.django import mixer
from classroom.models import Student


class TestStudentModel(TestCase):
    # def setUp(self):
    #     self.student = Student.objects.create(
    #         first_name="sumit",
    #         last_name="singh",
    #         admission_number="0161ECE124",
    #         average_score=65,
    #     )

    def test_student_can_be_created(self):
        student = mixer.blend(Student, first_name="sumit")
        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(student_result.first_name, "sumit")

    def test_str_return(self):
        student = mixer.blend(Student, first_name="sumit")
        student_result = Student.objects.last()

        self.assertEqual(str(student_result), "sumit")

    def test_average_score_fail(self):
        student = mixer.blend(Student, average_score=10)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Fail")

    def test_average_score_pass(self):
        student = mixer.blend(Student, average_score=70)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Pass")

    def test_average_score_excellent(self):
        student = mixer.blend(Student, average_score=95)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Excellent")

    def test_average_score_error(self):
        student = mixer.blend(Student, average_score=105)
        student_result = Student.objects.last()

        self.assertEqual(student_result.get_grade(), "Error")
