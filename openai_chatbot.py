from openai import OpenAI

# this next line REQUIRES a .env file in the same folder with the key OPENAI_API_KEY
client = OpenAI()

# this messages variable is a list of all the different messaes we can provide
messages = [
    # we start with a single system message that provides context
    {"role": "system", "content": "You will be provided with unstructured data, and your task is to parse it into CSV format and answer relevant questions about the data."}
]

# loop for chatbot
while(True):
    # get users input and append into the list of messages
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})

    # get the response by chatgpt based on these messages
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # print and add the response into the list of messages
    print("Assistant:", completion.choices[0].message.content)
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})

"""
## SAMPLE OUTPUT

User:
There are many fruits that were found on the recently discovered planet Goocrux. 
There are neoskizzles that grow there, which are purple and taste like candy. 
There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. 
Pounits are a bright green color and are more savory than sweet. 
There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. 
Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.


Assistant: 
Sure! I will create a CSV file with the information provided about the fruits found on the planet Goocrux. The CSV file will have columns for the fruit name, color, taste description, and additional characteristics.

Here is the CSV data:

```
fruit_name,color,taste_description,additional_characteristics
neoskizzles,purple,taste like candy,
loheckles,grayish blue,tart like a lemon,
pounits,bright green,savory,
loopnovas,neon pink,taste like cotton candy,
glowls,pale orange,sour and bitter,acidic and caustic
```

Please let me know if you need any further information or analysis on this data.


User: 
If I made a juice of loheckles and loopnovas, what colour would it likely be?

Assistant: 
If you made a juice of loheckles (grayish blue fruit) and loopnovas (neon pink fruit), the likely color of the juice would be a combination of these two colors. Mixing grayish blue and neon pink could result in a purplish color due to the blending of the blue and pink pigments. So, the juice would likely be a shade of purple.

"""