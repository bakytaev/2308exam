import datetime
from user.models import Student, Mentor, Language, Course

languages = [
    {
        'name': 'Python',
        'months_to_learn': 6
    },
    {
        'name': 'Java Script',
        'months_to_learn': 6
    },
    {
        'name': 'UX-UI',
        'months_to_learn': 2
    },
]

students = [
    {
        'name': 'Amanov Aman',
        'email': 'aman@mail.ru',
        'phone_number': '+996700989898',
        'work_study_place': 'School №13',
        'has_own_notebook': True,
        'preferred_os': 'windows'
    },
    {
        'name': 'Apina Alena',
        'email': 'aapina@bk.ru',
        'phone_number': '0550888888',
        'work_study_place': 'TV',
        'has_own_notebook': True,
        'preferred_os': 'mac'
    },
    {
        'name': 'Phil Spencer',
        'email': 'spencer@microsoft.com',
        'phone_number': '0508312312',
        'work_study_place': 'Microsoft Gaming',
        'has_own_notebook': False,
        'preferred_os': 'linux'
    }
]

mentors = [
    {
        'name': 'Ilona Maskova',
        'email': 'imask@gmail.com',
        'phone_number': '0500545454',
        'main_work': None,
        'experience': datetime.date(year=2021, month=10, day=23)
    },
    {
        'name': 'Halil Nurmuhametov',
        'email': 'halil@gmail.com',
        'phone_number': '0709989876',
        'main_work': 'University of Fort Collins',
        'experience': datetime.date(year=2010, month=9, day=18)
    }
]

for language in languages.items():
    lan = Language.objects.create(name=language['name'], months_to_learn=language['months_to_learn'])

for student in students.items():
    stu = Student.objects.create(name=student['name'],
                                 email=student['email'],
                                 phone_number=student['phone_number'],
                                 work_study_place=student['work_study_place'],
                                 has_own_notebook=student['has_own_notebook'],
                                 preferred_os=student['preferred_os'],
                                 )

for mentor in mentors.items():
    men = Mentor.objects.create(name=mentor['name'],
                                email=mentor['email'],
                                phone_number=mentor['phone_number'],
                                main_work=mentor['main_work'],
                                experience=mentor['experience'],
                                )

for mentor in mentors.items():
    men = Mentor.objects.create(name=mentor['name'],
                                email=mentor['email'],
                                phone_number=mentor['phone_number'],
                                main_work=mentor['main_work'],
                                experience=mentor['experience'],
                                )

course1 = Course.objects.create()