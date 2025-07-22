import requests

# endpoint = "https://httpbin.org"  #simulate the HTTP request

# get_response = requests.get(endpoint)  #HTTP GET request to the endpoint
# print(get_response.text) #Prints the response text from the GET request(HTML content)


# endpoint = "https://httpbin.org/anything"  #simulate the API request

# get_response = requests.get(endpoint)
# print(get_response.text)  #JSON response from the API request
# print(get_response.json())

endpoint = "http://localhost:8000/api/"  #local API endpoint
get_response = requests.get(endpoint, params={"name": "John", "age": 30}, json={"query": "Hello World!"})
# print(get_response.text)
print(get_response.json())