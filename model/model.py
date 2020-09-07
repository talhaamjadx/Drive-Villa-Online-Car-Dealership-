from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.preprocessing.text import  Tokenizer
from tensorflow.keras.models import   Sequential, load_model
import numpy as np
# default data

bot_replies=[]
seller_queries=[]
max_sentence_len=200 #default
vocablen=1
def data_Preparer(data):
       
#separate data
        max_sentence_len=len(max(data,key=len))# store maximum length of string
        for i,d in enumerate(data):#sseparate bots answer and seller queries
                 if  i%2 !=0: 
                        bot_replies.append(d)
                 else:
                        seller_queries.append(d)   
                 vocablen=len(bot_replies)
        return seller_queries,bot_replies,vocablen
#2.1 Convert separated lines into embedded matrix

t=Tokenizer(num_words=max_sentence_len, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\n', char_level=False, oov_token=True)

def Matrix_Maker(unprocessed_lines):
        word_index=t.word_index
        index_to_word=t.index_word
        t.fit_on_texts(unprocessed_lines)
        matrix=t.texts_to_matrix(unprocessed_lines,mode='binary')
        return matrix,index_to_word 

def Seq2Seq(vocablen,max_sentence_len):
    #Define Sequential Model
    model = Sequential() 
    #Create input layer
    model.add(Dense(max_sentence_len, input_shape=(max_sentence_len,)))
    model.add(Dense(max_sentence_len))
    model.add(Dense(max_sentence_len))
    #Create hidden layer 
    model.add(Activation('relu')) 
    #Create Output layer
    model.add(Activation('sigmoid')) 
    #model.compile(optimizer='rmsprop',loss='mse')
    model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='rmsprop')
    return model
def Trainer(model,inp,output):
    model.fit(inp,output, epochs=1000, batch_size=32)
    return model


def PredictReply(model,inp,index_to_word):
        enc_inp,_=Matrix_Maker(inp)
        prediction=model.predict(enc_inp)
        response=np.argmax(prediction,axis=1)
        vocablen=len(index_to_word)
        word= [index_to_word[a%vocablen] for a in response]
        sentence=word[1]
        return sentence 



#load the model
def LoadChatBot(strname):  
    strmodelname="model/Model/"+strname +".hdf5"           
    loaded_model=load_model(strmodelname)
    return loaded_model
import pickle as p
#create or update chatbot model
def CreateUpdateChatbot(modelname,modelchat):
      #  address="Conversation/"+modelname+".txt"
        seller_queries,bot_replies,vocablen=data_Preparer(modelchat)
        model=Seq2Seq(vocablen,max_sentence_len)
        inp,_=Matrix_Maker(bot_replies)
        output,index_to_word=Matrix_Maker(seller_queries)
        file="model/Dictionary/"+modelname+".p"
        with open(file,"wb") as f:
                p.dump(index_to_word,f)
        model=Trainer(model,inp,output)  
        strmodelname="model/Model/"+modelname +".hdf5"
        model.save(strmodelname)
        return 0


#Hey
# Model_maker()   

    
