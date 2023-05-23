from django.db import models

# Create your models here.
class Student(models.Model):
    # blank=True необезательно в сайте указывать,null=True чтобы в базе не возникал ошибка и в бале был null
    firstname = models.CharField(max_length=50, verbose_name="Name", blank=True, null=True)
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    # unique отвечает за уникальность и он не может повторятся
    phone = models.CharField(max_length=12, verbose_name="Number phone", unique=True)
    course = models.PositiveBigIntegerField(verbose_name="Course")
    group = models.CharField(max_length=50, verbose_name="Group")
    faculty = models.CharField(max_length=50, verbose_name="Faculty")

    @property
    def full_name(self):
        return self.firstname + " " + self.lastname

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} | course: {self.course} | group: {self.group} | faculty: {self.faculty}"

    class Meta:
        verbose_name = "Студент"
        verbose_name = "Студенты"

class Teacher(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Name")
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    subjectname = models.CharField(max_length=50, verbose_name="Subject name")
    lengthofservice = models.CharField(max_length=50, verbose_name="Length of service")

    @property
    def full_name(self):
        return self.firstname + " " + self.lastname

    class Meta:
        verbose_name = "Teacher"
        verbose_name = "Teachers"

