# Django + Stripe API — Тестовое задание

Простой Django-проект, интегрированный с [Stripe](https://stripe.com), реализующий базовую eCommerce-логику:

* просмотр товара
* оплата через Stripe Checkout

## Стек

* Django 4+
* Stripe Python SDK
* HTML + JS (stripe.redirectToCheckout)
* Render (деплой)

## Установка и запуск локально

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Создайте и активируйте виртуальное окружение
```bash
python -m venv venv

Linux: source venv/bin/activate  
Windows: venv\Scripts\activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Создайте файл .env
```
SECRET_KEY=your-django-secret-key
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
DEBUG=True
```
5. Проведите миграции и создайте суперпользователя (для админки)
```bash
python manage.py migrate
python manage.py createsuperuser
```
6. Запустите сервер
```bash
python manage.py runserver
```

## Как работает

### Страница товара: `/item/<id>`

- Показывает название, описание, цену и кнопку "Buy"
- При клике на "Buy":
  - JS делает запрос на `/buy/<id>`
  - Получает `session.id`
  - Редиректит пользователя на Stripe Checkout через `stripe.redirectToCheckout`

### GET/buy/{id}
- Создаёт Stripe Session и возвращает session.id в JSON формате.


## Сайт: [stripe-api-project.onrender.com](https://stripe-api-project.onrender.com)
### Пример товара:  
https://stripe-api-project.onrender.com/item/1

### Пример `.env` доступен в файле `.env.example`