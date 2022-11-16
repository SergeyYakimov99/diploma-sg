Веб-приложение — планировщик задач.

Шаг 1-2.
Создали приложение todolist. Добавили файл requirements.txt, установили зависимости, указанные в нем.
Шаг 3.
Установили библиотеку python-dotenv. Создали файл .env, в котором хранятся настройки по умолчанию.
Шаг 4-5.
Создали приложение core.
В файле core/models.py добавили модель пользователя, которая наследуется от 
AbstractUser.
Шаг 6.
Установили Postgres, подключились, сделали миграции, сформировали таблицы.
Шаг 7.
Создали суперюзера. В админке:
- Отобразили поля в списке
- Добавили поиск по полям
- Добавили фильтры по полям
- Скрыть поле Password.
- Сделать поля неизменяемыми: Last login, Date joined.
