import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st
from playsound import playsound

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
st.subheader("Sensor 1")

audio_file = open('Alarm.wav', 'rb')
audio_bytes = audio_file.read()


#Sensor 1 Temperature 
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1708546/fields/1.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"1dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field1":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
x= float(fannie.group(1))
print(x)
st.write("Sensor 1 temperature is")
st.write(x)

if x > 38:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20temperatures%20above%2038%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1th/main/S1TH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif x <= 38:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20temperatures%20below%2035%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1tl/main/S1TL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)

#Sensor 1 Humidity
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1708546/fields/2.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"2dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field2":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
  x = float(fannie.group(1))
print(x)
st.write("Sensor 1 humidity is")
st.write(x)

if x > 50:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20humidity%20above%2050%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1hh/main/S1HH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif x <= 0:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%201%20has%20detected%20humidity%20below%2000%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s1hl/main/S1HL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)


st.subheader("Sensor 2")

#Sensor 1 Temperature 
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/1.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"1dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field1":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
x= float(fannie.group(1))
 
print(x)
st.write("Sensor 2 temperature is")
st.write(x)
if x > 38:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20temperatures%20above%2038%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2th/main/S2TH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif x < 35:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20temperatures%20below%2035%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2tl/main/S2TL.py)")  
  st.audio(audio_bytes, format='audio/wav', start_time=0)
 

#Sensor 1 Humidity
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/2.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"2dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field2":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
  x = float(fannie.group(1))
print(x)
st.write("Sensor 2 humidity is")
st.write(x)
if x > 50:
 telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20humidity%20levels%20above%2050%Percent%20.%20Stay%20alert")
 st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2hh/main/S2HH.py)")  
 st.audio(audio_bytes, format='audio/wav', start_time=0)
elif x < 0:
 telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%202%20has%20detected%20humidity%20levels%20below%200%Percent%20.%20Stay%20alert")
 st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s2hl/main/S2HL.py)") 
 st.audio(audio_bytes, format='audio/wav', start_time=0)
 

st.subheader("Sensor 3")

#Sensor 1 Temperature 
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/1.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"1dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field1":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
x= float(fannie.group(1))

print(x)
st.write("Sensor 3 temperature is")
st.write(x)
if x > 38:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20temperatures%20above%2038%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3th/main/S3TH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif x < 35:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20temperatures%20below%2035%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3tl/main/S3TL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
 

#Sensor 1 Humidity
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/2.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"2dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field2":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
  y = float(fannie.group(1))

print(y)
st.write("Sensor 3 humidity is")
st.write(y)

if y > 50:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20humidity%20above%2050%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3hh/main/S3HH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif y < 0:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%203%20has%20detected%20humidity%20below%200%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s3hl/main/S3HL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
  


st.subheader("Sensor 4")

#Sensor 1 Temperature 
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738082/fields/1.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"1dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field1":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
z= float(fannie.group(1))

print(z)
st.write("Sensor 4 temperature is")
st.write(z)
if z > 38:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20temperatures%20above%2038%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4th/main/S4TH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif z < 35:
  telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20temperatures%20below%2035%20degree%20celcius%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4tl/main/S4TL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)

#Sensor 1 Humidity
datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738082/fields/2.json?results=1");
select=repr(datafromwebsite.read());
select=select[::-1]
pick=re.search('}]}(.+?):"2dleif',select)
m=repr(pick);
m=m[::-1]
fannie=re.search('field2":"(.+?)"',m)
if fannie:
  print(fannie.group(1));
  z2 = float(fannie.group(1))
  print(z2)
st.write("Sensor 4 humidity is")
st.write(z2)

if z2 > 50:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20humidity%20above%2050%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4hh/main/S4HH.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)
elif z2 < 0:
  telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5351217346:AAECgdjzWMdRZFd0YPiSn1glvbODjEfhM1M/sendMessage?chat_id=@dfctunnel&text=Sensor%204%20has%20detected%20humidity%20below%200%20percent%20.%20Stay%20alert")
  st.write("[Threshold Reached>](https://share.streamlit.io/lbgletsoisa/s4hl/main/S4HL.py)")
  st.audio(audio_bytes, format='audio/wav', start_time=0)