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
from datetime import date

today=date.today()
print (today)

day_count=today.timetuple().tm_yday
print (f"day_count= {day_count}")

API_KEY='AIzaSyALWdiUdBh0BFnrYTTNkc131ApjkDST8hY'
genai.configure(api_key=API_KEY)
opening="Create a seo optimized blog post with 600 words focusing on copywriting, mindset and psychology keywords to answer this question: "
cat_id=6

model = genai.GenerativeModel("gemini-1.5-flash")
title_array = data.importer()
size=len(title_array)

#f=open("rowcount.txt","r")
counter=day_count
print (f"Row= {counter}")
#f.close()


#f=open("rowcount.txt","w")
#if (counter-1==size):
 #   updater=2
#else:
    #updater=counter+1
#f.write(str(updater))
#f.close()




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
    
    username = "zalikamari@gmail.com"
    pass_word = "r64y yXUy vqHR xr9f rTwl ehk3"
    credentials = username + ':' + pass_word
    token = base64.b64encode(credentials.encode())
    wpBaseUrl="https://copymindset.com"
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


run=counter-2
print (f"Index = {run}")
prompt = opening + title_array[run]
print (f"Prompt: {prompt}")
        #run=run+1
#response.append(prompt)
content=prompter(prompt)     
push_to_wp(title_array[run],content)
print (f"Response \nTITLE: {title_array[run]}")
#print (f"\nCONTENT: {content}")
    #sleep(60)
    #start=end
   # print (f"start: {start}")
  #  end = start + 10
  #  if (end>size):
    #    end=size
  #  print (f"end: {end}")

#data.exporter(response)
    




#print("response",response.text)