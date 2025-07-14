#!/bin/bash

# Остановка и удаление контейнеров
docker compose -f /var/www/loadLiner/docker-compose.prod.yml down &
wait

# Удаление и создание docker volume
docker volume rm static-volume
docker volume create static-volume

# Запуск контейнеров с пересборкой
docker compose -f /var/www/loadLiner/docker-compose.prod.yml up --build -d &
wait

echo "Все контейнеры успешно перезапущены."