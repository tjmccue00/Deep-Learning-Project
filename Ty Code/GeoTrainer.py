import os, shutil
from keras import layers, models, optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


make_dir = False
original_dataset_dir = r"C:\Users\Tyler\Documents\GitHub\Deep-Learning-Project\GeoGuesser\Raw"
base_dir = r"C:\Users\Tyler\Documents\GitHub\Deep-Learning-Project\GeoGuesser"

train_dir = os.path.join(base_dir, 'Training')
validation_dir = os.path.join(base_dir, 'Validation')
test_dir = os.path.join(base_dir, 'Test')

train_yellow_dir = os.path.join(train_dir, 'Yellowstone')
train_grand_dir = os.path.join(train_dir, 'Grand Canyon')
train_glades_dir = os.path.join(train_dir, 'Everglades')

validation_yellow_dir = os.path.join(validation_dir, 'Yellowstone')
validation_grand_dir = os.path.join(validation_dir, 'Grand Canyon')
validation_glades_dir = os.path.join(validation_dir, 'Everglades')

test_yellow_dir = os.path.join(test_dir, 'Yellowstone')
test_grand_dir = os.path.join(test_dir, 'Grand Canyon')
test_glades_dir = os.path.join(test_dir, 'Everglades')


if make_dir:
    os.mkdir(train_dir)
    os.mkdir(validation_dir)
    os.mkdir(test_dir)

    os.mkdir(train_yellow_dir)
    os.mkdir(train_grand_dir)
    os.mkdir(train_glades_dir)

    os.mkdir(validation_yellow_dir)
    os.mkdir(validation_grand_dir)
    os.mkdir(validation_glades_dir)

    os.mkdir(test_yellow_dir)
    os.mkdir(test_grand_dir)
    os.mkdir(test_glades_dir)

    places = ["Yellowstone", "Grand Canyon", "Everglades"]
    for place in places:
        curr_dir = os.path.join(original_dataset_dir, place)
        curr_base_train = os.path.join(train_dir, place)
        files = os.listdir(curr_dir)
        for i in range(700):
            src = os.path.join(curr_dir, files[i])
            dst = os.path.join(curr_base_train, files[i])
            shutil.copyfile(src, dst)
        curr_base_vali = os.path.join(validation_dir, place)
        for i in range(700, 850):
            src = os.path.join(curr_dir, files[i])
            dst = os.path.join(curr_base_vali, files[i])
            shutil.copyfile(src, dst)
        curr_base_test = os.path.join(test_dir, place)
        for i in range(850, 1000):
            src = os.path.join(curr_dir, files[i])
            dst = os.path.join(curr_base_test, files[i])
            shutil.copyfile(src, dst)


print('Total Images for Grand Canyon Training: ', len(os.listdir(train_grand_dir)))
print('Total Images for Grand Canyon Validation: ', len(os.listdir(validation_grand_dir)))
print('Total Images for Grand Canyon Testing: ', len(os.listdir(test_grand_dir)))
print('Total Images for Yellowstone Training: ', len(os.listdir(train_yellow_dir)))
print('Total Images for Yellowstone Validation: ', len(os.listdir(validation_yellow_dir)))
print('Total Images for Yellowstone Testing: ', len(os.listdir(test_yellow_dir)))
print('Total Images for Everglades Training: ', len(os.listdir(train_glades_dir)))
print('Total Images for Everglades Validation: ', len(os.listdir(validation_glades_dir)))
print('Total Images for Everglades Testing: ', len(os.listdir(test_glades_dir)))

load = False
epochs = 100

if not load:
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.25))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(3, activation='sigmoid'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(learning_rate=1e-4), metrics=['accuracy'])

else:
    model = models.load_model(r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser/Model")

    model.summary()

train_data_gen = ImageDataGenerator(rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
test_data_gen = ImageDataGenerator(rescale=1./255)

train_generator = train_data_gen.flow_from_directory(train_dir, target_size=(200,200), batch_size=35, class_mode='categorical')
validation_generator = test_data_gen.flow_from_directory(validation_dir, target_size=(200,200), batch_size=25, class_mode='categorical')

history = model.fit(train_generator, steps_per_epoch=20, epochs=epochs, validation_data=validation_generator, validation_steps=6)

#model.save(r"/Users/tylermccue/Documents/GitHub/Deep-Learning-Project/GeoGuesser/Model")

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training Accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation Accuracy')
plt.title('Training and Validation Data')
plt.plot(epochs, loss, 'ro', label='Training Loss')
plt.plot(epochs, val_loss, 'r', label='Validation Loss')
plt.legend()
plt.show()