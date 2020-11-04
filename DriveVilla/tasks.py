from celery import shared_task
# from demoapp.models import Widget
from model.model import CreateUpdateChatbot, LoadChatBot, PredictReply
from model.ConversationCreator import chatConversation
import pickle as p

@shared_task(name='get_message_response')
def getResponse(message, username):
    customer_number="0123456789"
    txt=chatConversation("Toyota","secondhand","2016","400 miles", "3000 $", "2000 $"," 1500 $")
    if len(txt)%2 !=0:
        txt.append(" Thank you for viewing the car. If you have any query, please do contact ")
    name = username
    # CreateUpdateChatbot(name,txt)
    model=LoadChatBot(name)
    fileaddress="model/Dictionary/"+ name+".p"
    with open(fileaddress,"rb") as f: 
        dictionary=p.load(f)
    try:
        inp = message

        reply=PredictReply(model,inp,dictionary)
        response = str(reply)
        return response
    except KeyError:
        print("Commmunication Error! Pleasse try again later.") 
        return "whatchu talkin bout man?"

@shared_task(name='create_new_model')
def createUser(message, username):
    customer_number="0123456789"
    txt=chatConversation("Toyota","secondhand","2016","400 miles", "3000 $", "2000 $"," 1500 $")
    if len(txt)%2 !=0:
        txt.append(" Thank you for viewing the car. If you have any query, please do contact ")
    name = username
    CreateUpdateChatbot(name,txt)
