#!/bin/bash

echo "Building Docker image..."
docker build -t selenium-headless-test .

if [ $? -ne 0 ]; then
    echo " Docker build failed!"
    exit 1
fi

echo "Running Docker container..."
docker run --rm selenium-headless-test

if [ $? -ne 0 ]; then
    echo " Docker run failed!"
    exit 1
fi

echo "✅ Test completed successfully!"
