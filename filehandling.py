import json

with open('output.json', 'r', encoding='utf8', errors='ignore') as json_file:  
    data = json.load(json_file)
    for tweet in data:
     
        print("Created at:", tweet['created_at'])
        print("Tweet:", tweet['text'])
        print(tweet['user']['name'])
        print()



with open("hello.txt","r") as f:
 content = f.read()
 if "ginger" in content  
  print ("true")

with open("hello.txt","a") as f:
 f.write("tameside! \n ahhahahahah")
