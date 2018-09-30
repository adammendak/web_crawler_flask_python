from bs4 import BeautifulSoup
from model.single_element import SingleElement
import requests


class TextExtractor(object):
    """
    obiekt do wyciagania textu i obrazkow z htmla
    """

    @staticmethod
    def extract(url_to_extract):
        req = requests.get(url_to_extract)
        soup = BeautifulSoup(req.text, "html.parser")

        # znajdz liste obiektow tekstowych do zapisania
        data = soup.find_all(text=True)
        text_list = [i.strip() for i in data if i not in ['html', '\n', '\t']]
        text_to_save = []
        for t in text_list:
            paragraph = SingleElement(0, t, None)
            text_to_save.append(paragraph)

        # znajdz liste obrazkow do zapisania
        images = soup.find_all("img")
        images_to_save = []
        for i in images:
            image = SingleElement(1, None, i['src'])
            images_to_save.append(image)

        print(len(text_to_save))
        print(len(images_to_save))
        print("lol")

