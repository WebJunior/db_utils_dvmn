# Databese utils

## Описание проекта
В данном проекте представлены полезные функции для изменения БД [электронного дневника](https://github.com/devmanorg/e-diary).

* Функция `fix_marks` 
    * Аргументы:
        * `schoolkid_name` - имя школьника.
    * Что делает:
        * Исправляет все плохие оценки ( которые меньше 4-ёх ), на хорошие.

* Функция `remove_chastisements`
    * Аргументы:
        * `schoolkid_name` - имя школьника.
    * Что делает:
        * Удаляет все замечания по ученику.

* Функция `create_commendation`
    * Аргументы:
        * `subject` - название предмета.
        * `schoolkid_name` - имя школьника.
    * Что делает:
        * Создаёт одну похвалу от учителя.
        
## Требования к окружению
Разработка велась на python [3.7.3](https://www.python.org/downloads/) + PyCharm. Также необходимо скачать себе репозиторий
[электронного дневника](https://github.com/devmanorg/e-diary).

## Как установить
Клонируете себе репозиторий [электронного дневника](https://github.com/devmanorg/e-diary) `git clone https://github.com/devmanorg/e-diary.git`.

## Запуск
Вополняете шаги из README [электронного дневника](https://github.com/devmanorg/e-diary). Запускаете сервер `python datacenter/manage.py runserver`.
Откройте терминал, войдите в  `shell` — `python datacenter/manage.py shell`.

Когда `shell` будет запущен, первым делом надо импортировать модули, которые нужны для работы - `import random`, `from datacenter.models import *`.

Всё, теперь можно вставлять нужные функции в `shell` и вызывать их оттуда. Например, когда перенесете функцию
`fix_marks` в `shell` , можно её вызвать так `fix_marks('Фролов Иван')`