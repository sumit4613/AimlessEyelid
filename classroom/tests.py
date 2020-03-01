from django.test import TestCase

from classroom.models import Student


class TestStudentModel(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="sumit",
            last_name="singh",
            admission_number="0161ECE124",
            average_score=65,
        )

    def test_student_can_be_created(self):
        self.assertEqual(self.student.first_name, "sumit")

    def test_str_return(self):
        self.assertEqual(str(self.student.first_name), "sumit")

    def test_average_score_fail(self):
        self.assertEqual(str(self.student.get_grade()), "Pass")
