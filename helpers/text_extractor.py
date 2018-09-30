from bs4 import BeautifulSoup
from model.single_element import SingleElement
import requests


class TextExtractor(object):
    """
    obiekt do wyciagania textu i obrazkow z htmla
    """

    @staticmethod
    def extract(url_to_extract, domain):
        # usun wszystkie elementy z poprzedniego wyszukania dla danej domeny
        SingleElement.delete_all_elements_for_domain(domain)

        req = requests.get(url_to_extract)
        soup = BeautifulSoup(req.text, "html.parser")

        # znajdz liste obiektow tekstowych do zapisania
        data = soup.find_all(text=True)
        text_list = [i.strip() for i in data if i not in ['html', '\n', '\t']]
        text_to_save = []
        for t in text_list:
            paragraph = SingleElement(0, t, None, domain)
            text_to_save.append(paragraph)

        # znajdz liste obrazkow do zapisania
        images = soup.find_all("img")
        images_to_save = []
        for i in images:
            image = SingleElement(1, None, TextExtractor.normalize_src(i['src'], url_to_extract), domain)
            images_to_save.append(image)

    @classmethod
    def normalize_src(cls, src, url_to_extract):
        if str(src).startswith("./"):
            src = str(src)[2:]

        if str(src).startswith("/"):
            src = str(src)[1:]

        if str(src).find("www") == -1:
            src = url_to_extract + "/" + str(src)

        return src

