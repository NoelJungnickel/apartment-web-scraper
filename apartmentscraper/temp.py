import bs4 as bs4
import chompjs

with open("../4kurfuerst.html", "r") as f:
    soup = bs4.BeautifulSoup(f, "html.parser")
    response = soup.find_all("script")
    Apartments = []
    for i in range(20, 21):
        string = "".join([s.strip() for s in response[i].text.splitlines()])
        start = string.split("};", 1)[0].find("settings")
        end = string.find("};")
        string = string[start + len("settings") : end] + "}"
        string = string.split("=", 1)[1].strip()
        Apartments.append(chompjs.parse_js_object(string))
    # print(chompjs.parse_js_object(string))
    # print(Apartments)
