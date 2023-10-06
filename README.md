# Miband8_Strava-API

- Collect activity data from Mi band 8
- This project is based on [franchyze923/Strava_Api](https://github.com/franchyze923/Code_From_Tutorials/tree/master/Strava_Api)🙏

## Resources Used

- Python Version: 3.10.13
- IDE: VSCode
- Requirements:
  - Install [requirements](https://github.com/JohnnyHsieh1020/Miband8_Strava-API/blob/main/requirements.txt)
  ```terminal
  pip install -r requirements.txt
  ```

## File Introduction

- miband8_strava_single_user.py: For one mi band user connect to one Strava account.
- miband8_strava_multi_users.py: For multiple mi band users connect to one Strava account.
- requirements.txt: The package you need.

## Get Mi Band 8 Data by Strava API

1. Create a Strava account [here](https://www.strava.com/register).
2. Create an API application [here](https://www.strava.com/settings/api).
   - Website: https://www.strava.testapp.com
   - Authorization Callback Domain: localhost
3. Authorize Credentials in the Browser.
   - Get Client ID from https://www.strava.com/settings/api
   - Paste the URL in your browser: https://www.strava.com/oauth/authorize?client_id={YOUR_CLIENT_ID}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all
   - Copy the authorization code from the URL: http://localhost/exchange_token?state=&code={Copy}&scope=read,activity:read_all
4. Get Access and Refresh Tokens.(Two ways)

   - Postman
     ```
     Method: POST
     URL: https://www.strava.com/oauth/token
     Params:
     client_id=YOURCLIENTID
     client_secret=YOURCLIENTSECRET
     code=AUTHORIZATIONCODE
     grant_type=authorization_code
     ```
   - Terminal/Command Line(CMD):
     ```
     curl -X POST https://www.strava.com/oauth/token \
     -F client_id=YOURCLIENTID \
     -F client_secret=YOURCLIENTSECRET \
     -F code=AUTHORIZATIONCODE\
     -F grant_type=authorization_code
     ```

5. Make sure your Mi Fitness is connected with your Strava account.
6. Paste `client_id`, `client_secret`, `refresh_token` on the code.
7. Run code!

