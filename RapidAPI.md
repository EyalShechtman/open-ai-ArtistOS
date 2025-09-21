get albums: 

import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/albums/?ids=3IBcauSj5M2A6lTeffJzdv", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


album tracks: 

import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/album_tracks/?id=3IBcauSj5M2A6lTeffJzdv&offset=0&limit=300", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



album metadata

import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/album_metadata/?id=3IBcauSj5M2A6lTeffJzdv", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




