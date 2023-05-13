import openai
import json

# Get your free API key
# https://platform.openai.com/account/api-keys

# Set up your OpenAI API credentials
f = open('settings.json')
openai.api_key = json.load(f)['openai']['api_key']
# openai.api_key = 'YOUR_API_KEY'

# Define a function to ask questions to the ChatGPT model
def ask_chatgpt(question, engine='text-davinci-003', max_tokens=50):
    response = openai.Completion.create(
        engine=engine,
        prompt=question,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    answer = response.choices[0].text.strip()
    return answer

# Ask a question to the ChatGPT model
question = "what is the industry classification for point predictive including subcategory in one sentence?"
answer = ask_chatgpt(question)

# Print the answer
print("Q:", question)
print("A:", answer)