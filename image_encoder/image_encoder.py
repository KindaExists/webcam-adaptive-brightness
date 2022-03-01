import os
import base64

for file in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/assets'):
    filename = os.fsdecode(file)
    if filename.endswith('.png') or filename.endswith('.ico'):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/assets/' + filename, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
        print(filename)
        print(encoded_string)
        print('===============================')