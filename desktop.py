response = requests.get("https://www.seekpng.com/png/detail/101-1012015_baguette-baguette-png.png")


file = open("sample_image.png", "wb")

file.write(response.content)

file.close()
