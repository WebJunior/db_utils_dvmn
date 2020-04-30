# Database utils

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
Разработка велась на python [3.7.3](https://www.python.org/downloads/) + IDE PyCharm. Также необходимо скачать себе репозиторий
[электронного дневника](https://github.com/devmanorg/e-diary).

## Как установить
Клонируете себе репозиторий [электронного дневника](https://github.com/devmanorg/e-diary) командой:

`git clone https://github.com/devmanorg/e-diary.git`

## Запуск
Выполняете шаги из README [электронного дневника](https://github.com/devmanorg/e-diary). Сайт должен быть запущен.
Положите `db_utils.py` рядом с `manage.py`
Потом откройте терминал, нужно войти в `shell` командой:

`python manage.py shell`

Когда `shell` будет запущен, введите импорт:

`import db_utils as hack`

Всё, теперь можно вызывать нужные нам функции. Например:

    hack.fix_marks('Громов Зосима')
    hack.remove_chastisements('Громов Зосима')
    hack.create_commendation('Математика', 'Громов Зосима')

