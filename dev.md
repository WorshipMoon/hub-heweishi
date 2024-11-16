# Build and push script (build-push.sh)
#!/bin/bash
# Make the script executable with: chmod +x build-push.sh

# Set your registry and image details
REGISTRY="your-registry"  # e.g., docker.io/username or ghcr.io/username
IMAGE_NAME="django-app"
VERSION="1.0.0"

# Build the image
docker build -t $REGISTRY/$IMAGE_NAME:$VERSION .
docker tag $REGISTRY/$IMAGE_NAME:$VERSION $REGISTRY/$IMAGE_NAME:latest

# Push to registry
docker push $REGISTRY/$IMAGE_NAME:$VERSION
docker push $REGISTRY/$IMAGE_NAME:latest

# docker-compose.yml (for development)
version: '3.8'

services:
  web:
    image: ${REGISTRY:-local}/django-app:${VERSION:-latest}
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
      - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

```

To use this setup:

1. **Prepare Your Registry Account**
```bash
# Login to your registry (example for Docker Hub)
docker login

# For GitHub Container Registry
docker login ghcr.io
```

2. **Build and Push the Image**
```bash
# Edit build-push.sh with your registry details
chmod +x build-push.sh
./build-push.sh
```

3. **Pull and Run the Image**
```bash
# Pull the image
docker pull your-registry/django-app:latest

# Run the container
docker run -p 8000:8000 your-registry/django-app:latest
```

Key Features of this Setup:

1. **Multi-stage Build**
   - Uses builder stage to compile dependencies
   - Reduces final image size
   - Separates build dependencies from runtime

2. **Security Features**
   - Non-root user
   - Minimal base image
   - Only necessary dependencies

3. **Optimization**
   - .dockerignore to exclude unnecessary files
   - Wheel caching for faster builds
   - Layer optimization

4. **Development Support**
   - Volume mounting for local development
   - Environment variable configuration
   - Hot-reload support

To use different registries, modify the REGISTRY variable:

```bash
# For Docker Hub
REGISTRY="docker.io/yourusername"

# For GitHub Container Registry
REGISTRY="ghcr.io/yourusername"

# For Azure Container Registry
REGISTRY="yourregistry.azurecr.io"

# For Google Container Registry
REGISTRY="gcr.io/yourproject"
```

For production deployment, you might want to add a production docker-compose file:

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    image: ${REGISTRY}/django-app:${VERSION}
    restart: always
    environment:
      - DEBUG=0
      - DJANGO_ALLOWED_HOSTS=your-domain.com
    ports:
      - "8000:8000"
```

Would you like me to:
1. Add production-specific configurations?
2. Include GitHub Actions workflow for automated builds?
3. Add registry-specific authentication details?
4. Include more optimization techniques?