"""
response.py
-----------------
Answers users question in the chat
"""

import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")        # YOUR API KEY GOES HERE (replace)

# In this function, you will accept a question from the user and generate a response using GPT
def generate_dalle(instructionsList):
    '''Generates a list of images'''
    try:
        output_list = []
        for s in instructionsList:
            text_prompt = """Make a good dall-e prompt for the following:""" +s
            chatgpt_response = openai.ChatCompletion.create(
                mode = "gpt-3.5-turbo",
                messages = [{"role": "user", "content": text_prompt}],
                temperature = 0.1,
                max_tokens = 2000,
                top_p=0.95)
            response = chatgpt_response['choices'][0]['content'].strip()
            output_list.append(response)
            return output_list
    except: 
        return ""
     
def get_images(imagePrompts):
    '''
    Takes in a list of image prompt strings and creates an array of Dall-E Generated image URLS
    '''
    urls = []
    for imageprompt in imagePrompts:
        image_object = openai.Image.create(
                    prompt= imageprompt,
                    n=1,
                    size="512x512")

        image_url = image_object['data'][0]['url']
        urls.append(image_url)
# In this function, you will generate an image based on the user prompt
def generate_image(prompt):
    try:
        # TODO: generate one image which relates to prompt, and return the url of the image as a string
        return ""
    except:
        # DO NOT DELETE!
        return ""