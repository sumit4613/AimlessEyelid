from model_utils.models import TimeStampedModel
from django.db import models
from django.utils.text import gettext_lazy as _


class Student(TimeStampedModel):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    admission_number = models.CharField(
        verbose_name=_("Admission Number"), max_length=255, unique=True
    )
    is_qualified = models.BooleanField(verbose_name=_("Is Qualified"), default=False)
    average_score = models.FloatField(
        verbose_name=_("Average Score"), blank=True, null=True
    )

    def __str__(self):
        return self.first_name

    def get_grade(self):
        if self.average_score <= 40:
            return "Fail"
        elif 40 < self.average_score <= 70:
            return "Pass"
        elif 70 < self.average_score < 100:
            return "Excellent"
        else:
            return "Error"


class ClassRoom(TimeStampedModel):
    name = models.CharField(verbose_name=_("Class Name"), max_length=50)
    student_capacity = models.PositiveIntegerField(verbose_name=_("Students Allowed"))
    students = models.ManyToManyField("classroom.Student")

    def __str__(self):
        return self.name
