import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()


END_POINT = "https://pixe.la/v1/users"



USERNAME=os.getenv("USERNAME")
TOKEN= os.environ.get('Token')
GRAPH_ID=os.getenv("GRAPH_ID")

USER_PARAMETERS = {
    'token':TOKEN ,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=END_POINT, json=USER_PARAMETERS)
# print(response.status_code)
# print(response.json())
# print(response.text)

graph_endpoint=f"{END_POINT}/{USERNAME}/graphs"

browsing_the_graph=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
# like we passed the Api key along in parameters earlier but there are some
# websites which offer to protect such keys using header which can not be stolen and are stored under 'header'

graph_config = {
    'id':GRAPH_ID,
    'name': 'Cycling Graph',
    'unit' : 'Km',
    'type' : 'float',
    'color': 'ichou',
}

# this is authenticating using header

header={
    "X-USER-TOKEN":TOKEN
}

# graph_response= requests.post(url=graph_endpoint,headers=header,json=graph_config)
# print(graph_response.status_code)
# print(graph_response.text)

# now adding a pixel to the graph and refer to the API documentation for all the steps which are being followed
yesterday=datetime(year=2024,month=1,day=2)


adding_pixel_params={
    'date': yesterday.strftime("%Y%m%d"),
        'quantity':'15'
}
adding_pixel_end_point=f"{END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"

# adding_request=requests.post(url=adding_pixel_end_point,headers=header,json=adding_pixel_params)
# print(adding_request.text)

# now updating and deleting the pixel
updating_endpoint=f"{END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
request_body={
    'quantity':'9'
}
# update_request=requests.put(url=updating_endpoint,headers=header,json=request_body)
# print(update_request.text)

# deleting the pixel
# delete_request=requests.delete(url=updating_endpoint,headers=header)
# print(delete_request.text)

