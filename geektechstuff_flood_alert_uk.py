# geektechstuff
# UK Flood Details

import requests
import json

def flood_user_input():
    # checks flood details near by
    atlantis =""
    input_lat = input('Enter Latitude: ')
    input_long = input('Enter Longitude: ')
    distance = input('How close to the latitude / longitude should be seached?: ')
    flood_url = 'http://environment.data.gov.uk/flood-monitoring/id/floods'
    flood_parameters = '?lat='+input_lat+'&long='+input_long+'&dist='+distance
    flood_query = flood_url+flood_parameters
    get_data = requests.get(flood_query)
    get_data.raise_for_status()
    analysis = get_data.json()
    items = analysis["items"]
    river = items[0]["floodArea"]["riverOrSea"]
    severity = items[0]["severity"]
    # severity level 1 is severe, 2 is flood warning, 3 is flood alert and 4 is warning no longer in force
    s_level = items[0]["severityLevel"]
    message = items[0]["message"]
    time_severity_changed = items[0]["timeSeverityChanged"]
    if s_level >=3:
        severity=str(severity)
        s_level=str(s_level)
        message=str(message)
        time_severity_changed=str(time_severity_changed)
        atlantis = "\nWARNING \n \n"+river+"\n \n"+"Severity level is at "+s_level+"\n \n"+severity+"\n \n"+message+"\n \n"+"Last update: "+time_severity_changed+"\n"
    else:
        atlantis = "All OKAY"
    return(atlantis)

def auto_flood_check():
    # checks flood details near by
    # Replace XXXXXXX  with latitude and longitude
    atlantis = ""
    flood_query = 'http://environment.data.gov.uk/flood-monitoring/id/floods?lat=XXXXXXX&long=XXXXXXX&dist=1'
    get_data = requests.get(flood_query)
    get_data.raise_for_status()
    analysis = get_data.json()
    items = analysis["items"]
    river = items[0]["floodArea"]["riverOrSea"]
    severity = items[0]["severity"]
    # severity level 1 is severe, 2 is flood warning, 3 is flood alert and 4 is warning no longer in force
    s_level = items[0]["severityLevel"]
    message = items[0]["message"]
    time_severity_changed = items[0]["timeSeverityChanged"]
    if s_level >=3:
        severity=str(severity)
        s_level=str(s_level)
        message=str(message)
        time_severity_changed=str(time_severity_changed)
        atlantis = "\nWARNING \n \n"+river+"\n \n"+"Severity level is at "+s_level+"\n \n"+severity+"\n \n"+message+"\n \n"+"Last update: "+time_severity_changed+"\n"
    else:
        atlantis = "All OKAY"
    return(atlantis)

def stations_near_user_input():
    #returns details of the water stations near by
    base_url = "http://environment.data.gov.uk/flood-monitoring/id/stations"
    input_lat = input('Enter Latitude: ')
    input_long = input('Enter Longitude: ')
    distance = input('How close to the latitude / longitude should be seached?: ')
    user_parameters = '?lat='+input_lat+'&long='+input_long+'&dist='+distance
    station_url = base_url+user_parameters
    get_data = requests.get(station_url)
    get_data.raise_for_status()
    analysis = get_data.json()
    items = analysis["items"]
    url_for_station = items[0]["@id"]
    RLOIid = items[0]["RLOIid"]
    date_opened = items[0]["dateOpened"]
    whats_measured = items[0]["measures"][0]["parameterName"]
    str_url_for_station = str(url_for_station)
    str_station_name = str(station_name)
    str_RLOIid = str(RLOIid)
    str_dateOpened = str(date_opened)
    str_whats_measured = str(whats_measured)
    output_msg = "\n Station Name: "+str_station_name+"\n Station URL: "+str_url_for_station+"\n Station RLOIid: "+str_RLOIid+"\n Date Station Opened: "+str_dateOpened+"\n Station Measures: "+str_whats_measured+"\n"
    return(output_msg)

def stations_near_auto():
    # Returns details of the water stations near by
    # Replace XXXXXXX  with latitude and longitude
    station_url = "http://environment.data.gov.uk/flood-monitoring/id/stations?lat=XXXXXXX&long=XXXXXXX&dist=1"
    get_data = requests.get(station_url)
    get_data.raise_for_status()
    analysis = get_data.json()
    items = analysis["items"]
    url_for_station = items[0]["@id"]
    RLOIid = items[0]["RLOIid"]
    date_opened = items[0]["dateOpened"]
    station_name = items[0]["label"]
    whats_measured = items[0]["measures"][0]["parameterName"]
    str_url_for_station = str(url_for_station)
    str_station_name = str(station_name)
    str_RLOIid = str(RLOIid)
    str_dateOpened = str(date_opened)
    str_whats_measured = str(whats_measured)
    output_msg = "\n Station Name: "+str_station_name+"\n Station URL: "+str_url_for_station+"\n Station RLOIid: "+str_RLOIid+"\n Date Station Opened: "+str_dateOpened+"\n Station Measures: "+str_whats_measured+"\n"
    return(output_msg)

def readings_from_station_auto():
    # Gives station details, current reading and historic high / low readings from station
    # Replace XXXXXXX with the station @id (see url_for_station from stations_near_auto())
    station_url = "https://environment.data.gov.uk/flood-monitoring/id/stations/XXXXXXX.json"
    get_data = requests.get(station_url)
    get_data.raise_for_status()
    analysis = get_data.json()
    analysis = get_data.json()
    items = analysis["items"]
    url_for_station = items["@id"]
    str_url_for_station = str(url_for_station)
    RLOIid = items["RLOIid"]
    str_RLOIid = str(RLOIid)
    date_opened = items["dateOpened"]
    str_date_opened = str(date_opened)
    station_name = items["label"]
    str_station_name = str(station_name)
    # current measurements
    current_measurement_date_time = items["measures"]["latestReading"]["dateTime"]
    str_current_measurement_date_time = str(current_measurement_date_time)
    current_measurement_value = items["measures"]["latestReading"]["value"]
    str_current_measurement_value = str(current_measurement_value)
    # historic measurements
    max_high = items["stageScale"]["maxOnRecord"]["value"]
    str_max_high = str(max_high)
    max_high_date = items["stageScale"]["maxOnRecord"]["dateTime"]
    str_max_high_date = str(max_high_date)
    min_low = items["stageScale"]["minOnRecord"]["value"]
    str_min_low = str(min_low)
    min_low_date = items["stageScale"]["minOnRecord"]["dateTime"]
    str_min_low_date = str(min_low_date)

    output_msg = "\n Station Name: "+str_station_name+"\n RLOIid: "+str_RLOIid+"\n Date Opened: "+str_date_opened+"\n Current Measurement: "+str_current_measurement_value+"\n Measurement Taken at: "+str_current_measurement_date_time+"\n Historic Hight: "+str_max_high+"\n Max High Date: "+str_max_high_date+"\n Min Height: "+str_min_low+"\n Minimum Height Date: "+str_min_low_date+"\n"
    return(output_msg)

print(readings_from_station_auto())