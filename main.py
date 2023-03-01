import openai


DEBUG = False

def log(s):
  if DEBUG:
    print(s)
  
def getkey():
  with open(".keys", "r") as f:
    key = f.read()
    return key

def setup():
  openai.api_key = getkey()

def askOpenAi(prompt="hello word"):
  response = openai.Completion.create(
      model="text-davinci-001", 
      prompt=prompt,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty= 0,
      presence_penalty=0,
      stop= ["input:"])
  log(response)
  return response['choices'][0]['text']

if __name__ == "__main__":
  print("setup...\npress ctrl+c to exit\n")
  setup()
  while True:
    try:
      question = input("Ask me anything...\nQuestion: ")
      print("Answer: %s" % askOpenAi(question))
      print("-------------------")
    except KeyboardInterrupt:
      print("exist...")
      raise SystemExit