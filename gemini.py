#generate array of wp post

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

#GEMINI API
API_KEY=#[Insert you gemini API KEY]
genai.configure(api_key=API_KEY)

#Prompt
open="Create a seo optimized blog post with 600 words focusing on copywriting, mindset and psychology keywords to answer this question: "

#wordpress category id
cat_id=6

#Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
title_array = data.importer()
size=len(title_array)
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

#wp API
def push_to_wp(title, content) :   
    
    username = #[wordpress API username]
    pass_word = #[wordpress API password]
    credentials = username + ':' + pass_word
    token = base64.b64encode(credentials.encode())
    wpBaseUrl=#[Your baseURL]

    #modify to your url schema
    WP_url = wpBaseUrl + "/wp-json/wp/v2/posts"

    #debug
    print (WP_url)

    #API Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : 'Basic ' + token.decode('utf-8'),
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) \
            AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
        }


    #API Payload
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

#running number - excel row
start=0
end=10
run=1

if size < end :
    end=size

while (run < size):
    for execute in range (start,end) :
        print (execute)
        prompt = open + title_array[execute]
        print (f"Prompt: {prompt}")
        run=run+1
        #response.append(prompt)
        content=prompter(prompt)     
        push_to_wp(title_array[execute],content)
        #print (f"Response \nTITLE: {title_array[execute]}")
        #print (f"\nCONTENT: {content}")
    sleep(60)
    start=end
    print (f"start: {start}")

    #
    end = start + 10
    if (end>size):
        end=size
    print (f"end: {end}")

#data.exporter(response)
    




#print("response",response.text)
