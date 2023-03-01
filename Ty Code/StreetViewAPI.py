import requests
import json

class GStreetViewer(object):

    def __init__(self, api_key, default_size="640x640", verbose=True):

        self.api_key = api_key
        self.size = default_size
        self.verbose = verbose
        self.area = 10000

    def get_meta_data(self, location):
        meta_params = dict(key=self.api_key, location=location, radius=self.area)
        meta_response = requests.get('https://maps.googleapis.com/maps/api/streetview/metadata?', params=meta_params)

        meta_info = meta_response.json()
        status = meta_info['status']

        meta_response.close()
        return (status, meta_info)

    def get_pic(self, location):
        status, meta_info = self.get_meta_data(location)
        

        if status == "OK":
            if self.verbose:
                print("Acquiring picture")
            pic_params = dict(key=self.api_key, location=location, size=self.size, radius=self.area)
            pic_response = requests.get('https://maps.googleapis.com/maps/api/streetview?', params=pic_params)
            pic_response.close()

            return meta_info, pic_response.content

        else:

            return meta_info, None

if __name__ == "__main__":
    api_key = ""
    picGrabber = GStreetViewer(api_key)

    picGrabber.get_pic('800 21st St NW, Washington, DC 20052')

    


