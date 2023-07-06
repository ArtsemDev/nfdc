## Запуск Nginx + Docker Compose + Certbot

1. Запускаем контейнеры (контейнер с certbot первый раз не поднимется ввиду отсутствия сертификатов)
2. Перезапускаем certbot руками для выпуска сертификатов

    `docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.org`
    
    ! Выпустить сертификат можно только при наличии зарегистрированного домена

3. Перезапускаем все контейнеры
4. Обновление сертификатов

    `docker compose run --rm certbot renew`