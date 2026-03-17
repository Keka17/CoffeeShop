# Django CoffeeShop Site <img width="125" height="75" alt="django-bootstrap-Photoroom" src="https://github.com/user-attachments/assets/787c3f28-00a8-4370-b0b5-052d9a7e6baf" />


Веб-сайт локальной кофейни с основной информацией: адрес, способы связи, меню. 
Дополнительно добавлен раздел с изображениями и используемыми кофейными зернами. 
Основная информация взята с сайта https://www.schroederstore.com/red-bank-coffeehouse.

## Технологии:
- _Python 3.11+_
- Backend: _Django 5.2.12_
- Frontend: _Bootstrap 5.3_
- Database: _SQLite3_ (по умолчанию)

## Установка и запуск
**Локальный запуск**
  1. Клонирование репозитория:
     
     ```bash
     git clone https://github.com/Keka17/CoffeeShop.git
     
     cd CoffeeShop
     ```
  2. Создание виртуального окружения:
     
     ```bash
     python -m venv venv
    
     source venv/bin/activate  # Для Linux/Mac
    
     venv\Scripts\activate  # Для Windows
     ```
  3. Установка зависимостей:
     
     ```bash
      pip install -r requirements.txt
     ```
  4. Настройка переменных окружения:
 
     В корневой папке проекта создайте файл `.env`, заполнив его в соответствии с файлом `.env.example`.
  
  5. Запуск сервера:
     
     ```bash
     cd website
     
     python manage.py runserver
     ```
**Запуск через Docker**

  1. Клонирование репозитория:
     ```bash
     git clone https://github.com/Keka17/CoffeeShop.git
     
     cd CoffeeShop
     ```
  2. Настройка переменных окружения:
     В корневой папке проекта создайте файл `env.docker`, заполнив его в соответствии с файлом `.env.example`.
    
  3. Сборка и запуск

     ```bash
     docker build -t coffeeshop-app .
     
     docker run -p 8000:8000 --env-file .env coffeeshop-app
     ```
     
## Доступ к приложению
После успешной сборки и запуска приложение будет доступно по адресу: http://localhost:8000/.

### Примечание
Для манипуляции с базой данных достаточно перейти в админ-панель (http://localhost:8000/admin/); пользователь-администратор уже находится в базе:

```bash
Username: admin

Password: admin
```

## Демонстрация сайта
![website](https://github.com/user-attachments/assets/ec5c9788-47bd-4fd8-8335-08222e2cb4c0)




  
