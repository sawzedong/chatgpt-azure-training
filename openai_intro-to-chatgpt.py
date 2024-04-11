# this is just the beginnings of the code, feel free to tweak the parameters!

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo", # but dont change this!
  messages=[
    {"role": "user", "content": "..."}
  ],
  temperature = 0.2
)

print(completion.choices[0].message)
