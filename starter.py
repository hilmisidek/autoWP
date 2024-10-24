import openai
import requests
import json
from requests.auth import HTTPBasicAuth
import base64



API_KEY = "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"
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


# Set up the OpenAI API client
#openai.api_key = API_KEY
# Set up the model and prompt
#model_engine = "text-davinci-003"
#language="Malay"

title=str(input("Insert title: ")).strip()
#prompt = f"Create a seo-friendly blog post with 1000 words with title: {title} \
#in {language} language"

# Generate a response
#completion = openai.Completion.create(
 #   engine=model_engine,
  # prompt=prompt,
   #max_tokens=2048,
    #n=1,
    #stop=None,
    #temperature=1.0,
#)

#response = completion.choices[0].text

response = """Understanding the Basics of Copywriting
Copywriting is more than just putting words on a page; it’s about crafting messages that drive action. Whether you’re writing a product description, a blog post, or a social media update, your goal is to engage your audience and compel them to act.

Why Copywriting Matters
Copywriting is crucial in digital marketing. It's the bridge between your brand and your audience. Great copy can transform a casual browser into a loyal customer. It’s not just about selling products but also about building relationships.

SEO Best Practices for Copywriting
Integrating SEO into your copywriting ensures that your content is discoverable. Here are some best practices:

Keyword Placement: Naturally incorporate your primary keyword into the title, first paragraph, and throughout the content. Avoid keyword stuffing.

Quality Content: Google favors content that provides value. Focus on answering your audience's questions and solving their problems.

Readability: Break up text with subheadings, bullet points, and short paragraphs. Use simple language and a conversational tone.

Meta Descriptions: Write compelling meta descriptions that include your primary keyword. These should entice readers to click on your link.

Internal Linking: Link to other relevant pages on your website to keep readers engaged and improve your site’s SEO.

Crafting Compelling Copy
Your copy should not only be SEO-friendly but also resonate with your audience. Here are some tips:

Understand Your Audience: Know who you’re writing for. What are their pain points? What solutions are they seeking?

Clear and Concise: Avoid jargon. Write in a way that’s easy to understand. Get to the point quickly.

Emotional Appeal: Use storytelling to connect with your audience on an emotional level. People remember stories more than facts.

Strong CTAs: Your call-to-action should be clear and compelling. Guide your readers on what to do next.

Conclusion
Mastering copywriting takes time and practice, but with these tips, you’ll be well on your way to creating copy that converts. Always remember to keep your audience in mind and provide value in every piece of content you create.

Ready to elevate your copywriting skills? Start implementing these strategies today and watch your engagement soar!"""

#print(response)

payload = json.dumps({ 
        "status":"publish",
        "title": title,
        "content": response,
        "categories" : 2
        })

response = requests.request(
    "POST",
    WP_url,
    headers=headers,
    data=payload
    )

print("response",response.text)