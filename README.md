# Тестовое задание
### Фамилия Имя - Поваров Дмитрий 
### Тестовое задание:  
**Цель** -  Реализовать сервис загрузки изображений.  
**Функционал:**  
1. См. Общие требования; записью является изображение
2. Пользователь может загружать несколько изображений
3. По каждому изображению необходимо отображать количество
просмотров.  
Опционально:
1. Возможность добавить к каждому изображению тэги
2. Возможность фильтровать изображение по тэгам

Общие требования:
1. Авторизация: пользователь может регистрироваться в приложении,
авторизоваться и выходить из аккаунта
2. Требования к внешнему виду минимальные - приложение должно иметь
удобный, но не обязательно красивый интерфейс
Для WEB-приложения вместо графического интерфейса можно
реализовать REST API
3. Пользователь может создавать свои записи (в зависимости от задания),
просматривать и удалять; просмотр доступен для списка записей и для
каждой записи отдельно
4. Ролевая модель: пользователи делятся на обычных и администраторов
○ зарегистрироваться в качестве администратора нельзя, можно
только задать права вручную
○ администратор может просматривать/редактировать/удалять
любые записи любого пользователя
○ администратор может создавать/удалять/блокировать
пользователей
5. К исходному коду нужно приложить файл README.MD с кратким
описанием проекта, кто сделал, как запустить для проверки
6. Хранение данных реализовать
○ или в файлах - все создаваемые приложением файлы должны
быть добавлены в .gitignore проекта
○ или в БД - файлы миграций на создание таблиц должны быть в
проекте
7. Архивы, файлообменники, ссылки на Google Drive/OneDrive/Яндекс
Диск/Облако.Mail не принимаются - только репозитории в
GitHub/BitBucket
8. Git Flow:
○ кроме основной ветки master нужно создать ветку develop в
которой будет вестись вся разработка
○ публиковать изменения напрямую в master нельзя
○ практика Pull Request - законченные изменения оформляются в
pull request (merge request) из develop в master, для проверки
предоставляется ссылка на pull request
9. Разработка ведется на ООП  

**Как запустить проект**      
Скачать репозиторий, войти через консоль в папку, куда был скачан репозиторий и следовать следующим шагам:  

1. Для начала необходимо установить библиотеку virtualenv:

       pip install virtualenv
2. создать виртуальное окружение командой:
 
       virtualenv env
3. Примененить миграции:

       python manage.py migrate
4. Создание админки:

       python manage.py createsuperuser
5. А затем запустить сам сервис:

        python manage.py runserver
