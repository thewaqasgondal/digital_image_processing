
import cv2
import os

image_path = r'C:\Users\waqas\PycharmProjects\wg_cv\image.png'
directory = r'C:\Users\waqas\PycharmProjects\wg_cv\output'

img = cv2.imread(image_path)

os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = 'savedImage.jpg'

cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')