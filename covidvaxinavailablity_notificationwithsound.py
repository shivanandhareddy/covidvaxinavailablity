import requests
import json
import datetime
import time
import schedule
import winsound
from datetime import date
date = date.today()


def slots(districtid):
    pdate= date.strftime("%d-%m-"+'20'+"%y")
    #getting date of today
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"
    # url from api setu
    districtid=str(districtid)
    finalurl=url + "district_id=" + districtid + "&date=" + pdate
    #adding date and district to url api
    res=requests.get(finalurl)
    #requesting url data
    x=res.json()
    #getting url data
    if(bool(x['centers'])):
        output=[]
        cent=x['centers']
        #traversing in centers
        for i in cent:
            ses=i['sessions']
            #traversing in sessions
            for j in ses:
                if(j['available_capacity']>0 and j['min_age_limit']==18):
                    #can change age limit to >18 for all ages
                    if(j['available_capacity_dose1']>0):
                    #if(j['available_capacity_dose2']>0):--for dose 2
                        
                        result={ "pincode":i['pincode'],'District_name':i["district_name"],'Center_Name': i['name'], 'Block_name':i['block_name'],'Age_limit':j['min_age_limit'], 'Vaccine_type':j['vaccine'] ,'Date':j['date'],'Available_capacity':j['available_capacity'],'Fee_type':i['fee_type'],'available_capacity_dose1':j['available_capacity_dose1']}
                        #add ''available_capacity_dose1':j['available_capacity_dose1']' at last of result for dose 2 
                        output.append(result)
        if(len(output)==0):
            pass
            print('no centers available')
        else:
            c=0
            for o in output:
                c=c+1
                k=str(o)
                s=str(k)
                s=s.replace(',','\n').replace('{','').replace('}','').replace("'",'') #formating output
                print('\n'+str(c)+':'+s)
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)#notification sound
    else:
        print('not available')
def main():
    arr=[581,603]
    #district-ids
    a=['Hyd','RR']
    #district-names
    for i in range(len(arr)):
        print("\n"+'.'*10+str(arr[i])+'----'+a[i]+'.'*10+"\n")
        try:
            slots(arr[i])
        except: 
            print("An error occured--chek connection") 
        #requesting for slots availablity by district id
    print("-"*20+'+'*20,'-'*5,datetime.datetime.now().strftime('%I:%M:%S'))
main()    
def sheduler():
    schedule.every(5).seconds.do(main)#shedule total program for every 5 seconds
    #schedule.every(1).minutes.do(main)---  shedule total program for every 1 minutes
    while True:
        schedule.run_pending()
        time.sleep(1)
sheduler()

