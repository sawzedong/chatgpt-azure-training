from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Brainstorm 2 simple ideas combining VR and studying."}
  ],
  temperature = 0.0
)

# the completion itself gives a ChatCompletion object, with a lot of information
print(completion, "\n\n---------------------------------\n")

# this message is in the form of a ChatCompletionMessage with content, role, and others
print(completion.choices[0].message, "\n\n---------------------------------\n")

# this extracts only the text content of the message
print(completion.choices[0].message.content)

"""
## SAMPLE OUTPUT

ChatCompletion(id='chatcmpl-9DDFYDrFfpwZJB91wvpJZmC4MHgNw', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Virtual Reality Study Groups: Students can join virtual study groups in a VR environment where they can collaborate on assignments, discuss course material, and quiz each other. This can provide a more immersive and engaging study experience compared to traditional online study groups.\n\n2. Virtual Reality Flashcards: Students can create and study flashcards in a VR environment, where they can interact with the cards in a more dynamic and interactive way. This can help improve memory retention and make studying more enjoyable. Additionally, students can customize their flashcards with images, audio, and interactive elements to enhance their learning experience.', role='assistant', function_call=None, tool_calls=None))], created=1712936224, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=118, prompt_tokens=18, total_tokens=136)) 

---------------------------------

ChatCompletionMessage(content='1. Virtual Reality Study Groups: Students can join virtual study groups in a VR environment where they can collaborate on assignments, discuss course material, and quiz each other. This can provide a more immersive and engaging study experience compared to traditional online study groups.\n\n2. Virtual Reality Flashcards: Students can create and study flashcards in a VR environment, where they can interact with the cards in a more dynamic and interactive way. This can help improve memory retention and make studying more enjoyable. Additionally, students can customize their flashcards with images, audio, and interactive elements to enhance their learning experience.', role='assistant', function_call=None, tool_calls=None) 

---------------------------------

1. Virtual Reality Study Groups: Students can join virtual study groups in a VR environment where they can collaborate on assignments, discuss course material, and quiz each other. This can provide a more immersive and engaging study experience compared to traditional online study groups.

2. Virtual Reality Flashcards: Students can create and study flashcards in a VR environment, where they can interact with the cards in a more dynamic and interactive way. This can help improve memory retention and make studying more enjoyable. Additionally, students can customize their flashcards with images, audio, and interactive elements to enhance their learning experience.
"""