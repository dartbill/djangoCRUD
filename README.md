# Basic Django CRUD

## Install

- `pipenv shell`
- `pipenv install`

## Usage

- `Python manage.py runserver ` -> runs on localhost 8000
- Deployed server here -> https://djangotestfp.herokuapp.com/

## Routes

- index/ -> gets all db
- index/`<id>` -> shows cat based on id
- index/new/ -> takes in json to create a new cat
- update/`<id>` -> takes in json to update cat based on id
- delete/`<id>` -> deletes the cat chosen by id 
