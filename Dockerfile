# Dockerfile
# 第一阶段：构建阶段
FROM python:3.12-slim AS builder

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

# 安装构建依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 升级 pip
RUN pip install --upgrade pip

# 安装依赖
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

# 最终阶段
FROM python:3.12-slim

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=project.settings

WORKDIR /app

# 复制 wheel 文件
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/*

# 安装 gunicorn requirements已有
# RUN pip install gunicorn

# 复制项目文件
COPY . .

# 创建非-root用户并设置权限
RUN addgroup --system --gid 1002 django_user && \
    adduser --system --uid 1002 --gid 1002 --shell /bin/bash django_user && \
    mkdir -p /home/django_user && \
    chown -R 1002:1002 /home/django_user && \
    usermod -d /home/django_user django_user && \
    chown -R 1002:1002 /app

# # 创建 VS Code 工作目录
# RUN mkdir -p /home/django_user/.vscode-server && \
#     chown -R 1002:1002 /home/django_user/.vscode-server

# 确保日志目录的权限正确
RUN mkdir -p ./logs
RUN chown -R 1002:1002 /app/logs

# 切换到非-root用户
USER django_user

# 暴露端口
EXPOSE 8000

# 运行迁移并启动 gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn --config gunicorn.conf.py project.wsgi:application"]
# CMD ["sh", "-c", "python manage.py migrate && gunicorn project.wsgi:application --preload -b 0.0.0.0:5000"]
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]