#!/bin/bash

# Check if a parameter was provided
if [ $# -eq 0 ]; then
    echo "Please provide a migration name"
    exit 1
fi

migration_name="$1"
alembic revision --autogenerate -m "$migration_name"
