# Django Blog

## Установка и запуск

Открываем корень проекта в консоли и устанавливаем виртуальное окружение python

```bash
python -m venv virt
```

Запускаем виртуальное окружение

```bash
source virt/scripts/activate # для Windows
#или
source virt/bin/activate # для OS X и Linux
```

Устанавливаем все зависимости проекта

```bash
pip install -r requirements.txt
```

Теперь необходимо настроить базу данных. В файле /djangoblog/djangoblog/settings.py необходимо ввести данные вашей базы данных

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoblog', #имя вашей базы данных
        'USER': 'postgres', #имя пользователя базы данных
        'PASSWORD': '1234', #пароль
        'HOST': 'localhost', #хост
    }
}
```

Далее в консоли переходим в папку /djangoblog и выполняем миграцию

```bash
python manage.py makemigration

python manage.py migrate
```

Запускаем проект

```bash
python manage.py runserver
```
