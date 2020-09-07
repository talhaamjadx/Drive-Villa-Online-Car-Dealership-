from ConversationCreator import chatConversation
from model import  CreateUpdateChatbot,LoadChatBot,PredictReply

customer_number="0123456789"
txt=chatConversation("Toyota","secondhand","2016","400 miles", "3000 $", "2000 $"," 1500 $")

if len(txt)%2 !=0:
    txt.append(" Thank you for viewing the car. If you have any query, please do contact ")

name= input("Enter your id:")
CreateUpdateChatbot(name,txt)
model=LoadChatBot(name)
import pickle as p
fileaddress="Dictionary/"+ name+".p"
with open(fileaddress,"rb") as f: 
    dictionary=p.load(f)
while True: 

    try:
        inp= input("User:")
          
        reply=PredictReply(model,inp,dictionary)
        print(reply)
    except: 
        print("Commmunication Error! Pleasse try again later.") 
        break