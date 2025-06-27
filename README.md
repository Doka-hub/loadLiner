# LoadLiner Logistics

This project uses Django and Wagtail CMS. A Docker setup with Nginx and PostgreSQL is provided for a production-like deployment, for example to a Digital Ocean Droplet.

## Running with Docker Compose

1. Copy the example environment files and adjust values as needed:

   ```bash
   cp .env.distr .env
   cp .env.db.distr .env.db
   ```

2. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

Nginx will expose the application on [http://localhost:8000](http://localhost:8000).
