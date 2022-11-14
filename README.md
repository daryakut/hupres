# Running locally

The app can be run locally with or without docker. Without docket is best for development
because backend and frontend instantly refresh after any changes and start up quickly.

The benefits of Docker is that the setup would be equivalent to that of production, so
I recommend you only run as docker for testing before release.

## Running without Docker

Run each backend and frontend apps separately. See the corresponding README.md
files for each app for more details.

## Running with Docker

Install docker depending on your system. On Mac it's best to install Docker Desktop. 

Make sure you have the right port in environment variables, 
which will be used to access the app from the browser.

    export HUPRES_APP_PORT="8080"

Then, start the docker container with:

    ./start-docker-dev.sh
    
# Deployment in AWS

## Prepare AWS RDS Postgresql instance

Create a Postgresql instance in AWS RDS https://us-east-2.console.aws.amazon.com/rds/home?region=us-east-2#databases:

When creating the DB, enable public access to simplify running migrations locally
  * Use postgres-security-group that allows access to 5432 port
  * Specify `hupres` as the user and very long random string as password

Next, add prod credentials to your `~/.bashrc`:

    export HUPRES_POSTGRES_USERNAME="hupres"
    export HUPRES_POSTGRES_PASSWORD="<your long password>"
    export HUPRES_POSTGRES_HOSTNAME="<hostname from AWS RDS page>"
    export HUPRES_POSTGRES_PORT="5432"
    export HUPRES_POSTGRES_DATABASE_NAME="hupres_prod"

Then, run `bash` to reload the environment variables and try accessing the database:

    psql -U $HUPRES_POSTGRES_USERNAME -h $HUPRES_POSTGRES_HOSTNAME -p 5432 -d postgres
    
If the connection succeeds, create the `hupres_prod` database:

    CREATE DATABASE hupres_prod;

Then, run the migrations. They should pick up the prod credentials from the environment

    cd backend && ./migrate_head.sh

Test database connection and migrations:

    psql -U $HUPRES_POSTGRES_USERNAME -h $HUPRES_POSTGRES_HOSTNAME -p 5432 -d $HUPRES_POSTGRES_DATABASE_NAME
    select * from quizzes;

**Make sure to remove or comment-out prod credentials and run `bash` again**

## Prepare EC2 instance

Create an EC2 instance with Amazon Linux 2023 https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Home:
* Make sure to create ssh key for the instance and download it
* To ssh to the instance use `ssh -i /path/to/key.pem ec2-user@ec2.instance.hostname`

### Install Docker

First, ssh to the instance:

    `ssh -i /path/to/key.pem ec2-user@ec2.instance.hostname`

Install docker:

    sudo yum update -y
    sudo yum install docker -y
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -a -G docker ec2-user

Test installation:

    docker --version

Install Docker Compose:

    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

Test installation:
    
    docker-compose --version

Logout and log back in for `usermod` change to take effect.

### Add environment variables

Add the following environment variables to the EC2 instance with `vim ~/.bashrc`:

    export HUPRES_GOOGLE_0AUTH_CLIENT_ID="<prod value>"
    export HUPRES_GOOGLE_0AUTH_CLIENT_SECRET="<prod value>"
    export HUPRES_OPENAI_API_KEY="<prod value>"
    export HUPRES_SECRET_SESSION_KEY="<prod value>"
    export HUPRES_POSTGRES_USERNAME="hupres"
    export HUPRES_POSTGRES_PASSWORD="<your long password>"
    export HUPRES_POSTGRES_HOSTNAME="<hostname from AWS RDS page>"
    export HUPRES_POSTGRES_PORT="5432"
    export HUPRES_POSTGRES_DATABASE_NAME="hupres_prod"
    export HUPRES_APP_PORT="80"
    export HUPRES_PROD_HOSTNAME="http://chat.hupres.com"
    export HUPRES_ENV="production"

Run `bash` to reload the environment variables.

## Deploy recent changes

On the server, create `~/hupres-monorepo`:

    mkdir ~/hupres-monorepo

Copy `docker-compose.yml` to server from your local machine:

    cd /path/to/hupres-monorepo
    git pull
    scp -i /path/to/key.pem docker-compose.yml ec2-user@3.16.83.5:~/hupres-monorepo

Push the recent images:

    ./build-docker-prod-no-cache.sh

On the server, login and pull:

    docker login
    docker-compose pull

Then, start up the app and start recording the logs to a file:

    docker-compose up -d && docker-compose logs -f > docker-compose.log &

To shut down docker, run from `~/hupres-monorepo`:

    docker-compose down

# Development

Favicon, a few nice resources:
* https://editsvgcode.com/
* https://www.freeconvert.com/svg-to-ico
