#generate and push wp post daily using row number generated from current number of day in year

import json
from time import sleep
import requests
import google.generativeai as genai
import os
from requests.auth import HTTPBasicAuth
#from google.colab import userdata
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import base64
import importer as data
from datetime import timedelta
from datetime import datetime
from datetime import date
import pytz

#get datetime today for row processing
today = datetime.now(pytz.timezone('Australia/Sydney'))
print (today)

day_count=today.timetuple().tm_yday
print (f"day_count= {day_count}")


API_KEY='#Gemini AI API Key'
genai.configure(api_key=API_KEY)

#Opening prompt
opening="Create a seo optimized blog post with 600 words focusing on copywriting, mindset and psychology keywords to answer this question: "

#Wordpress category Id
cat_id=6

#GEMINI model
model = genai.GenerativeModel("gemini-1.5-flash")

#get title from excel
title_array = data.importer()

#determine current size
size=len(title_array)

#get row number = day_count
counter=day_count
print (f"Row= {counter}")

print(f"size: {size} ")

def prompter(prompt):
    response = model.generate_content(prompt,
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                })

    content = response.text
    content=content.replace("*","")
    return content

def push_to_wp(title, content) :   
    
    username = 'wordpress API Username'
    pass_word = "wordpress API Password"
    credentials = username + ':' + pass_word
    token = base64.b64encode(credentials.encode())
    
    wpBaseUrl="yourbaseurl.com"
    WP_url = wpBaseUrl + "/wp-json/wp/v2/posts"
    print (WP_url)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : 'Basic ' + token.decode('utf-8'),
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) \
            AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
        }



    payload = json.dumps({ 
           "status":"publish",
           "title": title,
           "content": content,
           "categories" : cat_id
           })

    response = requests.request(
       "POST",
      WP_url,
     headers=headers,
        data=payload
     )

#generate row number
run=counter-2
print (f"Index = {run}")

#generate final prompt
prompt = opening + title_array[run]
print (f"Prompt: {prompt}")

#call prompter method
content=prompter(prompt)     

#call push_to_wp method
push_to_wp(title_array[run],content)

print (f"Response \nTITLE: {title_array[run]}")
  




