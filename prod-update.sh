#!/bin/bash
# To be run on the production host

echo "Stopping docker"
docker-compose down

echo "Pulling newest images"
docker-compose pull

echo "Starting docker"
docker-compose up -d

echo "Recording logs"
docker-compose logs -f > docker-compose.log &
