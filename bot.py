import openai

openai.api_key = "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"

def get_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

while True:
  prompt = input("You: ")
  response = get_response(prompt)
  print("Assistant: ", response)