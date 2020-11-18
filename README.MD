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

##1. Retrieve data from API and save it to your Django models. The database backend will be Postgres


Since this is a some kind of reporting service, we would use dimensional modeling to define a star schema for our data.
###Models:
**ApiCallHistory** table is used as a staging table. This can be optimized as to use no indexes or 
to drop and recreate indexes in order to speed up insertion.


**TradeData** table is our fact table. It contains trade history data. 
For simplicity im only modeling two columns we need for reporting ( currency_volume, weighted_price, update_time).

**Coin** table is our dimension table. It contains only ticker symbol.

###Model Managers:

For demonstration purposes and since api call code is really simple i'm coupling it with model manager. 

