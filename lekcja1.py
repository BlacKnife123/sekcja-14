import requests

link = []

def is_exist(link):
    link = input("Wpisz link który chcesz sprawdzić: ")
    url = requests.get(link)
    if(int(url.status_code) != 200 ):
        with open("strony.txt","a",encoding="UTF-8") as file:
            file.write(link + "\n")

    else:
        print("Udało się połączyć ze stroną")

i = 0 #pętla jest po to aby wprowadzać kilka na raz a nie żeby startować co chwila skrypt
for i in range(4):
    is_exist(link)