from bs4 import BeautifulSoup
import os

OS_PATH_DIR_NAME = str(os.path.join(os.path.dirname(__file__), "static/index.html"))


def add_static_to_angular_dist_files(dir_name):
    """
    skrypt do dodania "/static" w plikach tworzonych z angulara
    """

    soup = BeautifulSoup(open(dir_name), "html.parser")

    for script in soup.find_all("script"):
        if "static" not in script['src']:
            script['src'] = "static/" + script['src']

    with open(dir_name, "w") as file:
        file.write(str(soup))


add_static_to_angular_dist_files(OS_PATH_DIR_NAME)
