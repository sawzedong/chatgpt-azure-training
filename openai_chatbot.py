from openai import OpenAI
client = OpenAI()

messages = [
    {"role": "system", "content": "You will be provided with unstructured data, and your task is to parse it into CSV format and answer relevant questions about the data."}
]

"""
SAMPLE DATA [paste as one line!]

There are many fruits that were found on the recently discovered planet Goocrux. 
There are neoskizzles that grow there, which are purple and taste like candy. 
There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. 
Pounits are a bright green color and are more savory than sweet. 
There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. 
Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.
"""

while(True):
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print("Assistant:", completion.choices[0].message.content)
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
