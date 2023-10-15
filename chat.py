#Simple example
# Get familar with the API (openai.ChatCompletion.create())
import openai
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, 
        {"role": "user", "content": "How many colors in the rainbow?"},
        {"role": "assistant", "content": "There are seven colors in the rainbow."},
        {"role": "user", "content": "What is the 3rd color?"},
    ],
    temperature=0,
)

print(response.choices[0]["message"]["content"])



# response = openai.ChatCompletion.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."}, 
#         {"role": "user", "content": "How many colors in the rainbow?"},
#     ],
#     temperature=0,
# )

# print(response.choices[0]["message"]["content"])


# response = openai.ChatCompletion.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."}, 
#         {"role": "user", "content": "What is the 3rd color?"},
#     ],
#     temperature=0,
# )
