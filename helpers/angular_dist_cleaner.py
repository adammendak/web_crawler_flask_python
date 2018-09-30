from bs4 import BeautifulSoup


def add_static_to_angular_dist_files(dir_name):
    """
    jak wywoluje skrypt ktory napisalem dla angulara npm run build to usuwa i zamienia pliki w static z
    tych ktore sa tworzone przez angulara w /dist
    ale scripty i style w pliku html maja src bez "/static" i nie dziala we flasku, wiec napisalem mala
    metode ktora dodaje /static tam gdzie go nie ma, sztuka dla sztuki w sumie :)
    """

    soup = BeautifulSoup(open(dir_name), "html.parser")

    for script in soup.find_all("script"):
        if "static" not in script['src']:
            script['src'] = "static/" + script['src']

    with open(dir_name, "w") as file:
        file.write(str(soup))