import requests


ascii_art = """
 ____    ___    ___   _____   ____  _____  _____  _  __
|  _ \  / _ \  / _ \ |_   _| / ___|| ____|| ____|| |/ /
| |_) || | | || | | |  | |  | |  _ |  _|  |  _|  | ' / 
|  _ < | |_| || |_| |  | |  | |_| || |___ | |___ | . \ 
|_| \_\ \___/  \___/   |_|   \____||_____||_____||_|\_\
"""

def url_decoder(url):
    try:
        response = requests.head(url, allow_redirects=True)
        decoded_url = response.url
        return decoded_url
    except requests.exceptions.RequestException:
        return "Entschlüsselung fehlgeschlagen: Fehler bei der Verbindung zum Shortener-Dienst."

if __name__ == "__main__":
    print(ascii_art)
    short_url = "http://bitly.ws/M5bs"  # Beispiel für die Zwischen-URL

    decoded_url = url_decoder(short_url)
    print("Entschlüsselter Original-Link:", decoded_url)
