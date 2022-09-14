#### Задание
Починить программу (выводить значение скорости и направления ветра в N-ной точке)
```
import requests
response = requests.past("https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0")
points = response.json()
wind = points['data'][1000]['wind10m']
print(wind)
```
