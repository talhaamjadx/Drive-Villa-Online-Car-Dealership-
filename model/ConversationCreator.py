def chatConversation(modelname,condition,boughtyear,transmission,purchaseprice,saleprice,lowestsalprice):
    l1="Hey!\n Hello sir, welcome.\n I am here to buy a car. Could you please help me with that?\n Sure, sir. We have "+modelname+" bought at year "+boughtyear+" \n Could you please brief about it?.\n Sure! It was bought in  "+boughtyear+" and has transmission of " +transmission+". Its in pretty good condition and very rare to find a car of this quality in the market.\n How much will this cost?\n Onroad price for this will be "+saleprice+"\n okay!\n Sure, sir. How about payment?\nI will make the complete payment by check.\n Sure, sir. We will get your car ready in a while.\n Ok!\n Thank You!\n Goodbye!"
    lis=l1.split('\n')   
    return lis 


