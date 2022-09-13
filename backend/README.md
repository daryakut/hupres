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

    createuser --username=postgres --no-superuser --pwprompt --createdb my_user
    createdb hupres_test

Test database connection:

    psql -U hupres -P 123456 -d hupres_test -h localhost -p 5432

Install:

    python -m pip install -r requirements.txt

Run (specifying port is optional):

    uvicorn app:app --port=8000


## Heroku

The app can be deployed to [Heroku](https://heroku.com) using free resources, however you will need to establish your
account first. Once you have an account, you can click the button here to deploy to Heroku:

1. Log into (or create) your Heroku account
2. Click this button [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bennylope/python-deployments-hello-world)
3. Enter a name for your app (it will need to be unique across all of Heroku)
4. Choose your region
5. Click "Deploy app"

Alternatively, fork this repository, create a Heroku app in your Heroku dashboard, then Git push to that repository.

1. Fork this repository in your GitHub account
1. Log into (or create) your Heroku account
2. Click "New" then select "Create new app"
3. Enter a name for your app (it will need to be unique across all of Heroku)
4. Choose your region and click Deploy
5. Select "Connect to GitHub", choose your fork and click "Connect"
