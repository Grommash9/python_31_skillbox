import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

example_private_auto = r'\b\w\d{3}\w{2}\d{2,3}'
example_taxi = r'\b\w{2}\d{3}\d{2,3}'

private_auto_list = re.findall(example_private_auto, text)
taxi_list = re.findall(example_taxi, text)

print(f"Список номеров частных автомобилей: {private_auto_list}\n"
      f"Список номеров такси: {taxi_list}")

