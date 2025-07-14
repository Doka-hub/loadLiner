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

----

### Obtaining initial SSL certificates:

Mount http.conf instead of https.conf to nginx service in Compose
docker compose up nginx -d
docker compose run --rm certbot certonly --webroot -w /var/lib/letsencrypt --agree-tos -m jenilpenil@gmail.com -d crmtrack.biz -d www.crmtrack.biz -n
Change nginx config mount back to https.conf, configure domain name as required
Renewal of exisitng certificates:

docker compose -f /home/admin/tg-shop-technics/docker-compose.yml up -d certbot

Cron version (weekly at 03:30am):

30 3 */7 * * /usr/bin/docker compose -f /home/admin/tg-shop-technics/docker-compose.yml up -d certbot

