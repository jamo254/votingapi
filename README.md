# REST API для системы голосования

# Как работает API:
 
 ## API позволяет:

   - Создание, обновление и удаление вопросов опроса;
   - Получение деталей вопроса
   - Фильтрация вопросов по идентификатору
   - Создание выбора для конкретного вопроса
   - Просмотр вопроса со всеми доступными вариантами
   - Голосование по конкретному вопросу
   - Просмотр результатов конкретного вопроса опроса

## Инструкции по локальному развертыванию приложения

1. Клонируйте этот репозиторий или загрузите Zip-файл проекта
2. Создайте виртуальную среду «Виртуальную среду» с именем «votingevn», которая будет работать с определенной версией python:
   - python3 -m venv votingenv 
   - как только виртуальная среда будет создана, перейдите в папку и активируйте виртуальную среду:  source votingevn/bin/activate
3. Откройте приложение с помощью редактора кода
   - Запустите сервер, используя следующую команду: python manage.py runserver
   - Вы можете получить доступ к панели администратора(admin), используя следующий URL-адрес http://127.0.0.1:8000/admin/

# Tестирования API
  - Можно тестировать API с помощью Postman, Swagger, Python shell или любых других инструментов.

Test results

### Создание вопроса для опроса
 ```POST create_question  - Создание вопрос опроса```
 
 ```http://127.0.0.1:8000/questions/```
 
```javascript
  {
    "title": "Food",
    "poll_question": "What is your favorite food?",
    "start_date": "2020-10-21T00:00:00Z",
    "end_date": "2021-10-25T17:50:57.424231Z"
  }
 ```
 #### Ошибка создания вопроса
 ```javascript
  {
     "title": [
         "This field is required."
     ],
     "poll_question": [
         "This field is required."
     ],
     "start_date": [
         "This field is required."
     ],
     "end_date": [
         "This field is required."
     ]
 }
  ```
  ### Получение деталей вопроса
  ```GET Fetching Questions - Получение деталей вопроса```
  ```http://127.0.0.1:8000/questions/ ```
  
   ```javascript
    [
  {
    "id": 2,
    "title": "Countries",
    "poll_question": "What is the capital of Japan?",
    "start_date": "2020-10-21T00:00:00Z",
    "end_date": "2021-10-25T17:50:57.424231Z",
    "choices": [
      {
        "poll_question_choice": "RnB"
      },
      {
        "poll_question_choice": "RnB"
      },
      {
        "poll_question_choice": "RnB"
      }
    ]
  },
  {
    "id": 3,
    "title": "Tourism",
    "poll_question": "Which is the best time to visit your town?",
    "start_date": "2020-11-05T00:00:00Z",
    "end_date": "2021-10-25T17:50:57.424231Z",
    "choices": [
      {
        "poll_question_choice": "Summer"
      }
    ]
  }
  
   ]
   ```
   ### Фильтрация вопросов по идентификатору (id)
   ```GET Fetch Questions by ID - Фильтрация вопросов по идентификатору ```
   ```http://127.0.0.1:8000/questions/3/ ```
   ```javascript
    {
     "id": 3,
     "title": "Tourism",
     "poll_question": "Which is the best time to visit your town?",
     "start_date": "2020-11-05T00:00:00Z",
     "end_date": "2021-10-25T17:50:57.424231Z",
     "choices": [
         {
             "poll_question_choice": "Summer"
         }
     ]
 }
```
### Обновление Вопрос
```PATCH Editing a question - Обновление Вопрос```
``` javascript
  {
      "title": "Travel",
      "poll_question": "Which country would you like to visit?"
  }

```
### Удаление вопросов опроса
```DEL Deleting a question - удаление вопрос```
```http://127.0.0.1:8000/questions/4/```
##### Ответ
```javascript 
"Вопрос удален" ```



