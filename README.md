# coronavirus

Just a prototype program

Scraps data from wikipedia about the coronavirs.
Push data into database, columns are country, cases, deaths, recoverd.

You can run both files just like: python3 scraper.py
                                  python3 database_api.py
                                  
When database_api.py is run daily data is pusht into database and is stored permanently.
The data pushed into database are type string.

The data can be plot with matplotlib



FIRST USAGE:

python3 scraper.py

It scraps the data from wikipedia and constructs a python table that can be used by a python class "Wikipedia"

Once the Wikipedia is initialized you can access the instance like a python class.

It give you a table with data rapresenting the coronavirus data, table columns are: country, cases, deaths, recoverd.




SECOND USAGE:

pyhton3 database_api.py

It scraps the data from wikipedia

It pushes the data into a sqlit3 database.

Than it asks you for a country.

    if you want to se data for china pleas enter the name as "china_"
    
    for countries with spaces in their names like "United States" pleas replace the space with underscore like "United_States"
    
Than it asks you for what kind of data you want to see, cases, deaths, recoverd.

Than it prints out the data
