# importing modules
import extract_msg
import os
import pandas as pd
import re
import json



    
def content_extraction(directory,extension):
    for mail in os.listdir(directory):
        try:
            if mail.endswith(extension):
                msg = extract_msg.Message(mail) 
                msg.save()  
        except(UnicodeEncodeError,AttributeError,TypeError) as e:
            pass 

def DataImporter(directory, extension):
    my_list = []
    for i in os.listdir(direct):
        try:
            if i.endswith(ext):
                msg = extract_msg.Message(i)
                my_list.append([msg.filename,msg.sender,msg.to, msg.date, msg.subject, msg.body, msg.message_id]) 
                global df
                df = pd.DataFrame(my_list, columns = ['File Name','From','To','Date','Subject','MailBody Text','Message ID'])
                print(df.shape[0],' rows imported')
        except(UnicodeEncodeError,AttributeError,TypeError) as e:
            pass

def text_to_json(filename):
    # dictionary where the lines from
    # text will be stored
    dict1 = {}
    
    # creating dictionary
    with open(filename) as fh:
    
        for line in fh:
    
            if re.search('^([^,]+):',line):
                c=[line.split(":")]
                nam=c[0]
                
                dict1[nam[0]]=nam[1]
                print(dict1)
    # creating json file
    # the JSON file is named as test1
    out_file = open("testing.json", "w")
    json.dump(dict1, out_file, indent = 4, sort_keys = False)
    out_file.close()


# location and file extension
direct = os.getcwd()
ext = '.msg' 
# content_extraction(direct,ext)
# DataImporter(direct,ext)

filename= "2021-12-27_2201 RE BL HLCL Sh#66100459 Doc#HLCUBSC2112BIPH0/message.txt"
# text_to_json(filename)

