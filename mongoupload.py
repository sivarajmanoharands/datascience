# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:54:54 2023

@author: user
C:\\Users\\user\\Downloads\\NIFTY.csv'
"""


import csv
from datetime import datetime 
import pandas as pd 
import pymongo
import tkinter as tk
from tkinter import filedialog
  
def loadCsv(csvfile):
    data = pd.read_csv(csvfile)
    data['Date '].apply(lambda x: datetime.strptime(x, '%d-%b-%y'))
    return data

#print(loadCsv('C:\\Users\\user\\Downloads\\NIFTY.csv'))


def docinsert(csvfile):
    # Create a connection to the MongoDB database
    client = pymongo.MongoClient("mongodb://localhost:27017")
    
    # Create a database and collection
    db = client["TradeTicks"]
    collection = db["NSEDATA"]
    
    # Read the CSV file into a Pandas DataFrame
    df = loadCsv('C:\\Users\\user\\Downloads\\NIFTY.csv')
    
    # Insert the DataFrame into MongoDB
    collection.insert_many(df.to_dict("records"))
    cursor = collection.aggregate([{"$count": "c"}])
    count = list(cursor)[0]["c"]

    print(count)
    # Close the connection to MongoDB
    client.close()
    #docretrieve()

def docretrieve():
    
    # Connect to the MongoDB database
    client = pymongo.MongoClient("mongodb://localhost:27017")
    
    # Use the find() method to retrieve the data from the database
    database = client.TradeTicks
    collection = database.NSEDATA
    
    df = pd.DataFrame(list(collection.find()))
    
    # Display the DataFrame in a tabular format
    print(df.to_string())    
        

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)
        # You can use the file_path here, for example, to open/read the file
        #docinsert('C:\\Users\\user\\Downloads\\NIFTY.csv')
        docinsert(file_path)

open_file_dialog()