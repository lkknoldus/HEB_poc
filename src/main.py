import extract_msg
import os
import pandas as pd

direct = os.getcwd()    # directory object to be passed to the function for accessing emails, this is where you will store all .msg files
ext = '.msg'            # type of files in the folder to be read


# 2). Create separate folder by email name and extract data

def content_extraction(directory, extension):
    for mail in os.listdir(directory):
        try:
            if mail.endswith(extension):
                msg = extract_msg.Message(mail)  # This will create a local 'msg' object for each email in direcory
                msg.save()  # This will create a separate folder for each email inside the parent folder and save a text file with email body content, also it will download all attachments inside this folder.
        except(UnicodeEncodeError, AttributeError, TypeError) as e:
            pass  # Using this as some emails are not processed due to different formats like, emails sent by mobile.


content_extraction(direct, ext)


# 3).Import the data to Python DataFrame using the extract_msg module
# note this will not import data from the sub-folders inside the parent directory
# rather it will extract the information from .msg files, you can use a loop instead
# to directly import data from the files saved on sub-folders.

def DataImporter(directory, extension):
    my_list = []
    for i in os.listdir(direct):
        try:
            if i.endswith(ext):
                msg = extract_msg.Message(i)
                my_list.append([msg.filename, msg.sender, msg.to, msg.date, msg.subject, msg.body,
                                msg.message_id])  # These are in-built features of '**extract_msg.Message**' class
                global df
                df = pd.DataFrame(my_list,
                                  columns=['File Name', 'From', 'To', 'Date', 'Subject', 'MailBody Text', 'Message ID'])
                print(df.shape[0], ' rows imported')
        except(UnicodeEncodeError, AttributeError, TypeError) as e:
            pass


DataImporter(direct, ext)

