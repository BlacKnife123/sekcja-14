import requests

links = "dzialajace_strony.txt"

def is_exist(links):
    with open("strony.txt", "r", encoding="UTF-8") as file:
        for line in file:
            url = line.strip()  # Usuwa znaki nowej linii oraz spacje na początku i końcu
            try:
                response = requests.get(url, timeout=5)  # Ustawienie limitu czasowego na 5 sekund
                if response.status_code == 200:
                    with open(links, "a", encoding="UTF-8") as out_file:
                        out_file.write(url + "\n")
            except requests.exceptions.RequestException as e:
                print(f"Błąd połączenia dla URL: {url} - {e}")

is_exist(links)
