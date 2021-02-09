# get day number from google api and display it to single digit 7 segement display
import requests
import digit

result =  requests.get('https://script.google.com/macros/s/AKfycbwIFBdvKE5f7604Eb-s32QVg6BiPbpU29vIzKefhJGQZ0PSaroXkNvD/exec')
# print(result.text)
digit.display_init()

if result.text == 'OFF':
  digit.display_nb(10) # 10 = -
  print('displayed OFF -')
else:
  digit.display_nb(int(result.text))
  print('displayed:', result.text)
