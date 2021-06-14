## covidvaccineavailablity
This is an python program which gives you an system sound when the COVIDvaccine available and details about vaccine centers.
It provides availability details for next 7 days from the today date.
Here i have used  Co-win API  to get details about vaccine availability.

co-win apis:-https://apisetu.gov.in/public/marketplace/api/cowin

## Modules used in program

* Requests
* json
* datetime
* time
* schedule
* winsound

for installing modules
```
pip install requests
pip install json
pip install datetime
pip install time
pip install schedule
pip install winsound
```
## usage
From apisethu or co-win apis this program gets data of available vaccines,it takes the district id's to get details availability of vaccine in the given particular district id's.
you can get your district id's by knowing your state id we can obtain it by using this link

to get state id's we use :``` https://cdn-api.co-vin.in/api/v2/admin/location/states```

by just pasting this link in browser we can get our state id's

district id's we use : https://cdn-api.co-vin.in/api/v2/admin/location/districts/ +state id

for example:
  ``` https://cdn-api.co-vin.in/api/v2/admin/location/districts/32 ```
  
now after getting district ids we can add them to an array in main function called district  to get details of covid vaccine availability.

After adding details district ids we can run the program this will update you about vaccine availability and it will cheak for every 5 seconds for availability in given districts and notify by making an alert sound.
