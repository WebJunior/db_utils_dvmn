import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        school_grades = [4, 5]
        for mark in marks:
            mark.points = random.choice(school_grades)
            mark.save(update_fields=['points'])
    except ObjectDoesNotExist:
        print(f'Не смог найти школьника {schoolkid_name}')
    except MultipleObjectsReturned:
        print('Школьник то не уникальный!')


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisement:
            chastisement.delete()
    except ObjectDoesNotExist:
        print(f'Не смог найти школьника {schoolkid_name}')
    except MultipleObjectsReturned:
        print('Школьник то не уникальный!')


def create_commendation(subject, schoolkid_name):
    compliments = [
        'Молодец!',
        'Отлично!',
        'Самый лучший ученик!',
        'Очень хороший ответ!',
        'Ты сегодня прыгнул выше головы!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!'
    ]
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        lesson = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter,
                                       subject__title__contains=subject).order_by('-date').first()
        if lesson:
            Commendation.objects.create(
                                text=random.choice(compliments),
                                created=lesson.date,
                                schoolkid=child,
                                subject=lesson.subject,
                                teacher=lesson.teacher
                                )
        else:
            print(f'Не смог найти предмет {subject}')
    except ObjectDoesNotExist:
        print(f'Не смог найти школьника {schoolkid_name}')
    except MultipleObjectsReturned:
        print('Школьник то не уникальный!')
