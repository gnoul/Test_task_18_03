I. Python/Flask приложение редактирования списка пользователей:

При запуске создается пользователь **admin** с паролем `QWEqwe123`
Сохранение списка пользователей доступна только активным пользователям с свойством is_staff равным True.

Для проверки можно использовать docker-compose. Для запуска нужно выполнить
``` shell
docker-compose up --build
```
Сервис будет доступен по адресу [http://localhost:5001/](http://localhost:5001/)