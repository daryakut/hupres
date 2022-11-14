## Running Locally

Postgresql install:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew update
    brew install postgresql

Start/Stop/Restart Postgresql:
    
    brew services start postgresql
    brew services stop postgresql
    brew services restart postgresql

Create a local user and a database (enter password when prompted 123456)

    createuser --username=postgres --no-superuser --pwprompt --createdb hupres
    createdb -U hupres -h localhost -p 5432 hupres_dev

Create a test database for integ tests

    createdb -U hupres -h localhost -p 5432 hupres_test

Test database connection:

    psql -U hupres -W -d hupres_test -h localhost -p 5432

List Postgres users:

    psql -U postgres -h localhost -p 5432 -c "\du"

Install `pyenv` if necessary. Create the `pyenv` environment and activate it:

    pyenv virtualenv 3.10.3 hupres-monorepo-3.10
    pyenv activate hupres-monorepo-3.10

Install from `backend folder`:

    cd backend
    python -m pip install -r requirements.txt

Install gettext for localization

    brew install gettext

Run migrations:

    migrate_head.sh

Run locally on port 8000:

    ./run.sh
