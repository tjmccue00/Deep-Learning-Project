import os, shutil
from keras import layers, models, optimizers
import matplotlib.pyplot as plt
import random
import matplotlib.image as mpimg

model = models.load_model(r"/Users/tylermccue/Downloads/GeoGuesser/Model")

base_dir = r"/Users/tylermccue/Downloads/GeoGuesser"
test_dir = os.path.join(base_dir, 'Test')

classes = ["Yellowstone", "Grand Canyon", "Everglades"]
class_int = random.randint(0,2)

landscape = classes[class_int]

file_int = random.randint(0,149)

class_dir = os.path.join(test_dir, landscape)
file_list = os.listdir(class_dir)

file_path = os.path.join(class_dir, file_list[file_int])

img = mpimg.imread(file_path)
imgplot = plt.imshow(img)
plt.show()

