
# RatesTask 

## Overview

This is a Rates Calculator restful service built using Flask and Postgres db.

## Features

- Fetch Rates

## Technologies Used

- **Backend:**
  - Flask

- **Database:**
  - Postgres

## Configuration

- Environment variables can be configured in a `.env` file.  Sample template is provided 

## Setup

1. Clone the repository: `git clone https://github.com/Bisrat306/ratestask-tt.git`
2. Navigate to the project folder: `cd ratestask-tt`
3. Set up environment variables.
i.e Setup environment variables depending on the database connection being used. If using the dockerfile use the following 

```
DATABASE_USER=postgres
DATABASE_PWD=ratestask
DATABASE_NAME=postgres
DATABASE_HOST=127.0.0.1
ENV=dev
```
4. Install the necessary libraries: `pip install -r requirements.txt` 
    NB: Make sure to use the latest pip version `pip install --upgrade pip`
5. Run the following command: `export FLASK_APP=manage.py`
6. To Run the application: `python manage.py run` App will run on port `5000` 
    ```
    Sample command
    curl "http://127.0.0.1:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
    ```
    - Swagger documentation can also be found on `http://127.0.0.1:5000`
7. To Run test: `python manage.py test` 

## Changes made/Reccomended changes to DB
- Updated the TEXT data type for the codes(dest_code & origin_code) to 5 character data types. This will help save a lot of space on DB & betters performance. 
- Relationships exist but are not enforced by foreign key constraints. Like, ports & prices table. It will be useful for data integrity purposes.
 
## Authors

- [@bisrat306](https://www.github.com/bisrat306)