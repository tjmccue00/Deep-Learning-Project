import os, shutil
from keras import layers, models, optimizers
import matplotlib.pyplot as plt
import random
import matplotlib.image as mpimg
import tensorflow as tf
import numpy as np

model = models.load_model(r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser/Model")

base_dir = r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser"
test_dir = os.path.join(base_dir, 'Test')

classes = ["Everglades", "Grand Canyon", "Yellowstone"]
class_int = random.randint(0,2)

landscape = classes[class_int]

file_int = random.randint(0,149)

class_dir = os.path.join(test_dir, landscape)
file_list = os.listdir(class_dir)

file_path = os.path.join(class_dir, file_list[file_int])

img = mpimg.imread(file_path)
imgplot = plt.imshow(img)
plt.show()
img = [img]
img = tf.convert_to_tensor(img)
img = tf.image.resize(img, [200,200], antialias=True)/255.0

preds = model.predict(img, verbose=0)
print(classes[np.argmax(preds)])
if classes[np.argmax(preds)] == classes[class_int]:
    print("Model is correct!")
else:
    print("Model is incorrect, correct answer is, ", classes[class_int])




