#!/bin/bash

# Clone the repository
# git clone -b self-dist --single-branch https://github.com/WorshipMoon/hub-heweishi.git && \
# cd hub-heweishi/ && \
mkdir -p ./logs && \
sudo chown -R 1002:1002 ./logs && \
sudo chmod 755 ./logs && \
mv .env.example .env

# Check if all commands completed successfully
if [ $? -eq 0 ]; then
    echo "Setup completed successfully!"
    echo "Please configure your .env file with appropriate values."
else
    echo "An error occurred during setup."
    exit 1
fi