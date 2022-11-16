#!/bin/bash

pushd backend

Echo "Compiling translations..."
./compile_translations.sh

popd

HUPRES_ENV="production"

# Docker repository and tag name
REPO="hupres/hupres-monorepo"

# Services in docker-compose.yml
SERVICES=("backend" "frontend")

# Iterate over services and build/push images
for SERVICE in "${SERVICES[@]}"; do
  # Build the Docker image
  docker-compose build "$SERVICE" --no-cache

  # Push the image to the Docker repository
  docker push "$REPO:$SERVICE"

  # Remove the local image (optional)
  # docker rmi "$IMAGE_NAME"
done
