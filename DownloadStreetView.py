#!/usr/bin/env python
# coding: utf-8

# In[119]:


## Import modules

from google_streetview import helpers
import os

## Module to encode our own URL's
try:
  from urllib.parse import urlencode
except ImportError:
  from urllib import urlencode


# In[120]:


## New Google Street View Class
class GoogleStreetView:
    def __init__(self, api_file, site_api='https://maps.googleapis.com/maps/api/streetview'):
        # api_file: string of the text file containing the API key
        
        ## Read text file to get API
        try:
            with open(api_file, "r") as file:
                self.api = file.read()
        except:
            raise Exception("API file does not exist")
        
        ## Establish google api
        self.site_api = site_api
        self.params = [{
                'size': '640x640', # max 640x640 pixels
                'location': '0,0',
                'radius' : '5000',
                'heading': '0',
                'pitch': '0',
                'key' : self.api
        }]
        
        ## Establish download path
        self.directory = os.getcwdb().decode()
        self.download_path = os.path.join(self.directory, '')
        print("DL Path: ", self.download_path)
        
    def encode_url(self):
        ## Encodes the parameters into url form
        self.links = [self.site_api + '?' + urlencode(p) for p in self.params]
        
    def update_location(self, new_location):
        ## new_location: string with latitude and longitude. Ex: '35.120153,-120.662541'
        self.params[0]['location'] = new_location
        
    def update_download_path(self, folder_name):
        ## Update download path
        self.download_path = os.path.join(self.directory, folder_name + '\\')
        
        ## If download path does not exist, create new folder
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
            
        print ("Updated Download Path", self.download_path)
                
    def download_image(self, name):
        self.encode_url()
        file_path = os.path.join(self.download_path, name + '.jpg')
        print("File Path With Name: ", file_path)
        print("Encoded URL: ", self.links[0])
        helpers.download(self.links[0], file_path)


# In[121]:


if __name__ == "__main__":
    ## Google Street View Object with API argument
    GSV = GoogleStreetView("API.txt")
        ## 3 methods to establish location, specify download path, and download image
    GSV.update_location('35.12,-120.64')
    GSV.update_download_path('California')
    GSV.download_image("pingpong")

