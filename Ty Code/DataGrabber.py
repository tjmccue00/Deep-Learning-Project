import StreetViewAPI as sv
import random as rng
import json
import os

def get_RG_Coords(coords, ranges):
    x = rng.random()
    y = rng.random()

    x = (2*x-1)*ranges[0] + coords[0]
    y = (2*y-1)*ranges[1] + coords[1]

    return (x,y)


class GrabData(object):

    def __init__(self):

        api_key = "AIzaSyC6QQyvk9Ur_tMQPQ_CvnYzc5n73mydpto"
        self.StreetView = sv.GStreetViewer(api_key)
        self.current_data_ids = []


    def GrabImg(self, location, directory):

        meta_info, img_content = self.StreetView.get_pic(location)

        if meta_info['status'] == "OK" and not meta_info['pano_id'] in self.current_data_ids:
            pic_path = "{}pic_{}.jpg".format(directory, meta_info['pano_id'].replace("/",""))
            meta_path = "{}Meta_Data/meta_{}.json".format(directory, meta_info['pano_id'].replace("/",""))

            with open(pic_path, 'wb') as file:
                    file.write(img_content)
            with open(meta_path, 'w') as file:
                    json.dump(meta_info, file)
            self.current_data_ids.append(meta_info['pano_id'])
            return True
        else:
            return False

    def GrabMultImg(self, location, ranges, directory, max_img):
        img_count = 0
        repeat = 0

        while len(self.current_data_ids) <= max_img and repeat < 15:
            lat,lon = get_RG_Coords(location, ranges)
            coords = str(lat)+","+str(lon)
            bool = self.GrabImg(coords, directory)
            if bool:
                repeat = 0
            else:
                repeat += 1

            print("Current Image Count: "+ str(len(self.current_data_ids)))
            print("Current Repeat Count: "+ str(repeat)+"\n")

    def getMetaData(self, dir):
        files = os.listdir(dir+"Meta_Data")

        for file in files:
            if ".json" in file:
                with open(dir+"Meta_Data/"+file) as f:
                    meta = json.load(f)
                self.current_data_ids.append(meta['pano_id'])



if __name__ == "__main__":

    data = GrabData()
    # data.getMetaData(r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser/Raw/Hawaii Volcanoes/")
    # data.GrabMultImg([19.380166, -154.974198],[0.175, 0.175],r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser/Raw/Hawaii Volcanoes/", 1000)
    data.getMetaData(r"/Users/Damond/Desktop/WINTER 2023/CSC487/Deep-Learning-Project/train/yosemite/")
    data.GrabMultImg([37.965952, -119.540852], [0.375, 0.375],
                     r"/Users/Damond/Desktop/WINTER 2023/CSC487/Deep-Learning-Project/train/yosemite/", 1000)