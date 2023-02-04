import StreetViewAPI as sv
import random as rng
import json

def get_RG_Coords(coords, ranges):
    x = rng.random()
    y = rng.random()

    x = (2*x-1)*ranges[0] + coords[0]
    y = (2*y-1)*ranges[1] + coords[1]

    return (x,y)


class GrabData(object):

    def __init__(self):

        api_key = "AIzaSyAcbe0rC7u6aI-asYUOysQGzveaXaYZYFM"
        self.StreetView = sv.GStreetViewer(api_key)
        self.current_data_ids = []


    def GrabImg(self, location, directory, name):
        pic_path = "{}pic_{}.jpg".format(directory, name.replace("/",""))
        meta_path = "{}Meta_Data/meta_{}.json".format(directory, name.replace("/",""))

        meta_info, img_content = self.StreetView.get_pic(location, directory, name)

        if meta_info['status'] == "OK" and not meta_info['pano_id'] in self.current_data_ids:
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

        while img_count < max_img and repeat < 15:
            lat,lon = get_RG_Coords(location, ranges)
            coords = str(lat)+","+str(lon)
            print(coords)
            bool = self.GrabImg(coords, directory, str(img_count))
            print(bool)
            if bool:
                img_count += 1
                repeat = 0
            else:
                repeat += 1

if __name__ == "__main__":

    data = GrabData()
    data.GrabMultImg([36.11486216422, -112.1501713982],[0.02, 0.02],r"/Users/tylermccue/Downloads/", 15)