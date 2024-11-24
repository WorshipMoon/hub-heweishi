## django+postgres docker-compose 部署

1. 目录结构

- /my-project
    - /logs
    - gunicorn.conf.py
    - .env # source: .env.example
    - docker-compose.yml
    - docker-compose.self.yml # 可选


2. 启动
    ```shell
    docker-compose up -d
    ```

## gitaction 自动部署
查看 .github/workflows/hub-heweishi-image.yml
