#!/bin/bash

mkdir -p ./logs && \
sudo chown -R 1002:1002 ./logs && \
sudo chmod 755 ./logs && \
mv .env.example .env && \
sudo chown -R 1002:1002 .env && \
sudo chmod 755 .env && \
sudo chown -R 1002:1002 gunicorn.conf.py && \
sudo chmod 755 gunicorn.conf.py

# Check if all commands completed successfully
if [ $? -eq 0 ]; then
    echo "Setup completed successfully!"
    echo "Please configure your .env file with appropriate values."
else
    echo "An error occurred during setup."
    exit 1
fi