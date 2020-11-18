Linkgraph project
==================

Deployment
----------

*Docker*

* Docker 17.05+
* Docker Compose 1.17+

Tested on Docker desktop community 2.2.0.0

Commands to run:

```bash
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py fetch_market_data
```

Main page is avaible at:
http://localhost:8000/

Api endpoint are at:

http://localhost:8000/api/trade-data

http://localhost:8000/api/coin


Notes:
-----

## 1. Retrieve data from API and save it to your Django models. The database backend will be Postgres


Since this is a some kind of reporting service, we would use dimensional modeling to define a star schema for our data.
### Models:
**ApiCallHistory** table is used as a staging table. This can be optimized as to use no indexes or 
to drop and recreate indexes in order to speed up insertion.


**TradeData** table is our fact table. It contains trade history data. 
For simplicity im only modeling two columns we need for reporting ( currency_volume, weighted_price, update_time).

**Coin** table is our dimension table. It contains only ticker symbol.

### Model Managers:

For demonstration purposes and since api call code is really simple is is contained inside model manager.
Model managers contain two methods for normalizing data from json.


## 2. Create a GraphQL API or Django Rest Framework APIs to expose this data for clients

Since we require top 20 currencies api endpoint is selecting only those last updated, sorting them by weighted price,
and excluding null values.
Pagination is set to 20 so we can limit the view on graph to top 20 and still fetch rest of the data from same endpoint.

## 3. Write one test case to verify your API endpoint is responding with a server 200.

Simple test written in market_data/tests.py

## 4. Frontend

Frontend is done via Django templates using javascript to fetch data from api on page load.

## 5. Period task

Period task is setup as shared tasks in market_data/task.py file
Second function there is used by fetch_market_data command in market_data/management/commands

## 6. Docker compose 

Docker compose file is used to spin up 5 containers (web app, db, redis, celery and celery beat)
Docker file is inside compose folder.

Thanks for reading :)
