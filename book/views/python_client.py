import requests


resp = requests.get("http://127.0.0.1:8000/home-cbv/")
print(resp.content)

# resp1 = request.post("http://127.0.0.1:8000/home-cbv/")
# print(resp1.content)

# resp2 = request.delete("http://127.0.0.1:8000/home-cbv/")
# print(resp2.content)

# resp3 = request.put("http://127.0.0.1:8000/home-cbv/")
# print(resp3.content)

# resp4 = request.patch("http://127.0.0.1:8000/home-cbv/")
# print(resp4.content)

