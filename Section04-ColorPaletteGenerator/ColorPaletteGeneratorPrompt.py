import openai
import json
from dotenv import dotenv_values
from IPython.display import Markdown, display

def display_colors(colors):
    display(Markdown(" ".join(f"<span style='color: {color}'>{chr(9608) * 4}</span>" for color in colors)))  

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

instructions = """
You are a color palette generating assistant that responds to text prompts for color palettes.
You should generate color palettes that fit the theme, mood or instructions in the prompt.
The color palettes should contain between 2 and colors.

Here are 2 Q & A examples:
Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]


Desired format: JSON array of hexadecimal color codes

Text: A beautiful sunset.

Result:
"""
openAiResponse = openai.Completion.create(
    model="text-davinci-003",
    prompt=instructions,
    max_tokens=200
)
colors = json.loads(openAiResponse["choices"][0]["text"])
print(colors)
display_colors(colors)