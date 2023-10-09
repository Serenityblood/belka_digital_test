# belka_digital_test

## Установка

1. Создать файл .env по примеру env.example
2. В корневой директории проекта
```
docker-compose up -d --build
```

## Опсиание
Доступны 3 эндпоинта:
- http://127.0.0.1:8000/api/v1/raw/ - добавление данных о сырье(POST)
- http://127.0.0.1:8000/api/v1/fromexcel/ - добавление данных о сырье через Excel таблицу(POST)
- http://127.0.0.1:8000/api/v1/report/ - формирование отчета за месяц(POST)

Эндпоинты для работы с пользователями:
- http://127.0.0.1:8000/auth/users/ - регистрация
- http://127.0.0.1:8000/auth/jwt/create/ - получение токена авторизации(Auth Header = Bearer)

### Подробнее об эндпоинтах:
1. http://127.0.0.1:8000/api/v1/raw/ - добавление данных о сырье(POST)
* Пример запроса с необходимыми полями:
```
{
    "month": "апрель",
    "name": "Ferrum",
    "iron_con": 0.1,
    "silicon_con": 0.5,
    "aluminum_con": 0.025,
    "calcium_con": 0.1,
    "sulfure_con": 0.2
}
```
* Пример ответа:
```
{
    "id": 4,
    "author": 1,
    "name": "Ferrum",
    "iron_con": 0.1,
    "silicon_con": 0.5,
    "aluminum_con": 0.025,
    "calcium_con": 0.1,
    "sulfure_con": 0.2,
    "month": "апрель"
}
```
2. http://127.0.0.1:8000/api/v1/fromexcel/ - добавление данных о сырье через Excel таблицу(POST)
* В таблице должны быть необходимые колонки с данными: month, name, iron_con, silicon_con, aluminum_con, sulfure_con
* Не более одного наименования сырья за раз(можно исправить)
3. http://127.0.0.1:8000/api/v1/report/ - формирование отчета за месяц(POST)
* Пример запроса с необоходимыми полями:
```
{
    "month": "апрель"
}
```
* Пример ответа:
```
{
    "iron_con__avg": 0.15000000000000002,
    "iron_con__min": 0.1,
    "iron_con__max": 0.2,
    "silicon_con__avg": 0.4,
    "silicon_con__min": 0.3,
    "silicon_con__max": 0.5,
    "aluminum_con__avg": 0.0175,
    "aluminum_con__min": 0.01,
    "aluminum_con__max": 0.025,
    "calcium_con__avg": 0.2,
    "calcium_con__min": 0.1,
    "calcium_con__max": 0.3,
    "sulfure_con__avg": 0.15000000000000002,
    "sulfure_con__min": 0.1,
    "sulfure_con__max": 0.2,
    "month": "апрель"
}
```
