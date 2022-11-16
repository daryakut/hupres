#!/bin/bash

Echo "Compiling translations..."
./compile_translations.sh

export HUPRES_ENV=development
uvicorn app:app --port=8000 --reload
