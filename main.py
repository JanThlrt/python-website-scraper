import requests
from bs4 import BeautifulSoup


def get_website_title(url):
    try:
        response = requests.get(url)

        # Prüfen ob die Anfrage erfolgreich war
        if response.status_code != 200:
            print("Could not access website. Status code:", response.status_code)
            return

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title

        if title:
            print("Website Title:", title.string.strip())
        else:
            print("No title found on this page.")

    except requests.exceptions.RequestException:
        print("Invalid URL or connection error.")


def main():
    print("Website Scraper Started")
    url = input("Enter URL (including https://): ")
    get_website_title(url)


if __name__ == "__main__":
    main()