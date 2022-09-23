## Running Locally

Postgresql install:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew update
    brew install postgresql

Start/Stop/Restart Postgresql:
    
    brew services start postgresql
    brew services stop postgresql
    brew services restart postgresql

Create a user and a database (enter password when prompted 123456)

    createuser --username=postgres --no-superuser --pwprompt --createdb hupres
    createdb -U hupres -h localhost -p 5432 hupres_test

Test database connection:

    psql -U hupres -W -d hupres_test -h localhost -p 5432

List Postgres users:

    psql -U postgres -h localhost -p 5432 -c "\du"

Install:

    python -m pip install -r requirements.txt

Run (specifying port is optional):

    uvicorn main:main --port=8000


## Heroku

The main can be deployed to [Heroku](https://heroku.com) using free resources, however you will need to establish your
account first. Once you have an account, you can click the button here to deploy to Heroku:

1. Log into (or create) your Heroku account
2. Click this button [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bennylope/python-deployments-hello-world)
3. Enter a name for your main (it will need to be unique across all of Heroku)
4. Choose your region
5. Click "Deploy main"

Alternatively, fork this repository, create a Heroku main in your Heroku dashboard, then Git push to that repository.

1. Fork this repository in your GitHub account
1. Log into (or create) your Heroku account
2. Click "New" then select "Create new main"
3. Enter a name for your main (it will need to be unique across all of Heroku)
4. Choose your region and click Deploy
5. Select "Connect to GitHub", choose your fork and click "Connect"
