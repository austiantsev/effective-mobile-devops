# Effective Mobile DevOps

## Как запустить

1. Клонировать репозиторий:
git clone https://github.com/austiantsev/effective-mobile-devops.git
cd effective-mobile-devops

2. Запустить контейнеры:
docker compose up --build

## Как проверить результат

curl http://localhost

Ожидаемый ответ: Hello from Effective Mobile!

## Как работает схема

Запрос от пользователя поступает на nginx по порту 80.
Nginx проксирует его на backend по порту 8080 внутри Docker-сети.
Backend возвращает текст "Hello from Effective Mobile!".


Порт 8080 не доступен снаружи — только nginx может обращаться к backend.