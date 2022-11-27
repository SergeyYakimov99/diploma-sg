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

DZ-34.
Написали Dockerfile и docker-compose.yaml, запустили 4 контейнера.
Создали специального пользователя deploy c правами администратора.
  <adduser deploy>
Завели файл в проекте 
.github/actions/action.yaml
Внутри него описали джобу, которая:
Собирает образ с помощью docker build
Выполняет логин в Docker Hub с помощью docker login
Отправляет образ в Docker Hub с помощью docker push
Каждая следующая сборка должна тегировать образ новым тегом (с помощью переменной $GITHUB_RUN_ID).
Создаем новый 'docker-compose-ci.yaml', в котором будет задана конфигурация для разворачивания на сервере:
Заменяем секции build на секции Image с такими же версиями, как при сборке приложения.
Заводим все необходимые секреты в GitHub:
логин и пароль для подключения по SSH (пользователь deploy, созданный на шаге 3);
логин, пароль, название БД (будет использоваться в файле 'docker-compose-ci.yaml' и в конфигурации вашего приложения);
любые другие чувствительные данные.
Добавляем джобу по рендеру 'docker-compose-ci.yaml' и файл конфигурации c помощью envsubst.
Добавляем джобу по копированию двух предыдущих файлов на сервер через SCP.
Добавляем джобу по запуску docker-compose up на самом сервере через SSH.
Установили DRF и добавили его в зависимости (requirements.txt) с указанием версии.
В приложении Core добавили urls.py и в файле todolist/urls.py включили urls из приложения Core.