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

def askOpenAi(prompt="hello word", type="text"):
  if type == "image":
    response = openai.Image.create(prompt=prompt, n=4, size="512x512")
    log(response)
    return response["data"]
  elif type == "text":
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
  else:
    raise Exception("type not supported")

if __name__ == "__main__":
  print("setup...\npress ctrl+c to exit\n")
  setup()
  while True:
    try:
      print("Ask me anything...")

      ask_type = input("Type: (text or image) ")
      assert ask_type in ["text", "image"]

      question = input("Question: ")

      print("Answer:\n %s" % askOpenAi(question, ask_type))
      print("-------------------")
    except KeyboardInterrupt:
      print("exist...")
      raise SystemExit