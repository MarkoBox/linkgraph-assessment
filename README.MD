Notes:

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

