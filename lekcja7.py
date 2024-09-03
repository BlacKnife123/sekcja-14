from PIL import Image

nazwaPliku = "Tapeta.jpg"

image = Image.open(nazwaPliku)

width,height = image.size # zwraca krotkę (szerokość, wysokość)

print("Szerokość obrazka:", width)
print("Wysokość obrazka:", height)
