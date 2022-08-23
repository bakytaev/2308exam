from django.db import models
from datetime import date


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=128)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.name.islower():
            self.name = self.name.title()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number.startswith('0'):
            self.phone_number = '+996' + self.phone_number[1:]
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=256)
    experience = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.main_work}, опыт работы с {self.experience}'


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=256)
    has_own_notebook = models.BooleanField()
    os_choice = (('windows', 'Windows'), ('macos', 'MacOS'), ('linux', 'Linux'),)
    preferred_os = models.CharField(max_length=128, choices=os_choice)
    courses = models.ManyToManyField(Mentor, through='Course')

    def __str__(self):
        return f'{self.name} - {self.work_study_place}'


class Course(models.Model):
    name = models.CharField(max_length=128)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        return self.date_started.month + Language.month_to_learn
