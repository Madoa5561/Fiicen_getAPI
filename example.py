from FiicenAPI.getProfile import Fiicen

fiicen = Fiicen()

print(f"名前 : {fiicen.getName("m0yashi")} ")
print(f"アイコンURL : {fiicen.getIcon("m0yashi")} ")
