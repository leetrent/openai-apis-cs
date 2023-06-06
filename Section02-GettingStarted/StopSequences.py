import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]
createResult = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate a list of the best movies of all time:",
    max_tokens=200,
    stop="5."
)
print(createResult["choices"][0]["text"])