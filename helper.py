import requests
import binascii
import os


def download_image(image_url, image_name, image_type):
    # image_url1 = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    # image_url2 = "http://www.gunnerkrigg.com//comics/00000001.jpg"
    _type = image_type.split('/')[1]

    f = open("./images/" + image_name + '.' + _type, 'wb')
    f.write(requests.get(image_url).content)
    f.close()

    return "./images/"+image_name + '.' + _type


def get_hex(image_loc):
    file = open(image_loc, 'rb')
    file_data = file.read()
    return binascii.hexlify(file_data)


def get_img(data, name, _type):
    data = data.strip()
    data = data.replace(' ', '')
    data = data.replace('\n', '')
    data = binascii.unhexlify(data)
    with open('./images/' + name + '.' + _type, 'wb') as image_file:
        image_file.write(data)

# def copyToImages(image_loc):
#     dest = './images'

#     path = copy2(image_loc, dest)
