#!/bin/bash

# Set your Docker Hub username
DOCKER_USERNAME="shivanshu1333"

# Set the version/tag for the images
VERSION="latest"

# Login to Docker Hub (you'll be prompted for password)
echo "Logging in to Docker Hub..."
docker login -u "$DOCKER_USERNAME"

# Build and push celery-app image
echo "Building celery-app image..."
docker build -t "$DOCKER_USERNAME/celery-app:$VERSION" .
echo "Pushing celery-app image..."
docker push "$DOCKER_USERNAME/celery-app:$VERSION"

# Build and push flower image
echo "Building flower image..."
docker build -t "$DOCKER_USERNAME/celery-flower:$VERSION" ./flower
echo "Pushing flower image..."
docker push "$DOCKER_USERNAME/celery-flower:$VERSION"

# Build and push task-generators image
echo "Building task-generators image..."
docker build -t "$DOCKER_USERNAME/task-generators:$VERSION" ./task_generators
echo "Pushing task-generators image..."
docker push "$DOCKER_USERNAME/task-generators:$VERSION"

echo "All images have been built and pushed successfully!" 

shivanshu1333/task-generators

shivanshu1333/celery-app

shivanshu1333/celery-flower