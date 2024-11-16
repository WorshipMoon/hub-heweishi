## django+postgres docker-compose 部署

1. 目录结构

/my-project
│
├── .env # source: .env.example
├── docker-compose.yml
├── docker-compose.dev.yml # 可选
└── README.md

2. 启动

```shell
docker-compose up -d
```

## gitaction 自动部署
查看 .github/workflows/hub-heweishi-image.yml