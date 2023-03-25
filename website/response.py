"""
response.py
-----------------
Answers users question in the chat
"""

import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")        # YOUR API KEY GOES HERE (replace)

# In this function, you will accept a question from the user and generate a response using GPT
def get_steps(userInput):
    # take the input and phrase it as a question to chatgpt with a prompt to break it into steps with some marker for
    # each step and return the list of steps as strings

    try:
        message = f'tell me how to {userInput} and break it down into numbered steps labelled by Step # marked by @@ at the beginning of the step. Start the beginning of the step with the action verb used in the step'
        chatgpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                temperature=0.1,
                max_tokens=2000,
                top_p=0.95)
        chatgpt_response = chatgpt_response.split('@@');
        chatgpt_response = [x for x in chatgpt_response if 'STEP' in x.upper()]
        return chatgpt_response
    except:
        return ""


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
    try:
        urls = []
        for imageprompt in imagePrompts:
            image_object = openai.Image.create(
                        prompt= imageprompt,
                        n=1,
                        size="512x512")

            image_url = image_object['data'][0]['url']
            urls.append(image_url)
        return urls
    except:
        return ""