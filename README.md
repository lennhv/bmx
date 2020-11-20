# bmx
Django app to show UDI and Dollar statistics from BMX

You can see it at http://hvz.io/series/

# Documentation

This project is made in django and basically consumes the Baxico API https://www.banxico.org.mx/SieAPIRest/service/v1/ to obtain the information on the UDI and the exchange rate from Dollars to Pesos.

In order not to be consuming the Banxico API in each request made to the page, there is a scheduled task that downloads the information of the day and saves it in the database.

When installing the project, you must execute the `loadseries` command that is part of the application, in order to fill the database with historical information, as arguments it receives an initial date and an end date, for this demo we only have information from 2010 to date:

```python manage.py loadseries 2010-01-01 2020-11-19```



