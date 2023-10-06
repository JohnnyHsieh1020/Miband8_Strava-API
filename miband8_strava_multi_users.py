import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import datetime

# 小米 ID
user_dict = {
    "USER1_MI_ID": "USERNAME1",
    "USER2_MI_ID": "USERNAME2"
}

# URLs
auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"


# Get Access token
auth_params = {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "refresh_token": "YOUR_CLIENT_REFRESH_TOKEN",
    "f": "json",
    "grant_type": "refresh_token"
}

# POST request
auth_res = requests.post(auth_url, data=auth_params, verify=False)
access_token = auth_res.json()["access_token"]
print(f"Access Token :{access_token}\n")
#-------------------------------------------------------------------

# Get activities
header = {"Authorization": "Bearer " + access_token}
param = {"per_page": 200, "page": 1}

# GET request
all_records = requests.get(activites_url, headers=header, params=param).json()
# print(all_records)
#-------------------------------------------------------------------


for record in all_records:
    activity_type = ""
    start_date = ""
    distance = 0.0
    avg_heart_rate = 0.0
    max_heart_rate = 0.0

    # Get 小米 ID
    mi_user_id = record["external_id"].split("_")[0]
    user_name = user_dict[mi_user_id]
    
    # Get activity type
    activity_type = record["type"]
    
    # Get local start date
    start_date = record["start_date_local"][:-1]
    start_date = start_date.replace("T", " ")
    
    # Get during time(need to convert)
    during_time_sec = record["elapsed_time"]
    during_time = str(datetime.timedelta(seconds = during_time_sec))

    # Get distance
    distance_m = record["distance"]

    # Get heart rate
    avg_heart_rate = record.get("average_heartrate", avg_heart_rate)
    max_heart_rate = record.get("max_heartrate",max_heart_rate)

    # Print out data
    print(f"User Name: {user_name}")
    print(f"User ID: {mi_user_id}")
    print(f"Type: {activity_type}")
    print(f"Date: {start_date}")
    print(f"Time: {during_time}")
    print(f"Distance: {distance_m}m")
    print(f"Average Heart Rate: {avg_heart_rate}bpm")
    print(f"Maximum Heart Rate: {max_heart_rate}bpm")
    print("*" * 20)
