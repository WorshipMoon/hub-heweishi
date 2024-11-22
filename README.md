## django+postgres docker-compose 部署

1. 目录结构

    /my-project<br>
    │<br>
    ├── /logs<br>
    |—— gunicorn.log<br>
    ├── .env # source: .env.example<br>
    ├── docker-compose.yml<br>
    └── docker-compose.dev.yml # 可选<br>


2. 启动

    ```shell
    docker-compose up -d
    ```

## gitaction 自动部署
查看 .github/workflows/hub-heweishi-image.yml
