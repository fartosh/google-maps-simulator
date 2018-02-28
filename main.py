#https://maps.googleapis.com/maps/api/staticmap?center=Gda%C5%84sk+Wrzeszcz&zoom=15&size=5000x5000

import ssl

context = ssl._create_unverified_context()

key = "AIzaSyBRfsVyW-uT-TQ5T5aU_HX4ywuh-ln5VO8"


# photo_wrzeszcz = requests.get("https://maps.googleapis.com/maps/api/staticmap?center=Gda%C5%84sk+Wrzeszcz&zoom=14&scale=2&size=640x640")
# with open("wrzeszcz.png", "wb") as plik:
#     plik.write(photo_wrzeszcz.content)
#     plik.close()
#
# req = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Raciborskiego+50+Gdansk&destination=Wilenska+3+Gdansk&key="+key)
# print(req.json())
