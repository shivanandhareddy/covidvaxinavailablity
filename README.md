## covidvaxinavailablity
This is an python program which gives you an system sound when the COVIDvaxin avilable and details about vaxin centers.
It provides availablity details for next 7 days from the todays date.
Here i have used  Cowin api  to get details about vaxin availablity.

cowin apis:-https://apisetu.gov.in/public/marketplace/api/cowin

## Moduels used in program

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
From apisethu or cowin apis this program gets data of avilable vaxins,it takes the district id's to get details avilablity of vaxin in the given particular district id's.
you can get your district id's by knowing your state id we can obtain it by using this link

to get state id's we use :``` https://cdn-api.co-vin.in/api/v2/admin/location/states```

by just pasting this link in browser we can get our state id's

district id's we use : https://cdn-api.co-vin.in/api/v2/admin/location/districts/ +state id

for example:
  ``` https://cdn-api.co-vin.in/api/v2/admin/location/districts/32 ```
now after getiing distictict ids we can add them to an array in main function called district ids to get detais of covid vaxin availablity
