## django+postgres docker-compose 部署

1. 目录结构

- /my-project
    - /logs
    - gunicorn.conf.py
    - .env.example
    - docker-compose.yml
    - docker-compose.self.yml # alternative
    - setup.sh

    ```shell
    git clone git@github.com:WorshipMoon/hub-heweishi.git
    ```

2. 启动

    ```shell
    sudo chmod +x setup.sh
    ./setup.sh
    docker-compose up -d
    ```

## gitaction 自动部署
查看 .github/workflows/hub-heweishi-image.yml
