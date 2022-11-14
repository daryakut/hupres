# host.docker.internal is the hostname of the host machine from within the docker container
# development_docker is the environment for running docker locally
HUPRES_POSTGRES_HOSTNAME="host.docker.internal" HUPRES_ENV="development_docker" docker-compose up --build
