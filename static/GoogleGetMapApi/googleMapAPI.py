
# Python program to get a google map  
# image of specified location using  
# Google Static Maps API 
  
# importing required modules 
import requests

  
# Enter your api key here 
api_key = "AIzaSyDOO7Fb9wGFEPH99kWg00K4Nr-mBNtWB20"
  
# url variable store url 
#url = "https://maps.googleapis.com/maps/api/staticmap?center=40.714%2c%20-73.998&zoom=12&size=400x400&key=AIzaSyDOO7Fb9wGFEPH99kWg00K4Nr-mBNtWB20&signature=RLpb4x9y6-Fpg_Hu6Z0XtsE_Bfs="
url = "https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyDOO7Fb9wGFEPH99kWg00K4Nr-mBNtWB20&signature=UxG4CR3q3PLeEBtqwX-RZLPv7H0="

# center defines the center of the map, 
# equidistant from all edges of the map.  
center = "Dehradun"
  
# zoom defines the zoom 
# level of the map 
zoom = 10
  
# get method of requests module 
# return response object 
r = requests.get(url + "center =" + center + "&zoom =" +
                   str(zoom) + "&size = 400x400&key =" +
                             api_key + "sensor = false") 
  
# wb mode is stand for write binary mode 
f = open('location.png', 'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content) 
  
# close method of file object 
# save and close the file 
f.close() 

