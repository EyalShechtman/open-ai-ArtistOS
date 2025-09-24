# Spotify RapidAPI Documentation

This document contains examples for various Spotify API endpoints through RapidAPI.

## Table of Contents

- [Get Albums](#get-albums)
- [Album Tracks](#album-tracks)
- [Album Metadata](#album-metadata)
- [Artist Overview](#artist-overview)
- [Artist Discography](#artist-discography)
- [Artist Singles](#artist-singles)
- [Artist Appears On](#artist-appears-on)
- [Artist Related](#artist-related)
- [Track Lyrics](#track-lyrics)

## Get Albums

Retrieves album information for given Spotify album IDs.

```python
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
```

**Response:**
```json
{
  "albums": [
    {
      "album_type": "album",
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
          },
          "id": "51DevdOxIJin6DB1FXJpD1",
          "name": "UZI",
          "type": "artist",
          "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
        }
      ],
      "copyrights": [
        {
          "text": "2021 M.O.B Entertainment Associated Label Of Govinet",
          "type": "C"
        },
        {
          "text": "2021 M.O.B Entertainment Associated Label Of Govinet",
          "type": "P"
        }
      ],
      "external_ids": {
        "upc": "3616553578384"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/album/3IBcauSj5M2A6lTeffJzdv"
      },
      "genres": [],
      "id": "3IBcauSj5M2A6lTeffJzdv",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab67616d0000b27367c738a703dc979f5c3c52ef",
          "width": 640
        },
        {
          "height": 300,
          "url": "https://i.scdn.co/image/ab67616d00001e0267c738a703dc979f5c3c52ef",
          "width": 300
        },
        {
          "height": 64,
          "url": "https://i.scdn.co/image/ab67616d0000485167c738a703dc979f5c3c52ef",
          "width": 64
        }
      ],
      "label": "M.O.B. Entertainment",
      "name": "Kan",
      "popularity": 77,
      "release_date": "2021-03-19",
      "release_date_precision": "day",
      "total_tracks": 10,
      "tracks": {
        "items": [
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 211016,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/5jvhTc0g18kwYQNUJM5C4e"
            },
            "id": "5jvhTc0g18kwYQNUJM5C4e",
            "is_local": false,
            "is_playable": true,
            "name": "Makina",
            "preview_url": "https://p.scdn.co/mp3-preview/26d19b78d0470a426e3c5c80a0a1ec215f48521e?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:5jvhTc0g18kwYQNUJM5C4e"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 185458,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/72t3CRd8YEFrlc3x0OVaob"
            },
            "id": "72t3CRd8YEFrlc3x0OVaob",
            "is_local": false,
            "is_playable": true,
            "name": "Umrumda Değil",
            "preview_url": "https://p.scdn.co/mp3-preview/957b21793cfa732a195d1db728eaa28fe9cabc0b?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 2,
            "type": "track",
            "uri": "spotify:track:72t3CRd8YEFrlc3x0OVaob"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              },
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/3BVPc9s4JXzM6O1InlLxED"
                },
                "id": "3BVPc9s4JXzM6O1InlLxED",
                "name": "Mavi",
                "type": "artist",
                "uri": "spotify:artist:3BVPc9s4JXzM6O1InlLxED"
              }
            ],
            "disc_number": 1,
            "duration_ms": 200000,
            "explicit": false,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/5TkQatzJqKafPgHQerZ0dL"
            },
            "id": "5TkQatzJqKafPgHQerZ0dL",
            "is_local": false,
            "is_playable": true,
            "name": "Gecenin Içine Gir",
            "preview_url": "https://p.scdn.co/mp3-preview/62a08e83bf51c1c9c01bc9c7a706fdda26f1d51b?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 3,
            "type": "track",
            "uri": "spotify:track:5TkQatzJqKafPgHQerZ0dL"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 243205,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/6IW5ocUH5DRWagxkLTlbUS"
            },
            "id": "6IW5ocUH5DRWagxkLTlbUS",
            "is_local": false,
            "is_playable": true,
            "name": "Nedenini Sorma",
            "preview_url": "https://p.scdn.co/mp3-preview/8b62b6e53ecd5307f1872c1390daf7053a495e8c?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 4,
            "type": "track",
            "uri": "spotify:track:6IW5ocUH5DRWagxkLTlbUS"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              },
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/7GaMopkesD4KK9dNbgyO5D"
                },
                "id": "7GaMopkesD4KK9dNbgyO5D",
                "name": "Eko Fresh",
                "type": "artist",
                "uri": "spotify:artist:7GaMopkesD4KK9dNbgyO5D"
              }
            ],
            "disc_number": 1,
            "duration_ms": 152301,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/1ijjjMFlM3Pe8t3ykXBzxk"
            },
            "id": "1ijjjMFlM3Pe8t3ykXBzxk",
            "is_local": false,
            "is_playable": true,
            "name": "Mahalle",
            "preview_url": "https://p.scdn.co/mp3-preview/22decb29effb88818217b4bfeda6e783022162c4?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 5,
            "type": "track",
            "uri": "spotify:track:1ijjjMFlM3Pe8t3ykXBzxk"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 171880,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/4a1WLOoydq7u011UG9jjC9"
            },
            "id": "4a1WLOoydq7u011UG9jjC9",
            "is_local": false,
            "is_playable": true,
            "name": "Krvn",
            "preview_url": "https://p.scdn.co/mp3-preview/d926087a76e97d335af154a73dc3149eddd7b0c9?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 6,
            "type": "track",
            "uri": "spotify:track:4a1WLOoydq7u011UG9jjC9"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 155010,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/4hy4nY2PiYWx8qVXjpky3P"
            },
            "id": "4hy4nY2PiYWx8qVXjpky3P",
            "is_local": false,
            "is_playable": true,
            "name": "Vur",
            "preview_url": "https://p.scdn.co/mp3-preview/4d3df748ceb96ee16d38f761043c6994992f31b2?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 7,
            "type": "track",
            "uri": "spotify:track:4hy4nY2PiYWx8qVXjpky3P"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              },
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/6dOAGo4z0syiCjbnlh4VSO"
                },
                "id": "6dOAGo4z0syiCjbnlh4VSO",
                "name": "Critical",
                "type": "artist",
                "uri": "spotify:artist:6dOAGo4z0syiCjbnlh4VSO"
              }
            ],
            "disc_number": 1,
            "duration_ms": 223608,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/4PpYi6USHlY7OhOcDASnD3"
            },
            "id": "4PpYi6USHlY7OhOcDASnD3",
            "is_local": false,
            "is_playable": true,
            "name": "Davetiye",
            "preview_url": "https://p.scdn.co/mp3-preview/894fe4feaa99230fbab7d17fbe941de1bb4051d2?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 8,
            "type": "track",
            "uri": "spotify:track:4PpYi6USHlY7OhOcDASnD3"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              },
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/3R27mVPp04i87RNmvysZfY"
                },
                "id": "3R27mVPp04i87RNmvysZfY",
                "name": "Stap",
                "type": "artist",
                "uri": "spotify:artist:3R27mVPp04i87RNmvysZfY"
              }
            ],
            "disc_number": 1,
            "duration_ms": 196682,
            "explicit": true,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/5gx3dMxQGJ1JDw5qHarRqp"
            },
            "id": "5gx3dMxQGJ1JDw5qHarRqp",
            "is_local": false,
            "is_playable": true,
            "name": "Elhamdulillah",
            "preview_url": "https://p.scdn.co/mp3-preview/f5884c8e26c74eaec37742dafd14b487a32ea647?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 9,
            "type": "track",
            "uri": "spotify:track:5gx3dMxQGJ1JDw5qHarRqp"
          },
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1"
                },
                "id": "51DevdOxIJin6DB1FXJpD1",
                "name": "UZI",
                "type": "artist",
                "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1"
              }
            ],
            "disc_number": 1,
            "duration_ms": 192694,
            "explicit": false,
            "external_urls": {
              "spotify": "https://open.spotify.com/track/4PUniKS3Cywu23xjdtoji5"
            },
            "id": "4PUniKS3Cywu23xjdtoji5",
            "is_local": false,
            "is_playable": true,
            "name": "Outro",
            "preview_url": "https://p.scdn.co/mp3-preview/a82bb77bd5a75b682fee63259219fea01d42b7ee?cid=f6a40776580943a7bc5173125a1e8832",
            "track_number": 10,
            "type": "track",
            "uri": "spotify:track:4PUniKS3Cywu23xjdtoji5"
          }
        ],
        "limit": 50,
        "next": null,
        "offset": 0,
        "previous": null,
        "total": 10
      },
      "type": "album",
      "uri": "spotify:album:3IBcauSj5M2A6lTeffJzdv"
    }
  ]
}
```










## Album Tracks

Retrieves tracks from a specific album with pagination support.

```python
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
```

**Response:**
```json
{
  "data": {
    "album": {
      "playability": {
        "playable": true
      },
      "tracks": {
        "totalCount": 10,
        "items": [
          {
            "uid": "3d026f76adb5928f0e59",
            "track": {
              "saved": false,
              "uri": "spotify:track:5jvhTc0g18kwYQNUJM5C4e",
              "name": "Makina",
              "playcount": "64845125",
              "discNumber": 1,
              "trackNumber": 1,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 211016
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "419656ce995b7d2148d1",
            "track": {
              "saved": false,
              "uri": "spotify:track:72t3CRd8YEFrlc3x0OVaob",
              "name": "Umrumda Değil",
              "playcount": "69745254",
              "discNumber": 1,
              "trackNumber": 2,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 185458
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "dbfa6b79b176daea3899",
            "track": {
              "saved": false,
              "uri": "spotify:track:5TkQatzJqKafPgHQerZ0dL",
              "name": "Gecenin Içine Gir",
              "playcount": "5656390",
              "discNumber": 1,
              "trackNumber": 3,
              "contentRating": {
                "label": "NONE"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 200000
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:3BVPc9s4JXzM6O1InlLxED",
                    "profile": {
                      "name": "Mavi"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "58f3989f6fdefaf1c9be",
            "track": {
              "saved": false,
              "uri": "spotify:track:6IW5ocUH5DRWagxkLTlbUS",
              "name": "Nedenini Sorma",
              "playcount": "7163038",
              "discNumber": 1,
              "trackNumber": 4,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 243205
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "15dadc3ce6fa19b40977",
            "track": {
              "saved": false,
              "uri": "spotify:track:1ijjjMFlM3Pe8t3ykXBzxk",
              "name": "Mahalle",
              "playcount": "3992148",
              "discNumber": 1,
              "trackNumber": 5,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 152301
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:7GaMopkesD4KK9dNbgyO5D",
                    "profile": {
                      "name": "Eko Fresh"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "d465e72cf8573ced392a",
            "track": {
              "saved": false,
              "uri": "spotify:track:4a1WLOoydq7u011UG9jjC9",
              "name": "Krvn",
              "playcount": "81796749",
              "discNumber": 1,
              "trackNumber": 6,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 171880
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "b13b0f5f5cc4e9cb104a",
            "track": {
              "saved": false,
              "uri": "spotify:track:4hy4nY2PiYWx8qVXjpky3P",
              "name": "Vur",
              "playcount": "6809702",
              "discNumber": 1,
              "trackNumber": 7,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 155010
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "cc1f597105ee3f74e5ef",
            "track": {
              "saved": false,
              "uri": "spotify:track:4PpYi6USHlY7OhOcDASnD3",
              "name": "Davetiye",
              "playcount": "8348391",
              "discNumber": 1,
              "trackNumber": 8,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 223608
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:6dOAGo4z0syiCjbnlh4VSO",
                    "profile": {
                      "name": "Critical"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "a65e4830380ecca8e75e",
            "track": {
              "saved": false,
              "uri": "spotify:track:5gx3dMxQGJ1JDw5qHarRqp",
              "name": "Elhamdulillah",
              "playcount": "3312779",
              "discNumber": 1,
              "trackNumber": 9,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 196682
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:3R27mVPp04i87RNmvysZfY",
                    "profile": {
                      "name": "Stap"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "e540efaba938853ed3b6",
            "track": {
              "saved": false,
              "uri": "spotify:track:4PUniKS3Cywu23xjdtoji5",
              "name": "Outro",
              "playcount": "5463758",
              "discNumber": 1,
              "trackNumber": 10,
              "contentRating": {
                "label": "NONE"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 192694
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  }
}
```


## Album Metadata

Retrieves detailed metadata for a specific album.

```python
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
```

**Response:**
```json
{
  "data": {
    "album": {
      "uri": "spotify:album:3IBcauSj5M2A6lTeffJzdv",
      "name": "Kan",
      "artists": {
        "totalCount": 1,
        "items": [
          {
            "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
            "profile": {
              "name": "UZI"
            },
            "visuals": {
              "avatarImage": {
                "sources": [
                  {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8a2705cb98493cc305b0fde9",
                    "width": 640,
                    "height": 640
                  },
                  {
                    "url": "https://i.scdn.co/image/ab6761610000f1788a2705cb98493cc305b0fde9",
                    "width": 160,
                    "height": 160
                  }
                ]
              }
            },
            "sharingInfo": {
              "shareUrl": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1?si=uV-fBv5-RZym5y9-ev10xA"
            }
          }
        ]
      },
      "coverArt": {
        "extractedColors": {
          "colorRaw": {
            "hex": "#404040"
          }
        },
        "sources": [
          {
            "url": "https://i.scdn.co/image/ab67616d00001e0267c738a703dc979f5c3c52ef",
            "width": 300,
            "height": 300
          },
          {
            "url": "https://i.scdn.co/image/ab67616d0000485167c738a703dc979f5c3c52ef",
            "width": 64,
            "height": 64
          },
          {
            "url": "https://i.scdn.co/image/ab67616d0000b27367c738a703dc979f5c3c52ef",
            "width": 640,
            "height": 640
          }
        ]
      },
      "discs": {
        "totalCount": 1,
        "items": [
          {
            "number": 1,
            "tracks": {
              "totalCount": 10
            }
          }
        ]
      },
      "tracks": {
        "totalCount": 10,
        "items": [
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 211016
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 185458
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 200000
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 243205
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 152301
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 171880
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 155010
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 223608
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 196682
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 192694
              }
            }
          }
        ]
      },
      "releases": {
        "totalCount": 0,
        "items": []
      },
      "type": "ALBUM",
      "date": {
        "isoString": "2021-03-19T00:00:00Z",
        "precision": "DAY"
      },
      "playability": {
        "playable": true,
        "reason": "PLAYABLE"
      },
      "label": "M.O.B. Entertainment",
      "copyright": {
        "totalCount": 2,
        "items": [
          {
            "type": "C",
            "text": "2021 M.O.B Entertainment Associated Label Of Govinet"
          },
          {
            "type": "P",
            "text": "2021 M.O.B Entertainment Associated Label Of Govinet"
          }
        ]
      },
      "courtesyLine": "",
      "saved": false,
      "sharingInfo": {
        "shareUrl": "https://open.spotify.com/album/3IBcauSj5M2A6lTeffJzdv?si=WEC_y3k6RMqAYdUK07iQuA",
        "shareId": "WEC_y3k6RMqAYdUK07iQuA"
      },
      "moreAlbumsByArtist": {
        "items": [
          {
            "discography": {
              "popularReleases": {
                "items": []
              }
            }
          }
        ]
      }
    }
  }
}
```








## Artist Overview

Retrieves comprehensive information about an artist including biography, stats, and profile details.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/artist_overview/?id=2w9zwq3AktTeYYMuhMjju8", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "data": {
    "artist": {
      "id": "2w9zwq3AktTeYYMuhMjju8",
      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
      "following": false,
      "sharingInfo": {
        "shareUrl": "https://open.spotify.com/artist/2w9zwq3AktTeYYMuhMjju8?si=8HEMfSflRbqqgKLlG9z_lQ",
        "shareId": "8HEMfSflRbqqgKLlG9z_lQ"
      },
      "profile": {
        "name": "INNA",
        "verified": true,
        "pinnedItem": {
          "comment": "",
          "type": "PLAYLIST",
          "item": {
            "uri": "spotify:user:innaofficial:playlist:5fTCpsYWArmhL7001XP9up",
            "name": "INNA - Complete Playlist ",
            "images": {
              "items": [
                {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab67706c0000da84cd928ebf038cfb82f9de2b1d",
                      "width": 640,
                      "height": 640
                    }
                  ]
                }
              ]
            }
          }
        },
        "biography": {
          "text": "With an impressive string of hits, numerous awards under her trendy belt and concerts throughout Europe, Asia, Latin America, USA, Canada and the Middle East, <a href=\"spotify:artist:2w9zwq3AktTeYYMuhMjju8\" data-name=\"INNA\">INNA</a> is truly a fierce musical phenomenon, one of those larger-than-life stars of the moment.\n\nOne of the most exciting voices in the dance world, the Romanian artist has blazed through the global charts with hits like Hot, Sun Is Up or Déjà vu, reaching the top slots in dozen of countries, from Romania, to Japan, Mexico, Turkey, Argentina, Spain, Finland, Poland and the U.S.\n\nThe queen of dance music collaborated with lots of top worldwide artists like <a href=\"spotify:artist:0TnOYISbd1XYRBk9myaseg\" data-name=\"Pitbull\">Pitbull</a>, <a href=\"spotify:artist:0jnsk9HBra6NMjO2oANoPY\" data-name=\"Flo Rida\">Flo Rida</a>, <a href=\"spotify:artist:4VMYDCV2IEDYJArk749S6m\" data-name=\"Daddy Yankee\">Daddy Yankee</a>, <a href=\"spotify:artist:1ackd5XprZEkH3McKbQD51\" data-name=\"Juan Magán\">Juan Magán</a>, <a href=\"spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5\" data-name=\"J Balvin\">J Balvin</a>, <a href=\"spotify:artist:0eHQ9o50hj6ZDNBt6Ys1sD\" data-name=\"Yandel\">Yandel</a>, <a href=\"spotify:artist:0NGAZxHanS9e0iNHpR8f2W\" data-name=\"Alok\">Alok</a> &amp; <a href=\"spotify:artist:586uxXMyD5ObPuzjtrzO1Q\" data-name=\"Sofi Tukker\">Sofi Tukker</a>. Her most recent feature with the american artist <a href=\"spotify:artist:3Isy6kedDrgPYoTS1dazA9\" data-name=\"Sean Paul\">Sean Paul</a> for the song “Up”, has become an international sensation.\n\nWith looks and dance moves that match her musical talent, INNA has won multiple MTV Europe Awards, Romanian Music Awards and RRA Awards, and in 2012 became the first and only European female artist to reach 1 billion YouTube views. INNA now has more than 4 billion views on her official Youtube channel, and more than 6.1 billion views on other channels as well.\n\n2022 begins in full force for INNA, delighting her fans with a new album created in Dance Queen’s House, a special project that consisted of 16 days of music sessions in a house with producers and songwriters, everything being posted on INNA’s socials as a daily vlog. The album is called <a href=\"spotify:album:62XwEYC2iJIX37oZlJbsvi\" data-name=\"Champagne Problems #DQH1\">Champagne Problems #DQH1</a>."
        },
        "externalLinks": {
          "items": [
            {
              "name": "FACEBOOK",
              "url": "https://facebook.com/Inna"
            },
            {
              "name": "INSTAGRAM",
              "url": "https://instagram.com/inna"
            },
            {
              "name": "TWITTER",
              "url": "https://twitter.com/inna_ro"
            },
            {
              "name": "WIKIPEDIA",
              "url": "https://en.wikipedia.org/wiki/Inna"
            }
          ]
        },
        "playlists": {
          "totalCount": 8,
          "items": [
            {
              "uri": "spotify:playlist:3ybECzzbi7noSrZKNvesTN",
              "name": "INNA | Dance Playlist",
              "description": "Dance like there&#x27;s no tomorrow. 💃🕺",
              "owner": {
                "name": "INNA"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84b077af4a159fed8ca0b2e297",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:4r0ecmvlzJJWGecHxVnA4c",
              "name": "INNA | Touring Playlist ",
              "description": "This one&#x27;s for you, Club Rockers! 🤘 I compiled a list of my songs that will make you sing. ✨",
              "owner": {
                "name": "INNA"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da841ab8825174f37471a19b17dd",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:1liF44HtExxNieC9oGmftD",
              "name": "INNA | Workout Playlist ",
              "description": "This one is for you, Workout Lovers. I compiled a list of songs that will bring you energy.✨ Workout vibes for days. 🏋🏻‍♂️",
              "owner": {
                "name": "INNA"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84ca97da49087fcf8432395dd5",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:0oT9tEz4BfqS3lxMofnabS",
              "name": "INNA | Ride the Vibes",
              "description": "Let&#x27;s ride the vibes together! 🛹",
              "owner": {
                "name": "INNA"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84241a2881008be0bb87829930",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:1lTNpzNMI1PKQaGAvdQ5vf",
              "name": "13 Years Of INNA | Anniversary Playlist",
              "description": "Thank you for being part of my journey! This playlist is a selection made up of my entire career HITS! Enjoy!",
              "owner": {
                "name": "INNA"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da840f88513089b45717cf60c2e0",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:0Kp97jDlHwYdDEJKx1zZtC",
              "name": "INNA - Champagne Problems #DQH1",
              "description": "Follow and listen to the latest songs by INNA including her latest Album! INNA: Essentials playlist is the best way to get you right into your feels. Press Play and Enjoy!",
              "owner": {
                "name": "GLOBAL RECORDS"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da848e6697ae633e3a7a3a23fdba",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:1MRaYvIR5BwhvIBtql7fgH",
              "name": "Global Records Top 40",
              "description": "This is the definition of a Best Of. Carefully curated music by our very own in-house editors. 🙋‍♂🙋‍♀",
              "owner": {
                "name": "GLOBAL RECORDS"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da8430f70e7f716cc6ccdef82ff4",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:7wlwuwOAtDaUmCPoTrlM7W",
              "name": "Romania Top 40 Hits",
              "description": "This is Romania Top 40. Great music only, constant updates, perfectly suited for your tastes. 🎯 ",
              "owner": {
                "name": "GLOBAL RECORDS"
              },
              "images": {
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84488aa14678c9c20157a6a5ba",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      },
      "visuals": {
        "gallery": {
          "items": [
            {
              "sources": [
                {
                  "url": "https://i.scdn.co/image/ab6761670000ecd403d8cd0eee5f305be414ab4d",
                  "width": 640,
                  "height": 640
                }
              ]
            },
            {
              "sources": [
                {
                  "url": "https://i.scdn.co/image/ab6761670000ecd4e9a2fdb66499f61c0fc01bd3",
                  "width": 640,
                  "height": 640
                }
              ]
            },
            {
              "sources": [
                {
                  "url": "https://i.scdn.co/image/ab6761670000ecd4f8f5f823eea1a3ab03de0a8a",
                  "width": 640,
                  "height": 640
                }
              ]
            },
            {
              "sources": [
                {
                  "url": "https://i.scdn.co/image/ab6761670000ecd4dc650b908920b4cf4232478c",
                  "width": 640,
                  "height": 640
                }
              ]
            },
            {
              "sources": [
                {
                  "url": "https://i.scdn.co/image/ab6761670000ecd479cdb6ad07f8ebd4ea1848bd",
                  "width": 640,
                  "height": 640
                }
              ]
            }
          ]
        },
        "avatarImage": {
          "sources": [
            {
              "url": "https://i.scdn.co/image/ab6761610000e5eb571bd5587850d252e8fc892d",
              "width": 640,
              "height": 640
            },
            {
              "url": "https://i.scdn.co/image/ab6761610000f178571bd5587850d252e8fc892d",
              "width": 160,
              "height": 160
            }
          ],
          "extractedColors": {
            "colorRaw": {
              "hex": "#1878A0"
            }
          }
        },
        "headerImage": {
          "sources": [
            {
              "url": "https://i.scdn.co/image/ab676186000010161d286d39a867225579e66532",
              "width": 2660,
              "height": 1140
            }
          ],
          "extractedColors": {
            "colorRaw": {
              "hex": "#005078"
            }
          }
        }
      },
      "discography": {
        "latest": {
          "id": "49D6ut4LdJCBD90wRWzfe6",
          "uri": "spotify:album:49D6ut4LdJCBD90wRWzfe6",
          "name": "Lalele",
          "type": "SINGLE",
          "copyright": {
            "items": [
              {
                "type": "C",
                "text": "2022 Global Records"
              },
              {
                "type": "P",
                "text": "2022 Global Records"
              }
            ]
          },
          "date": {
            "year": 2022
          },
          "coverArt": {
            "sources": [
              {
                "url": "https://i.scdn.co/image/ab67616d00001e021f43d9d7588ec1c832b8f2dc",
                "width": 300,
                "height": 300
              },
              {
                "url": "https://i.scdn.co/image/ab67616d000048511f43d9d7588ec1c832b8f2dc",
                "width": 64,
                "height": 64
              },
              {
                "url": "https://i.scdn.co/image/ab67616d0000b2731f43d9d7588ec1c832b8f2dc",
                "width": 640,
                "height": 640
              }
            ]
          },
          "tracks": {
            "totalCount": 1
          },
          "label": "Global Records",
          "playability": {
            "playable": true,
            "reason": "PLAYABLE"
          }
        },
        "popularReleases": {
          "totalCount": 0,
          "items": []
        },
        "singles": {
          "totalCount": 166,
          "items": [
            {
              "releases": {
                "items": [
                  {
                    "id": "49D6ut4LdJCBD90wRWzfe6",
                    "uri": "spotify:album:49D6ut4LdJCBD90wRWzfe6",
                    "name": "Lalele",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2022 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "2022 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2022,
                      "month": 1,
                      "day": 20,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021f43d9d7588ec1c832b8f2dc",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511f43d9d7588ec1c832b8f2dc",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731f43d9d7588ec1c832b8f2dc",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "Global Records",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "d7myd-H2SBiRvREjMBn8-A",
                      "shareUrl": "https://open.spotify.com/album/49D6ut4LdJCBD90wRWzfe6?si=d7myd-H2SBiRvREjMBn8-A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2jA1exLaHCcpHtDrGLKTmy",
                    "uri": "spotify:album:2jA1exLaHCcpHtDrGLKTmy",
                    "name": "UP",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records/Dutty Rock Music/EMI April Music Ltd"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 12,
                      "day": 17,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027bd254131ac1f8678448d076",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517bd254131ac1f8678448d076",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737bd254131ac1f8678448d076",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "BZjOCpP1SEGKtc7kucbaLA",
                      "shareUrl": "https://open.spotify.com/album/2jA1exLaHCcpHtDrGLKTmy?si=BZjOCpP1SEGKtc7kucbaLA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6uvP8hlbI9X3RleKNVmBzT",
                    "uri": "spotify:album:6uvP8hlbI9X3RleKNVmBzT",
                    "name": "UP (Robert Cristian Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 12,
                      "day": 3,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021271f5f16702f3516f86579d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511271f5f16702f3516f86579d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731271f5f16702f3516f86579d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "AaeS9wPAQ9G8LQXWH2lrzg",
                      "shareUrl": "https://open.spotify.com/album/6uvP8hlbI9X3RleKNVmBzT?si=AaeS9wPAQ9G8LQXWH2lrzg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5kjggiiZEcRzFvQ4rowAsQ",
                    "uri": "spotify:album:5kjggiiZEcRzFvQ4rowAsQ",
                    "name": "De Dragul Tău",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 11,
                      "day": 26,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02da7c4e91509943b3c7cf8ef4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851da7c4e91509943b3c7cf8ef4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273da7c4e91509943b3c7cf8ef4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "Global Records",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "FzKIMi2rQLq4diRCzddu5w",
                      "shareUrl": "https://open.spotify.com/album/5kjggiiZEcRzFvQ4rowAsQ?si=FzKIMi2rQLq4diRCzddu5w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "21x0bCve7UJ7ZAapjt8GFz",
                    "uri": "spotify:album:21x0bCve7UJ7ZAapjt8GFz",
                    "name": "UP",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 29,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0265f27da14d572556a8a59755",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485165f27da14d572556a8a59755",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27365f27da14d572556a8a59755",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "C_xKqpjRQvmd7m0BOFgP3Q",
                      "shareUrl": "https://open.spotify.com/album/21x0bCve7UJ7ZAapjt8GFz?si=C_xKqpjRQvmd7m0BOFgP3Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3wBRVC1SMfIEdsr9thFSYJ",
                    "uri": "spotify:album:3wBRVC1SMfIEdsr9thFSYJ",
                    "name": "UP (Vadim Adamov & Hardphol Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 28,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0200296e006391b562e8c70563",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485100296e006391b562e8c70563",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27300296e006391b562e8c70563",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GSRS6BNhTw6SOBXHH9d-xA",
                      "shareUrl": "https://open.spotify.com/album/3wBRVC1SMfIEdsr9thFSYJ?si=GSRS6BNhTw6SOBXHH9d-xA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "605jn7Lsj6RD4ovYCsnrxe",
                    "uri": "spotify:album:605jn7Lsj6RD4ovYCsnrxe",
                    "name": "UP (Mert Hakan & Onur Betin Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 28,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023a3334b5c3ac49b938312f03",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513a3334b5c3ac49b938312f03",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733a3334b5c3ac49b938312f03",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "H8hRlrxvRxCHA02dtp3SmA",
                      "shareUrl": "https://open.spotify.com/album/605jn7Lsj6RD4ovYCsnrxe?si=H8hRlrxvRxCHA02dtp3SmA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3QJqG1fLaNGsgjVUroIPCT",
                    "uri": "spotify:album:3QJqG1fLaNGsgjVUroIPCT",
                    "name": "UP (Filatov & Karas Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 28,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02d73086d4cbe065734d124185",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851d73086d4cbe065734d124185",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273d73086d4cbe065734d124185",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "HYdsSMaLST2n7wfHbo3pQw",
                      "shareUrl": "https://open.spotify.com/album/3QJqG1fLaNGsgjVUroIPCT?si=HYdsSMaLST2n7wfHbo3pQw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "57NJ9mlC0mPtXJAc6T9Q2g",
                    "uri": "spotify:album:57NJ9mlC0mPtXJAc6T9Q2g",
                    "name": "UP (Bzars Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 28,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0237f1c2da634da62a84370a09",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485137f1c2da634da62a84370a09",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27337f1c2da634da62a84370a09",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "qwfqpnTcSAiqm-9ciojJ6A",
                      "shareUrl": "https://open.spotify.com/album/57NJ9mlC0mPtXJAc6T9Q2g?si=qwfqpnTcSAiqm-9ciojJ6A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "53kblUkYfsJ5bYAb3yDO0s",
                    "uri": "spotify:album:53kblUkYfsJ5bYAb3yDO0s",
                    "name": "UP (Barlas & Mert Remix)",
                    "type": "SINGLE",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "exclusively licensed to Warner Music Poland for World except Romania, ℗ 2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2021,
                      "month": 10,
                      "day": 28,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022af676a3bccbfe4a9cf0408d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512af676a3bccbfe4a9cf0408d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732af676a3bccbfe4a9cf0408d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 1
                    },
                    "label": "WM Poland/WMI",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "LD_woBxjSiiE4mXVwYowZA",
                      "shareUrl": "https://open.spotify.com/album/53kblUkYfsJ5bYAb3yDO0s?si=LD_woBxjSiiE4mXVwYowZA"
                    }
                  }
                ]
              }
            }
          ]
        },
        "albums": {
          "totalCount": 11,
          "items": [
            {
              "releases": {
                "items": [
                  {
                    "id": "62XwEYC2iJIX37oZlJbsvi",
                    "uri": "spotify:album:62XwEYC2iJIX37oZlJbsvi",
                    "name": "Champagne Problems #DQH1",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2021 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "2021 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2022,
                      "month": 1,
                      "day": 7,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02482832441ba0b9f1ede62ae6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851482832441ba0b9f1ede62ae6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273482832441ba0b9f1ede62ae6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 8
                    },
                    "label": "Global Records",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "8Tsg40LzRGu4hacej7Q31g",
                      "shareUrl": "https://open.spotify.com/album/62XwEYC2iJIX37oZlJbsvi?si=8Tsg40LzRGu4hacej7Q31g"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3QFR3OduDKvQpTPsnmiYl9",
                    "uri": "spotify:album:3QFR3OduDKvQpTPsnmiYl9",
                    "name": "Heartbreaker",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2020 Global Records"
                        },
                        {
                          "type": "P",
                          "text": "2020 Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2020,
                      "month": 12,
                      "day": 4,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c1725be0a413be97208ccdca",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c1725be0a413be97208ccdca",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c1725be0a413be97208ccdca",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 10
                    },
                    "label": "Global Records",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "zHa1rB46Q9-k7-t0rSrSpA",
                      "shareUrl": "https://open.spotify.com/album/3QFR3OduDKvQpTPsnmiYl9?si=zHa1rB46Q9-k7-t0rSrSpA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4BaDuakq8ON5eOQFRoNYM5",
                    "uri": "spotify:album:4BaDuakq8ON5eOQFRoNYM5",
                    "name": "YO",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "© 2019 Global Records, Under Exclusive License to Roc Nation, LLC"
                        },
                        {
                          "type": "P",
                          "text": "℗ 2019 Global Records, Under Exclusive License to Roc Nation, LLC"
                        }
                      ]
                    },
                    "date": {
                      "year": 2019,
                      "month": 5,
                      "day": 31,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02eaa5b18552a3e2e9f95eb9ca",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851eaa5b18552a3e2e9f95eb9ca",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273eaa5b18552a3e2e9f95eb9ca",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 11
                    },
                    "label": "INNA / Roc Nation",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "WXvGUQo6TQiRsc2i1Jbe9Q",
                      "shareUrl": "https://open.spotify.com/album/4BaDuakq8ON5eOQFRoNYM5?si=WXvGUQo6TQiRsc2i1Jbe9Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1A2pvHdbhlvaRMJ7o8I09m",
                    "uri": "spotify:album:1A2pvHdbhlvaRMJ7o8I09m",
                    "name": "Nirvana",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2017 Yeni Dünya Müzik under exclusive license from Global Records"
                        },
                        {
                          "type": "P",
                          "text": "2017 Yeni Dünya Müzik under exclusive license from Global Records"
                        }
                      ]
                    },
                    "date": {
                      "year": 2018,
                      "month": 2,
                      "day": 2,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0235140cdf490e8625b4a81e24",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485135140cdf490e8625b4a81e24",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27335140cdf490e8625b4a81e24",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 10
                    },
                    "label": "YENİ DÜNYA MÜZİK",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "PdqWQjEITuWn4-25HudLYg",
                      "shareUrl": "https://open.spotify.com/album/1A2pvHdbhlvaRMJ7o8I09m?si=PdqWQjEITuWn4-25HudLYg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3KtkvnTpqK8zQPNT9v1zIh",
                    "uri": "spotify:album:3KtkvnTpqK8zQPNT9v1zIh",
                    "name": "Inna",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2015 Yeni Dünya Müzik under exclusive license from Roton"
                        },
                        {
                          "type": "P",
                          "text": "2015 Yeni Dünya Müzik under exclusive license from Roton"
                        }
                      ]
                    },
                    "date": {
                      "year": 2015,
                      "month": 11,
                      "day": 6,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f6cfdbc9435bd1c741a997ed",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f6cfdbc9435bd1c741a997ed",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f6cfdbc9435bd1c741a997ed",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 19
                    },
                    "label": "YENİ DÜNYA MÜZİK",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "QniMfNi6QbKUXHnVmpAhNA",
                      "shareUrl": "https://open.spotify.com/album/3KtkvnTpqK8zQPNT9v1zIh?si=QniMfNi6QbKUXHnVmpAhNA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2iIiwsEKIHPZXIHr1qO4fD",
                    "uri": "spotify:album:2iIiwsEKIHPZXIHr1qO4fD",
                    "name": "Party Never Ends, Pt. 2 (Deluxe Editon)",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2013 Roton"
                        },
                        {
                          "type": "P",
                          "text": "2013 Roton"
                        }
                      ]
                    },
                    "date": {
                      "year": 2013,
                      "month": 3,
                      "day": 4,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02813ec28d324f446a38bd7379",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851813ec28d324f446a38bd7379",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273813ec28d324f446a38bd7379",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 9
                    },
                    "label": "Roton Music",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "MHlxzwnyRlaTwn_OlEDtJA",
                      "shareUrl": "https://open.spotify.com/album/2iIiwsEKIHPZXIHr1qO4fD?si=MHlxzwnyRlaTwn_OlEDtJA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2qL4k9MmaPNgj2PMayGuHH",
                    "uri": "spotify:album:2qL4k9MmaPNgj2PMayGuHH",
                    "name": "Party Never Ends, Pt. 1 (Deluxe Edition)",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2013 Roton"
                        },
                        {
                          "type": "P",
                          "text": "2013 Roton"
                        }
                      ]
                    },
                    "date": {
                      "year": 2013,
                      "month": 3,
                      "day": 4,
                      "precision": "DAY"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0221e639a53f2707d4b32f7faf",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485121e639a53f2707d4b32f7faf",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27321e639a53f2707d4b32f7faf",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 16
                    },
                    "label": "Roton Music",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "MliBq_ldRLa_dSwLEr68pg",
                      "shareUrl": "https://open.spotify.com/album/2qL4k9MmaPNgj2PMayGuHH?si=MliBq_ldRLa_dSwLEr68pg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4lVMYJoQGTWtlggefBGef4",
                    "uri": "spotify:album:4lVMYJoQGTWtlggefBGef4",
                    "name": "Party Never Ends, Part 2 (Deluxe Edition)",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2013 Roton Music"
                        },
                        {
                          "type": "P",
                          "text": "2013 Roton Music"
                        }
                      ]
                    },
                    "date": {
                      "year": 2013,
                      "month": null,
                      "day": null,
                      "precision": "YEAR"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027daff2c7c8a71f644af6b265",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517daff2c7c8a71f644af6b265",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737daff2c7c8a71f644af6b265",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 9
                    },
                    "label": "Roton Music",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GYXTPZ2jRlSiQsGh0F7EYw",
                      "shareUrl": "https://open.spotify.com/album/4lVMYJoQGTWtlggefBGef4?si=GYXTPZ2jRlSiQsGh0F7EYw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "45WWiybURSpC7tslSxGnrf",
                    "uri": "spotify:album:45WWiybURSpC7tslSxGnrf",
                    "name": "Party Never Ends, Part 1 (Deluxe Edition)",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2013 Roton Music"
                        },
                        {
                          "type": "P",
                          "text": "2013 Roton Music"
                        }
                      ]
                    },
                    "date": {
                      "year": 2013,
                      "month": null,
                      "day": null,
                      "precision": "YEAR"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02789b5fef31115d1437e2d5a5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851789b5fef31115d1437e2d5a5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273789b5fef31115d1437e2d5a5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 16
                    },
                    "label": "Roton Music",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "D8kG_wN9SLC_8uzpePLM6g",
                      "shareUrl": "https://open.spotify.com/album/45WWiybURSpC7tslSxGnrf?si=D8kG_wN9SLC_8uzpePLM6g"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7LUW42pRwoFJV3bIFeliVJ",
                    "uri": "spotify:album:7LUW42pRwoFJV3bIFeliVJ",
                    "name": "I Am the Club Rocker",
                    "type": "ALBUM",
                    "copyright": {
                      "items": [
                        {
                          "type": "C",
                          "text": "2011 Roton Music"
                        },
                        {
                          "type": "P",
                          "text": "2011 Roton Music"
                        }
                      ]
                    },
                    "date": {
                      "year": 2011,
                      "month": null,
                      "day": null,
                      "precision": "YEAR"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02464f14f7c511222dc6c95b97",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851464f14f7c511222dc6c95b97",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273464f14f7c511222dc6c95b97",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "tracks": {
                      "totalCount": 13
                    },
                    "label": "Roton Music",
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "KaVULzIrT4SKthT7KT17CA",
                      "shareUrl": "https://open.spotify.com/album/7LUW42pRwoFJV3bIFeliVJ?si=KaVULzIrT4SKthT7KT17CA"
                    }
                  }
                ]
              }
            }
          ]
        },
        "compilations": {
          "totalCount": 0,
          "items": []
        },
        "topTracks": {
          "items": [
            {
              "uid": "086114147d04f674d102",
              "track": {
                "id": "2ykXJ9QVwx9Li8nsW0h6b2",
                "uri": "spotify:track:2ykXJ9QVwx9Li8nsW0h6b2",
                "name": "UP",
                "playcount": "9518118",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 148944
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    },
                    {
                      "uri": "spotify:artist:3Isy6kedDrgPYoTS1dazA9",
                      "profile": {
                        "name": "Sean Paul"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:2jA1exLaHCcpHtDrGLKTmy",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e027bd254131ac1f8678448d076"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d000048517bd254131ac1f8678448d076"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b2737bd254131ac1f8678448d076"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "837c05e5e259a594b3f1",
              "track": {
                "id": "3ajgQFhKuWa4Hz6VgkThuO",
                "uri": "spotify:track:3ajgQFhKuWa4Hz6VgkThuO",
                "name": "UP",
                "playcount": "11390916",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 150395
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:21x0bCve7UJ7ZAapjt8GFz",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e0265f27da14d572556a8a59755"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000485165f27da14d572556a8a59755"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b27365f27da14d572556a8a59755"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "51c499b19131b2f71ef6",
              "track": {
                "id": "7ltLi7CG003USSGYsSba9s",
                "uri": "spotify:track:7ltLi7CG003USSGYsSba9s",
                "name": "It Don’t Matter - Spotify Singles",
                "playcount": "54230626",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 173742
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:0NGAZxHanS9e0iNHpR8f2W",
                      "profile": {
                        "name": "Alok"
                      }
                    },
                    {
                      "uri": "spotify:artist:586uxXMyD5ObPuzjtrzO1Q",
                      "profile": {
                        "name": "Sofi Tukker"
                      }
                    },
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:5w5UPTvxo2vjCWnP5fbEnc",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e0260b16fc0b0cc5948f2173511"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000485160b16fc0b0cc5948f2173511"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b27360b16fc0b0cc5948f2173511"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "f46f541daf1df5fec615",
              "track": {
                "id": "7AB1TtGbNXkixdYZtJRb4u",
                "uri": "spotify:track:7AB1TtGbNXkixdYZtJRb4u",
                "name": "Flashbacks",
                "playcount": "20391277",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 177725
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:3QFR3OduDKvQpTPsnmiYl9",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e02c1725be0a413be97208ccdca"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d00004851c1725be0a413be97208ccdca"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b273c1725be0a413be97208ccdca"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "b77be47288fd9d66941b",
              "track": {
                "id": "2ZAOEPkOeZTGsjGHWyCThc",
                "uri": "spotify:track:2ZAOEPkOeZTGsjGHWyCThc",
                "name": "Cola Song (feat. J Balvin)",
                "playcount": "97986420",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 198245
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    },
                    {
                      "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5",
                      "profile": {
                        "name": "J Balvin"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:3153stlyNnwZT5tDZY6bZL",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e023a35e5d94f6cc67f4442e0a7"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d000048513a35e5d94f6cc67f4442e0a7"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b2733a35e5d94f6cc67f4442e0a7"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "9aa92f4188830663a618",
              "track": {
                "id": "7osGopqc6yUWHMEERUYFFB",
                "uri": "spotify:track:7osGopqc6yUWHMEERUYFFB",
                "name": "Oh My God",
                "playcount": "6547638",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 168220
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:1ieuMbqWl9HW9PUuMLchfi",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e025320b79cf9b66a3831d31b4d"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d000048515320b79cf9b66a3831d31b4d"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b2735320b79cf9b66a3831d31b4d"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "105bb25edae27fd1471e",
              "track": {
                "id": "679uDxkLbBdUTA3XB9RoCm",
                "uri": "spotify:track:679uDxkLbBdUTA3XB9RoCm",
                "name": "Summer's Not Ready",
                "playcount": "14916222",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 151961
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "EXPLICIT"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:0jnsk9HBra6NMjO2oANoPY",
                      "profile": {
                        "name": "Flo Rida"
                      }
                    },
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    },
                    {
                      "uri": "spotify:artist:0CbeG1224FS58EUx4tPevZ",
                      "profile": {
                        "name": "Timmy Trumpet"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:1G0XxPLeIcJZzAUILhiOA2",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e029d3cdfa53acb7f47ffa753b7"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d000048519d3cdfa53acb7f47ffa753b7"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b2739d3cdfa53acb7f47ffa753b7"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "54a375a856ceb65d6ed9",
              "track": {
                "id": "4sWH0Fhl1a6yBCXnYm73Jp",
                "uri": "spotify:track:4sWH0Fhl1a6yBCXnYm73Jp",
                "name": "Always On My Mind",
                "playcount": "2236384",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 164434
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:62XwEYC2iJIX37oZlJbsvi",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e02482832441ba0b9f1ede62ae6"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d00004851482832441ba0b9f1ede62ae6"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b273482832441ba0b9f1ede62ae6"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "07f786aa55a217247c0e",
              "track": {
                "id": "3gD2EgOb6UHhzPSz78xzvt",
                "uri": "spotify:track:3gD2EgOb6UHhzPSz78xzvt",
                "name": "Papa",
                "playcount": "4759734",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 166198
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:4oE7f7lNFkh0EbEZWEawBF",
                      "profile": {
                        "name": "SICKOTOY"
                      }
                    },
                    {
                      "uri": "spotify:artist:6Cej574CUx7dHKuRHBPNp0",
                      "profile": {
                        "name": "Elvana Gjata"
                      }
                    },
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:0fprmuiWAU7cCx64jG58HI",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e024cf5144feb940b6e5ddcf24f"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d000048514cf5144feb940b6e5ddcf24f"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b2734cf5144feb940b6e5ddcf24f"
                      }
                    ]
                  }
                }
              }
            },
            {
              "uid": "fdaec46d17a221a9f789",
              "track": {
                "id": "0SxeiJsGGIpzrvsEk3dZeE",
                "uri": "spotify:track:0SxeiJsGGIpzrvsEk3dZeE",
                "name": "Sober",
                "playcount": "13266211",
                "discNumber": 1,
                "duration": {
                  "totalMilliseconds": 162258
                },
                "playability": {
                  "playable": true,
                  "reason": "PLAYABLE"
                },
                "contentRating": {
                  "label": "NONE"
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    }
                  ]
                },
                "album": {
                  "uri": "spotify:album:7ol5R0cGYVflCySSwIsCAl",
                  "coverArt": {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67616d00001e02f56f13d5d7f5d62d3ec4f1f6"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d00004851f56f13d5d7f5d62d3ec4f1f6"
                      },
                      {
                        "url": "https://i.scdn.co/image/ab67616d0000b273f56f13d5d7f5d62d3ec4f1f6"
                      }
                    ]
                  }
                }
              }
            }
          ]
        }
      },
      "stats": {
        "followers": 1085323,
        "monthlyListeners": 7804823,
        "worldRank": 0,
        "topCities": {
          "items": [
            {
              "numberOfListeners": 176300,
              "city": "Mexico City",
              "country": "MX",
              "region": "CMX"
            },
            {
              "numberOfListeners": 172253,
              "city": "Istanbul",
              "country": "TR",
              "region": "34"
            },
            {
              "numberOfListeners": 146848,
              "city": "Warsaw",
              "country": "PL",
              "region": "14"
            },
            {
              "numberOfListeners": 102820,
              "city": "Santiago",
              "country": "CL",
              "region": "RM"
            },
            {
              "numberOfListeners": 102727,
              "city": "São Paulo",
              "country": "BR",
              "region": "SP"
            }
          ]
        }
      },
      "relatedContent": {
        "appearsOn": {
          "totalCount": 89,
          "items": [
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2qQf72CQ3j5D9AEwvmGvdX",
                    "id": "2qQf72CQ3j5D9AEwvmGvdX",
                    "name": "Sunrise",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:20gsENnposVs2I4rQ5kvrf",
                          "profile": {
                            "name": "Sam Feldt"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0201288d5dc8b701031d97a0d7",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485101288d5dc8b701031d97a0d7",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27301288d5dc8b701031d97a0d7",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2017
                    },
                    "sharingInfo": {
                      "shareId": "je76vA8nQcCFUhZAvvTO8A",
                      "shareUrl": "https://open.spotify.com/album/2qQf72CQ3j5D9AEwvmGvdX?si=je76vA8nQcCFUhZAvvTO8A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4QyylR4pPcWRpp3U2gkPcd",
                    "id": "4QyylR4pPcWRpp3U2gkPcd",
                    "name": "Sunrise To Sunset",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:20gsENnposVs2I4rQ5kvrf",
                          "profile": {
                            "name": "Sam Feldt"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0209345bdc4fa847fb5e5898cc",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485109345bdc4fa847fb5e5898cc",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27309345bdc4fa847fb5e5898cc",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2017
                    },
                    "sharingInfo": {
                      "shareId": "ShUnZDM_SFa0Qg5r5z98iw",
                      "shareUrl": "https://open.spotify.com/album/4QyylR4pPcWRpp3U2gkPcd?si=ShUnZDM_SFa0Qg5r5z98iw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:66cSCYHzE9eWbgtICJ7ceI",
                    "id": "66cSCYHzE9eWbgtICJ7ceI",
                    "name": "Annual 2021",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0NGAZxHanS9e0iNHpR8f2W",
                          "profile": {
                            "name": "Alok"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b495cce6a4628c518b67adc4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b495cce6a4628c518b67adc4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b495cce6a4628c518b67adc4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2021
                    },
                    "sharingInfo": {
                      "shareId": "XswzUkTCTfSZejTHpFpH3w",
                      "shareUrl": "https://open.spotify.com/album/66cSCYHzE9eWbgtICJ7ceI?si=XswzUkTCTfSZejTHpFpH3w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:209j2TtzIAQHRxoBgeoqUM",
                    "id": "209j2TtzIAQHRxoBgeoqUM",
                    "name": "Reloaded",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:14dmbYen0AciYxu5n4Fkpd",
                          "profile": {
                            "name": "DJ BoBo"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025e31e1be55fa05cc9651ce07",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515e31e1be55fa05cc9651ce07",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735e31e1be55fa05cc9651ce07",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2013
                    },
                    "sharingInfo": {
                      "shareId": "009PloveQmuEuUq0lcwxww",
                      "shareUrl": "https://open.spotify.com/album/209j2TtzIAQHRxoBgeoqUM?si=009PloveQmuEuUq0lcwxww"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:17nkMuRLEPUTt9xt3gQOgy",
                    "id": "17nkMuRLEPUTt9xt3gQOgy",
                    "name": "Antiexemplu",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1n5LD9Ar3D6RK2X2ewGvXb",
                          "profile": {
                            "name": "Carla's Dreams"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028cb919b4f26d3a0d663fd6a0",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518cb919b4f26d3a0d663fd6a0",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738cb919b4f26d3a0d663fd6a0",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2017
                    },
                    "sharingInfo": {
                      "shareId": "3bg1WepFQP24XWJmEL8Akw",
                      "shareUrl": "https://open.spotify.com/album/17nkMuRLEPUTt9xt3gQOgy?si=3bg1WepFQP24XWJmEL8Akw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 2,
                "items": [
                  {
                    "uri": "spotify:album:17B9ZB9opgRGcvN4Svc2si",
                    "id": "17B9ZB9opgRGcvN4Svc2si",
                    "name": "Never Dies",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022a4f7e877e5755965064961b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512a4f7e877e5755965064961b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732a4f7e877e5755965064961b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2020
                    },
                    "sharingInfo": {
                      "shareId": "VIxeBrtRReCWGSoXHsv9gw",
                      "shareUrl": "https://open.spotify.com/album/17B9ZB9opgRGcvN4Svc2si?si=VIxeBrtRReCWGSoXHsv9gw"
                    }
                  },
                  {
                    "uri": "spotify:album:68ImxwrLIWhRlb38KLjcfU",
                    "id": "68ImxwrLIWhRlb38KLjcfU",
                    "name": "Never Dies",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029c673f6c9e9d53a27dd10da9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519c673f6c9e9d53a27dd10da9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739c673f6c9e9d53a27dd10da9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2020
                    },
                    "sharingInfo": {
                      "shareId": "h_R9Sq6nS3KU81_k5foR6w",
                      "shareUrl": "https://open.spotify.com/album/68ImxwrLIWhRlb38KLjcfU?si=h_R9Sq6nS3KU81_k5foR6w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:77G3b0NefwZSiYhuSMGIpu",
                    "id": "77G3b0NefwZSiYhuSMGIpu",
                    "name": "Best Dance Hits Ever - Top 50",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b819c668dcc0b22c6fdef4d2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b819c668dcc0b22c6fdef4d2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b819c668dcc0b22c6fdef4d2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2018
                    },
                    "sharingInfo": {
                      "shareId": "Gv0YvJR_RA-PpCuGycBzaw",
                      "shareUrl": "https://open.spotify.com/album/77G3b0NefwZSiYhuSMGIpu?si=Gv0YvJR_RA-PpCuGycBzaw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2knRps90HKMGWoVRxgpvXJ",
                    "id": "2knRps90HKMGWoVRxgpvXJ",
                    "name": "My Gorgeous Drama Queens",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:05qpk4JDcLSFNJSsPIZ8Ye",
                          "profile": {
                            "name": "The Motans"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c577e39bde79b41129b7acea",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c577e39bde79b41129b7acea",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c577e39bde79b41129b7acea",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2018
                    },
                    "sharingInfo": {
                      "shareId": "W7oFZyzmQamnYNIUvTCTcw",
                      "shareUrl": "https://open.spotify.com/album/2knRps90HKMGWoVRxgpvXJ?si=W7oFZyzmQamnYNIUvTCTcw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3z7A1LFhxzmOGwTZtSWQ1D",
                    "id": "3z7A1LFhxzmOGwTZtSWQ1D",
                    "name": "Ngoc",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1n5LD9Ar3D6RK2X2ewGvXb",
                          "profile": {
                            "name": "Carla's Dreams"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02213d9424796690df42271d6b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851213d9424796690df42271d6b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273213d9424796690df42271d6b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2016
                    },
                    "sharingInfo": {
                      "shareId": "zlkcHMQTTlC0NrJwyz4A9A",
                      "shareUrl": "https://open.spotify.com/album/3z7A1LFhxzmOGwTZtSWQ1D?si=zlkcHMQTTlC0NrJwyz4A9A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0XgKWgSVOG0BLFvROk3AVg",
                    "id": "0XgKWgSVOG0BLFvROk3AVg",
                    "name": "DJ Central Groove Vol, 3",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02da120b23e980081c9354e3fb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851da120b23e980081c9354e3fb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273da120b23e980081c9354e3fb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2018
                    },
                    "sharingInfo": {
                      "shareId": "2Z9G800-RFCua73NxH39jw",
                      "shareUrl": "https://open.spotify.com/album/0XgKWgSVOG0BLFvROk3AVg?si=2Z9G800-RFCua73NxH39jw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6RoGYmxUOIzCDxK7P7P46H",
                    "id": "6RoGYmxUOIzCDxK7P7P46H",
                    "name": "Sober",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6tqRPlUavLUI398ZRw7M6e",
                          "profile": {
                            "name": "yeanix"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027c7c44dd3dacdeedd1f532df",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517c7c44dd3dacdeedd1f532df",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737c7c44dd3dacdeedd1f532df",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2022
                    },
                    "sharingInfo": {
                      "shareId": "bwJv1AVpSm28tBml89rzlA",
                      "shareUrl": "https://open.spotify.com/album/6RoGYmxUOIzCDxK7P7P46H?si=bwJv1AVpSm28tBml89rzlA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4SIpuXhPR2PhE2H1tU75QM",
                    "id": "4SIpuXhPR2PhE2H1tU75QM",
                    "name": "Supervara 2009",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a395a93d8a438e46e914caeb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a395a93d8a438e46e914caeb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a395a93d8a438e46e914caeb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2009
                    },
                    "sharingInfo": {
                      "shareId": "ew6AYj3vRgeClKLxGwwa1A",
                      "shareUrl": "https://open.spotify.com/album/4SIpuXhPR2PhE2H1tU75QM?si=ew6AYj3vRgeClKLxGwwa1A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 2,
                "items": [
                  {
                    "uri": "spotify:album:0Dufuv6lYFks1aX0GqXfk5",
                    "id": "0Dufuv6lYFks1aX0GqXfk5",
                    "name": "Mai Stai",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0niQ4Q9nI1Qh0BHpT3b4NC",
                          "profile": {
                            "name": "3 Sud Est"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0205a9ab49a99e1940242c4e0e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485105a9ab49a99e1940242c4e0e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27305a9ab49a99e1940242c4e0e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2015
                    },
                    "sharingInfo": {
                      "shareId": "-A9JheGKQiCB9w5jkGGpiw",
                      "shareUrl": "https://open.spotify.com/album/0Dufuv6lYFks1aX0GqXfk5?si=-A9JheGKQiCB9w5jkGGpiw"
                    }
                  },
                  {
                    "uri": "spotify:album:3X2yHumpEN6qHCOHgjr6x8",
                    "id": "3X2yHumpEN6qHCOHgjr6x8",
                    "name": "Mai stai",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0niQ4Q9nI1Qh0BHpT3b4NC",
                          "profile": {
                            "name": "3 Sud Est"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0247f1c72cfe9a3bddfbbc1453",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485147f1c72cfe9a3bddfbbc1453",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27347f1c72cfe9a3bddfbbc1453",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2015
                    },
                    "sharingInfo": {
                      "shareId": "eiHjFVTkT0CgRGbsx3OhOg",
                      "shareUrl": "https://open.spotify.com/album/3X2yHumpEN6qHCOHgjr6x8?si=eiHjFVTkT0CgRGbsx3OhOg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0qsCsajava06qxa5apReib",
                    "id": "0qsCsajava06qxa5apReib",
                    "name": "Reina Istanbul, Vol. 7",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:2K15nwVhvJnIsg6fcfGiSi",
                          "profile": {
                            "name": "Ufuk Akyıldız"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0248d542e04d87ea970ed6f65b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485148d542e04d87ea970ed6f65b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27348d542e04d87ea970ed6f65b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2015
                    },
                    "sharingInfo": {
                      "shareId": "qQnroNNcSruHqZQNg91YNw",
                      "shareUrl": "https://open.spotify.com/album/0qsCsajava06qxa5apReib?si=qQnroNNcSruHqZQNg91YNw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3pcIJIuMpyw7L2fxGETbzk",
                    "id": "3pcIJIuMpyw7L2fxGETbzk",
                    "name": "Baila Conmigo",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0224806be3b400cc478731bfbe",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485124806be3b400cc478731bfbe",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27324806be3b400cc478731bfbe",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2019
                    },
                    "sharingInfo": {
                      "shareId": "fxbmFlSZT-yksvIPTA_kug",
                      "shareUrl": "https://open.spotify.com/album/3pcIJIuMpyw7L2fxGETbzk?si=fxbmFlSZT-yksvIPTA_kug"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0URMeyN2XosmGKgsibzLuj",
                    "id": "0URMeyN2XosmGKgsibzLuj",
                    "name": "Party Anthems",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027fb0863939fd706bbd4b2494",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517fb0863939fd706bbd4b2494",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737fb0863939fd706bbd4b2494",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2021
                    },
                    "sharingInfo": {
                      "shareId": "KTHCqe8fSxqKuvMVtmlM2A",
                      "shareUrl": "https://open.spotify.com/album/0URMeyN2XosmGKgsibzLuj?si=KTHCqe8fSxqKuvMVtmlM2A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6dCJAD121RDSJ4xrTGewlA",
                    "id": "6dCJAD121RDSJ4xrTGewlA",
                    "name": "Supervara 2009",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c036c933aa73e5aaa7e88272",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c036c933aa73e5aaa7e88272",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c036c933aa73e5aaa7e88272",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2009
                    },
                    "sharingInfo": {
                      "shareId": "tuGlmK_tQwCbJ6vVc6Rg2w",
                      "shareUrl": "https://open.spotify.com/album/6dCJAD121RDSJ4xrTGewlA?si=tuGlmK_tQwCbJ6vVc6Rg2w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4KDupOYFdmHY0buIQ3w7o7",
                    "id": "4KDupOYFdmHY0buIQ3w7o7",
                    "name": "Home Workout Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0220fb03705b6651066b91e31f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485120fb03705b6651066b91e31f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27320fb03705b6651066b91e31f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2021
                    },
                    "sharingInfo": {
                      "shareId": "yVUzxRNdQVqmiAIWnl6dAw",
                      "shareUrl": "https://open.spotify.com/album/4KDupOYFdmHY0buIQ3w7o7?si=yVUzxRNdQVqmiAIWnl6dAw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4VgO2rhcyq3Un1gMkg9oJM",
                    "id": "4VgO2rhcyq3Un1gMkg9oJM",
                    "name": "Masquerade Club Istanbul",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:2c9zUiLbT2bm0DPsAbqLzt",
                          "profile": {
                            "name": "Cihat Ugurel"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0294e467b2d6c46d1f3dc41f43",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485194e467b2d6c46d1f3dc41f43",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27394e467b2d6c46d1f3dc41f43",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2018
                    },
                    "sharingInfo": {
                      "shareId": "EoYaSnn1T-SoMBNYqr_ahA",
                      "shareUrl": "https://open.spotify.com/album/4VgO2rhcyq3Un1gMkg9oJM?si=EoYaSnn1T-SoMBNYqr_ahA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:1Fzq2n9s3YHDajNdQOCOQS",
                    "id": "1Fzq2n9s3YHDajNdQOCOQS",
                    "name": "Can't Get You Out Of My Head Vol. 001",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0NGAZxHanS9e0iNHpR8f2W",
                          "profile": {
                            "name": "Alok"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b0600d2d2af8b00605e022cb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b0600d2d2af8b00605e022cb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b0600d2d2af8b00605e022cb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "date": {
                      "year": 2021
                    },
                    "sharingInfo": {
                      "shareId": "cGK21Rd1SYOAUDweHolQHg",
                      "shareUrl": "https://open.spotify.com/album/1Fzq2n9s3YHDajNdQOCOQS?si=cGK21Rd1SYOAUDweHolQHg"
                    }
                  }
                ]
              }
            }
          ]
        },
        "featuring": {
          "totalCount": 12,
          "items": [
            {
              "uri": "spotify:playlist:37i9dQZF1DZ06evO1ru5u8",
              "id": "37i9dQZF1DZ06evO1ru5u8",
              "owner": {
                "name": "Spotify"
              },
              "name": "This Is INNA",
              "description": "This is INNA. The essential tracks, all in one playlist.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://thisis-images.scdn.co/37i9dQZF1DZ06evO1ru5u8-default.jpg",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1E4zUNZhVINYCS",
              "id": "37i9dQZF1E4zUNZhVINYCS",
              "owner": {
                "name": "Spotify"
              },
              "name": "INNA Radio",
              "description": "",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://seeded-session-images.scdn.co/v1/img/artist/2w9zwq3AktTeYYMuhMjju8/en",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX5cc7vmfioLh",
              "id": "37i9dQZF1DX5cc7vmfioLh",
              "owner": {
                "name": "Spotify"
              },
              "name": "Yabancı Pop",
              "description": "Hit pop trendleri. Kapak: Taylor Swift x Ed Sheeran",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002f65970cda419a22790b45f14",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWXBcLLksEQAf",
              "id": "37i9dQZF1DWXBcLLksEQAf",
              "owner": {
                "name": "Spotify"
              },
              "name": "Pozitif",
              "description": "Good vibes only.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f0000000284d1ff2af2a9e1cbac76cacd",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX76Wlfdnj7AP",
              "id": "37i9dQZF1DX76Wlfdnj7AP",
              "owner": {
                "name": "Spotify"
              },
              "name": "Beast Mode",
              "description": "Get your beast mode on!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000029249b35f23fb596b6f006a15",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DXcRXFNfZr7Tp",
              "id": "37i9dQZF1DXcRXFNfZr7Tp",
              "owner": {
                "name": "Spotify"
              },
              "name": "just hits",
              "description": "Current favorites and exciting new music. Cover: Ed Sheeran",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002e548988f9c5c0aff5dc801eb",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX9p87xT0df0F",
              "id": "37i9dQZF1DX9p87xT0df0F",
              "owner": {
                "name": "Spotify"
              },
              "name": "LOOP",
              "description": "Döne döne dinlediğin, son yılların hit yabancı şarkıları.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002203768c88c741aa117804007",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWYBO1MoTDhZI",
              "id": "37i9dQZF1DWYBO1MoTDhZI",
              "owner": {
                "name": "Spotify"
              },
              "name": "Good Vibes",
              "description": "Set it off with these epic anthems. Only good vibes here!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000027dc2a0fb4bfe0d07294f685e",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWUxHPh2rEiHr",
              "id": "37i9dQZF1DWUxHPh2rEiHr",
              "owner": {
                "name": "Spotify"
              },
              "name": "Global X",
              "description": "The sound of a new era. Discover rhythmic crossover hits from cultures around the world! Cover: PEDRO SAMPAIO, Mc Pedrinho",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002bd043ad0ab6b55106e4e67dc",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DXcZDD7cfEKhW",
              "id": "37i9dQZF1DXcZDD7cfEKhW",
              "owner": {
                "name": "Spotify"
              },
              "name": "Pop Remix",
              "description": "Remixed pop and <a href=\"spotify:genre:edm_dance\">dance</a> collabs. Cover: Jennifer Lopez.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000029f7cc919b9a8287355eaa3e2",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX0AMssoUKCz7",
              "id": "37i9dQZF1DX0AMssoUKCz7",
              "owner": {
                "name": "Spotify"
              },
              "name": "Tropical House",
              "description": "Take down the tempo but keep the party going with the biggest tropical house jams.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002194e62197788bcbd737a07a2",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX8a1tdzq5tbM",
              "id": "37i9dQZF1DX8a1tdzq5tbM",
              "owner": {
                "name": "Spotify"
              },
              "name": "Dance Classics",
              "description": "<a href=\"spotify:genre:edm_dance\">Dance radio</a> hits from the 90s and 00s!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002377cd62f388e2de7c3b2b08c",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            }
          ]
        },
        "discoveredOn": {
          "totalCount": 91,
          "items": [
            {
              "uri": "spotify:playlist:37i9dQZF1DXcRXFNfZr7Tp",
              "id": "37i9dQZF1DXcRXFNfZr7Tp",
              "owner": {
                "name": "Spotify"
              },
              "name": "just hits",
              "description": "Current favorites and exciting new music. Cover: Ed Sheeran",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002e548988f9c5c0aff5dc801eb",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX12G1GAEuIuj",
              "id": "37i9dQZF1DX12G1GAEuIuj",
              "owner": {
                "name": "Spotify"
              },
              "name": "Главные хиты",
              "description": "Актуальные хиты в России прямо сейчас. На обложке: Tyga & Doja Cat",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002e96ad5e35471a288d0a97a81",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX76Wlfdnj7AP",
              "id": "37i9dQZF1DX76Wlfdnj7AP",
              "owner": {
                "name": "Spotify"
              },
              "name": "Beast Mode",
              "description": "Get your beast mode on!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000029249b35f23fb596b6f006a15",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWYBO1MoTDhZI",
              "id": "37i9dQZF1DWYBO1MoTDhZI",
              "owner": {
                "name": "Spotify"
              },
              "name": "Good Vibes",
              "description": "Set it off with these epic anthems. Only good vibes here!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000027dc2a0fb4bfe0d07294f685e",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DXaXB8fQg7xif",
              "id": "37i9dQZF1DXaXB8fQg7xif",
              "owner": {
                "name": "Spotify"
              },
              "name": "Dance Party",
              "description": "<a href=\"spotify:genre:edm_dance\">Move</a> your feet!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002707af5c8abb5c0b4ef0df2ed",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWZ5Se2LB1C5h",
              "id": "37i9dQZF1DWZ5Se2LB1C5h",
              "owner": {
                "name": "Spotify"
              },
              "name": "Euphoria EDM",
              "description": "Únete a la extravaganza del neón y la electrónica. Foto: Diplo",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002b0f9bc3c3b5ad0912a4cc003",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:4PjuQlhAehZD44vfNlpGP0",
              "id": "4PjuQlhAehZD44vfNlpGP0",
              "owner": {
                "name": "Original Music"
              },
              "name": "ELETRÔNICAS 2022 ⚡ MAIS TOCADAS",
              "description": "Ouça agora a Playlist Eletronica mais ATUALIZADA 2021-2022 | O Melhor do Eletrônico | As Mais Tocadas, como: Don&#x27;t Say Goodbye, Astronaut in The Ocean, The Business, Alive, Roses, Goosebumps, Paradise, Slow Down. Foto: Alok",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da8477d185fcc49a7928a7a3aa14",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX49bSMRljsho",
              "id": "37i9dQZF1DX49bSMRljsho",
              "owner": {
                "name": "Spotify"
              },
              "name": "Hot Hits Polska",
              "description": "50 najgorętszych hitów w Polsce. Cover: Sara James",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000021efc55a247cfb167af35f7ab",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWZUWZIwpqsT3",
              "id": "37i9dQZF1DWZUWZIwpqsT3",
              "owner": {
                "name": "Spotify"
              },
              "name": "This Is Alok",
              "description": "Press play and let's dance with the biggest Brazilian DJ!",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002dcc7a422002b9423dd021e85",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX12meDmp2yzx",
              "id": "37i9dQZF1DX12meDmp2yzx",
              "owner": {
                "name": "Spotify"
              },
              "name": "Hit Dancefloor",
              "description": "Największe taneczne hity w Polsce. Cover: bryska",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000022d1ef4a1478c94d8553ddce3",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DXcZDD7cfEKhW",
              "id": "37i9dQZF1DXcZDD7cfEKhW",
              "owner": {
                "name": "Spotify"
              },
              "name": "Pop Remix",
              "description": "Remixed pop and <a href=\"spotify:genre:edm_dance\">dance</a> collabs. Cover: Jennifer Lopez.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000029f7cc919b9a8287355eaa3e2",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX3NPSGp8NFZJ",
              "id": "37i9dQZF1DX3NPSGp8NFZJ",
              "owner": {
                "name": "Spotify"
              },
              "name": "Танцевальные хиты",
              "description": "Самая популярная танцевальная музыка в России прямо сейчас. На обложке: Kygo и DNCE",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002c55666a05bb4552744772562",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX70RN3TfWWJh",
              "id": "37i9dQZF1DX70RN3TfWWJh",
              "owner": {
                "name": "Spotify"
              },
              "name": "Workout",
              "description": "Pop hits to keep your workout fresh.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f000000029cc6891dbc9b7292361bd673",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:3RxJQGGhaS71GGUNuYEQns",
              "id": "3RxJQGGhaS71GGUNuYEQns",
              "owner": {
                "name": "hotamazingnetwork"
              },
              "name": "ELECTRONICA PARA FIESTAS 2022 🔥🌴☀️ EXITOS ",
              "description": "ELECTRONICA PARA FIESTAS 2022 🔥 EXITOS : VERANO 2022 MIX 🌴☀️  La Mejor Música Electrónica 2022 | ENGANCHADO FIESTA 2021 &amp; 2022 : MUSICA LOS MAS ESCUCHADOS : LA PLAYA : CHILL : LOUNGE : BRAZIL HITS : PORTUGAL : SPANISH HITS : DANCE MIX 2022 🌴Melhores Na Balada Jovem Pan 2022🌱Musicas Electronicas 🌱Alok",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da8493ae0fdd27043562613800cc",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DX6QbU3i33zqm",
              "id": "37i9dQZF1DX6QbU3i33zqm",
              "owner": {
                "name": "Spotify"
              },
              "name": "Electrónica Máxima",
              "description": "El mejor Dance.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f0000000210ad8781d37de7e07533835b",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWTWEW1zqSeEj",
              "id": "37i9dQZF1DWTWEW1zqSeEj",
              "owner": {
                "name": "Spotify"
              },
              "name": "Zurück in die 90er",
              "description": "Flashback in die Zeit von Eurodance und Gameboys: Das sind die 90er.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f0000000205930415850829e8cde41aeb",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DWUI9wBgUr4BH",
              "id": "37i9dQZF1DWUI9wBgUr4BH",
              "owner": {
                "name": "Spotify"
              },
              "name": "Futurs Hits",
              "description": "Les hits de demain sont déjà ici. Photo : Camila Cabello x Ed Sheeran",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706f00000002b0a401d218829aca47e0c29c",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:37i9dQZF1DZ06evO1ru5u8",
              "id": "37i9dQZF1DZ06evO1ru5u8",
              "owner": {
                "name": "Spotify"
              },
              "name": "This Is INNA",
              "description": "This is INNA. The essential tracks, all in one playlist.",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://thisis-images.scdn.co/37i9dQZF1DZ06evO1ru5u8-default.jpg",
                        "width": null,
                        "height": null
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:79rqB0JO0uWvJoMCotj41p",
              "id": "79rqB0JO0uWvJoMCotj41p",
              "owner": {
                "name": "Bigod Plays"
              },
              "name": "Alok 2022 🔥 Lançamentos |  As melhores",
              "description": "Ouça aqui os maiores hits do Alok, com Alive (It feels like) | Dont Say Goodbye | Party On My Own | Tu | Quando o grave bate forte | Piece of your heart | As melhores e mais tocadas da música eletrônica no momento | It Don&#x27;t Matter. Foto: DJ Alok",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84ecea4d6e7a1243a71440d420",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            },
            {
              "uri": "spotify:playlist:7mZZkjpyoY83wHbssEtzNF",
              "id": "7mZZkjpyoY83wHbssEtzNF",
              "owner": {
                "name": "LoudKult"
              },
              "name": "GYM MUSIC 2022🏋️ WORKOUT BEATS",
              "description": "Gym Motivation,Running Songs ,Motivation mix, Workout Music,Workout songs, Spinning Songs , Crossfit Mixtape.  Treino .  Gym Motivation - Treino",
              "images": {
                "totalCount": 1,
                "items": [
                  {
                    "sources": [
                      {
                        "url": "https://i.scdn.co/image/ab67706c0000da84f59dd568d149c4fd2eb814c0",
                        "width": 640,
                        "height": 640
                      }
                    ]
                  }
                ]
              }
            }
          ]
        },
        "relatedArtists": {
          "totalCount": 20,
          "items": [
            {
              "id": "6RQDTlies3nrNDJwXvbBZT",
              "uri": "spotify:artist:6RQDTlies3nrNDJwXvbBZT",
              "profile": {
                "name": "Otilia"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb0d6cf2887a3a062e07e473c2",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1780d6cf2887a3a062e07e473c2",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "57Pw3FSi1qi2fOY4wKOKjK",
              "uri": "spotify:artist:57Pw3FSi1qi2fOY4wKOKjK",
              "profile": {
                "name": "Akcent"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebe9b9fbdd998a20f9d3d28068",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178e9b9fbdd998a20f9d3d28068",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "0BmLNz4nSLfoWYW1cYsElL",
              "uri": "spotify:artist:0BmLNz4nSLfoWYW1cYsElL",
              "profile": {
                "name": "Alexandra Stan"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb07447480bbae1da5b3a2d014",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f17807447480bbae1da5b3a2d014",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "2b01rwtcqW5LyfVBMzIFQ4",
              "uri": "spotify:artist:2b01rwtcqW5LyfVBMzIFQ4",
              "profile": {
                "name": "Kate Linn"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebd7fc46d6b21a51bcb57e55eb",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178d7fc46d6b21a51bcb57e55eb",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "1oqThNqOfhev071PvmOwWQ",
              "uri": "spotify:artist:1oqThNqOfhev071PvmOwWQ",
              "profile": {
                "name": "DJ Project"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eba8f9dce9103e30a3f9a3d781",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178a8f9dce9103e30a3f9a3d781",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "0rDSGIC4lIxx1zc0eGJY42",
              "uri": "spotify:artist:0rDSGIC4lIxx1zc0eGJY42",
              "profile": {
                "name": "Dj Sava"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb2a928cbcd0adc5bdc3dc9eaf",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1782a928cbcd0adc5bdc3dc9eaf",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "1oiZoULxUJDYGOKMgVefP4",
              "uri": "spotify:artist:1oiZoULxUJDYGOKMgVefP4",
              "profile": {
                "name": "Morandi"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb2a7ed9042a0122efcc29cccc",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1782a7ed9042a0122efcc29cccc",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "2Rum2rwDio2My0Md24m3Oa",
              "uri": "spotify:artist:2Rum2rwDio2My0Md24m3Oa",
              "profile": {
                "name": "Fly Project"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebb82cdb8180bb919a8502046c",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178b82cdb8180bb919a8502046c",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "4TLzMoEaUDkcAfIlY3Xhxn",
              "uri": "spotify:artist:4TLzMoEaUDkcAfIlY3Xhxn",
              "profile": {
                "name": "Antonia"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebd42df33b004a1fbb03bd9620",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178d42df33b004a1fbb03bd9620",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "0TmLIfQje5MdX2ovu4yQKz",
              "uri": "spotify:artist:0TmLIfQje5MdX2ovu4yQKz",
              "profile": {
                "name": "Monoir"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb9892d1e00cda3efacd23afd0",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1789892d1e00cda3efacd23afd0",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "6XwwFnewNgWp81MYMK8zLq",
              "uri": "spotify:artist:6XwwFnewNgWp81MYMK8zLq",
              "profile": {
                "name": "Edward Maya"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebb20698cf6048254eea007587",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178b20698cf6048254eea007587",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "7hQmAXAzWI6D350VTgkKTG",
              "uri": "spotify:artist:7hQmAXAzWI6D350VTgkKTG",
              "profile": {
                "name": "Arash"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eba70ab4d7f3d5795603d2a4f8",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178a70ab4d7f3d5795603d2a4f8",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "3ZASW3RrHBbSRkNLjOrAFF",
              "uri": "spotify:artist:3ZASW3RrHBbSRkNLjOrAFF",
              "profile": {
                "name": "Sasha Lopez"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb5985f3c672438221b2d6d663",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1785985f3c672438221b2d6d663",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "4T8dF8zYAxgtlPPICuFQ5w",
              "uri": "spotify:artist:4T8dF8zYAxgtlPPICuFQ5w",
              "profile": {
                "name": "Pascal Junior"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb524369d15fb6006b3c61a9d8",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178524369d15fb6006b3c61a9d8",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "2rcsCDLsJw6erBukvjEsrP",
              "uri": "spotify:artist:2rcsCDLsJw6erBukvjEsrP",
              "profile": {
                "name": "Claydee"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb3270ef9055672c6138c7dbd5",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1783270ef9055672c6138c7dbd5",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "05qpk4JDcLSFNJSsPIZ8Ye",
              "uri": "spotify:artist:05qpk4JDcLSFNJSsPIZ8Ye",
              "profile": {
                "name": "The Motans"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebdbe3b95bf72c04d0669e0eb1",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178dbe3b95bf72c04d0669e0eb1",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "72FGvJgYbs0NBeJqECy6cF",
              "uri": "spotify:artist:72FGvJgYbs0NBeJqECy6cF",
              "profile": {
                "name": "Andra"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5ebc663ffd5c1034ccee2985aed",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f178c663ffd5c1034ccee2985aed",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "4oE7f7lNFkh0EbEZWEawBF",
              "uri": "spotify:artist:4oE7f7lNFkh0EbEZWEawBF",
              "profile": {
                "name": "SICKOTOY"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb69be3df5d247c29d7e90283a",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f17869be3df5d247c29d7e90283a",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "5v7efr4mqt3RQxkT0Mmh5g",
              "uri": "spotify:artist:5v7efr4mqt3RQxkT0Mmh5g",
              "profile": {
                "name": "Faydee"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb5ddbc60af905a570589a2a1d",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1785ddbc60af905a570589a2a1d",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            },
            {
              "id": "5T0j6On1EthT2QVNXh8vqc",
              "uri": "spotify:artist:5T0j6On1EthT2QVNXh8vqc",
              "profile": {
                "name": "Minelli"
              },
              "visuals": {
                "avatarImage": {
                  "sources": [
                    {
                      "url": "https://i.scdn.co/image/ab6761610000e5eb4d6f226b185b33b6a0cc3038",
                      "width": 640,
                      "height": 640
                    },
                    {
                      "url": "https://i.scdn.co/image/ab6761610000f1784d6f226b185b33b6a0cc3038",
                      "width": 160,
                      "height": 160
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      "goods": {
        "events": {
          "userLocation": {
            "name": null
          },
          "concerts": {
            "totalCount": 1,
            "items": [
              {
                "uri": "spotify:concert:4IWU2EQ1ZxAnvNIJEEOpug",
                "id": "4IWU2EQ1ZxAnvNIJEEOpug",
                "title": "Love The Tuentis 2022",
                "category": "FESTIVAL",
                "festival": true,
                "nearUser": false,
                "venue": {
                  "name": "IFEMA Feria de Madrid",
                  "location": {
                    "name": "Madrid"
                  },
                  "coordinates": {
                    "latitude": 40.46423,
                    "longitude": -3.61311
                  }
                },
                "artists": {
                  "items": [
                    {
                      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
                      "id": "2w9zwq3AktTeYYMuhMjju8",
                      "profile": {
                        "name": "INNA"
                      }
                    },
                    {
                      "uri": "spotify:artist:47BNWfpngeFHYvBlPPyraM",
                      "id": "47BNWfpngeFHYvBlPPyraM",
                      "profile": {
                        "name": "Kate Ryan"
                      }
                    },
                    {
                      "uri": "spotify:artist:0j8QSBQZ9MNSGjHr1Vll1R",
                      "id": "0j8QSBQZ9MNSGjHr1Vll1R",
                      "profile": {
                        "name": "Natalia Jiménez"
                      }
                    },
                    {
                      "uri": "spotify:artist:21ttsUKZ3y2Hm6nduyvbAw",
                      "id": "21ttsUKZ3y2Hm6nduyvbAw",
                      "profile": {
                        "name": "Pignoise"
                      }
                    },
                    {
                      "uri": "spotify:artist:6Zd2JZF0kIBpeyv2FlPh8i",
                      "id": "6Zd2JZF0kIBpeyv2FlPh8i",
                      "profile": {
                        "name": "Huecco"
                      }
                    },
                    {
                      "uri": "spotify:artist:2vAu3qMgOvtukijgajuXhM",
                      "id": "2vAu3qMgOvtukijgajuXhM",
                      "profile": {
                        "name": "King Africa"
                      }
                    },
                    {
                      "uri": "spotify:artist:1VfKauu6JYTUrApbJXU0zo",
                      "id": "1VfKauu6JYTUrApbJXU0zo",
                      "profile": {
                        "name": "Bustamante"
                      }
                    },
                    {
                      "uri": "spotify:artist:1i9NxPRrKcoW34XTMnvzJy",
                      "id": "1i9NxPRrKcoW34XTMnvzJy",
                      "profile": {
                        "name": "Sylver"
                      }
                    },
                    {
                      "uri": "spotify:artist:0HXSR2BeI0nXqc6Nlr65eq",
                      "id": "0HXSR2BeI0nXqc6Nlr65eq",
                      "profile": {
                        "name": "David Tavaré"
                      }
                    },
                    {
                      "uri": "spotify:artist:57QfQOhi7oyPiscoWfUSeC",
                      "id": "57QfQOhi7oyPiscoWfUSeC",
                      "profile": {
                        "name": "Jan Wayne"
                      }
                    }
                  ]
                },
                "partnerLinks": {
                  "items": [
                    {
                      "partnerName": "Songkick",
                      "url": "https://www.songkick.com/festivals/2247139-love-the-tuentis/id/39285551-love-the-tuentis-2022?utm_source=8123&utm_medium=partner&utm_content=&utm_campaign=artist"
                    }
                  ]
                },
                "date": {
                  "year": 2022,
                  "month": 6,
                  "day": 25,
                  "hour": 16,
                  "minute": 0,
                  "second": 0,
                  "isoString": "2022-06-25T16:00+02:00",
                  "precision": "MINUTE"
                }
              }
            ],
            "pagingInfo": {
              "limit": 4
            }
          }
        },
        "merch": {
          "items": [
            {
              "uri": "2206495",
              "description": "This is a new, unopened CD in its original packaging. Original Release Date: 2018-09-26 UPC: 4988002763795 Weight: 0.18 lb Dimensions: 4.9\" x 5.6\" x 0.4\"",
              "imageUri": "https://merch-img.scdn.co/https%3A%2F%2Fmerchbar.imgix.net%2Fproduct%2F4%2F1616%2F36719716%2F4988002763795.jpg%3Fblend64%3DaHR0cHM6Ly9tZXJjaGJhci5pbWdpeC5uZXQvfnRleHQ_dHh0LWZvbnQ9c2Fucy1zZXJpZi1ib2xkJnR4dC1jb2xvcj1mZmYmdHh0LXNpemU9NjQmdHh0LXBhZD0xNiZ3PTMyMCZiZz1mNzMxMTkmZHByPTImdHh0LWFsaWduPW1pZGRsZSUyQ2NlbnRlciZ0eHQ2ND1UMDRnVTBGTVJRJTNEJTNE%26blend-mode%3Dnormal%26blend-align%3Dbottom%2Cleft%26dpr%3D2%26blend-w%3D0.25%26w%3D640%26h%3D640?h=300&w=300&s=ab3059374f56364e5ee9d78b002c023d",
              "name": "NIRVANA CD",
              "url": "https://www.merchbar.com/vinyl-records/inna/inna-nirvana-cd-2206495?utm_source=merchbar-spotify&utm_medium=affiliate&mb-listing-id=2206495v2028"
            }
          ]
        }
      }
    }
  }
}
```



## Artist Discography

Retrieves an artist's complete discography including albums, singles, and other releases.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/artist_discography_overview/?id=2w9zwq3AktTeYYMuhMjju8", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "data": {
    "artist": {
      "id": "2w9zwq3AktTeYYMuhMjju8",
      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
      "profile": {
        "name": "INNA"
      },
      "discography": {
        "albums": {
          "totalCount": 11
        },
        "singles": {
          "totalCount": 166
        },
        "compilations": {
          "totalCount": 0
        }
      }
    }
  }
}
```




## Artist Singles

Retrieves an artist's singles and EPs.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/artist_singles/?id=2w9zwq3AktTeYYMuhMjju8&offset=0&limit=20", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "data": {
    "artist": {
      "discography": {
        "singles": {
          "totalCount": 166,
          "items": [
            {
              "releases": {
                "items": [
                  {
                    "id": "49D6ut4LdJCBD90wRWzfe6",
                    "uri": "spotify:album:49D6ut4LdJCBD90wRWzfe6",
                    "name": "Lalele",
                    "type": "SINGLE",
                    "date": {
                      "year": 2022,
                      "isoString": "2022-01-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021f43d9d7588ec1c832b8f2dc",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511f43d9d7588ec1c832b8f2dc",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731f43d9d7588ec1c832b8f2dc",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "S9SCNRzATAiKCZRwuuSCIA",
                      "shareUrl": "https://open.spotify.com/album/49D6ut4LdJCBD90wRWzfe6?si=S9SCNRzATAiKCZRwuuSCIA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2jA1exLaHCcpHtDrGLKTmy",
                    "uri": "spotify:album:2jA1exLaHCcpHtDrGLKTmy",
                    "name": "UP",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-12-17T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027bd254131ac1f8678448d076",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517bd254131ac1f8678448d076",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737bd254131ac1f8678448d076",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "ynQZ-UBPRM-qS5QOQQic8w",
                      "shareUrl": "https://open.spotify.com/album/2jA1exLaHCcpHtDrGLKTmy?si=ynQZ-UBPRM-qS5QOQQic8w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6uvP8hlbI9X3RleKNVmBzT",
                    "uri": "spotify:album:6uvP8hlbI9X3RleKNVmBzT",
                    "name": "UP (Robert Cristian Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-12-03T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021271f5f16702f3516f86579d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511271f5f16702f3516f86579d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731271f5f16702f3516f86579d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "h2XpE3slT9qxTFCvxZ2rYQ",
                      "shareUrl": "https://open.spotify.com/album/6uvP8hlbI9X3RleKNVmBzT?si=h2XpE3slT9qxTFCvxZ2rYQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5kjggiiZEcRzFvQ4rowAsQ",
                    "uri": "spotify:album:5kjggiiZEcRzFvQ4rowAsQ",
                    "name": "De Dragul Tău",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-11-26T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02da7c4e91509943b3c7cf8ef4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851da7c4e91509943b3c7cf8ef4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273da7c4e91509943b3c7cf8ef4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "-Ww2uxo7TEO99CCeO9u2ug",
                      "shareUrl": "https://open.spotify.com/album/5kjggiiZEcRzFvQ4rowAsQ?si=-Ww2uxo7TEO99CCeO9u2ug"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "21x0bCve7UJ7ZAapjt8GFz",
                    "uri": "spotify:album:21x0bCve7UJ7ZAapjt8GFz",
                    "name": "UP",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-29T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0265f27da14d572556a8a59755",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485165f27da14d572556a8a59755",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27365f27da14d572556a8a59755",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "JZBWu--GT3uTtUwNbHEz9g",
                      "shareUrl": "https://open.spotify.com/album/21x0bCve7UJ7ZAapjt8GFz?si=JZBWu--GT3uTtUwNbHEz9g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3wBRVC1SMfIEdsr9thFSYJ",
                    "uri": "spotify:album:3wBRVC1SMfIEdsr9thFSYJ",
                    "name": "UP (Vadim Adamov & Hardphol Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0200296e006391b562e8c70563",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485100296e006391b562e8c70563",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27300296e006391b562e8c70563",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "vVHQi-heSRGOWJ3PR1qG4Q",
                      "shareUrl": "https://open.spotify.com/album/3wBRVC1SMfIEdsr9thFSYJ?si=vVHQi-heSRGOWJ3PR1qG4Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "605jn7Lsj6RD4ovYCsnrxe",
                    "uri": "spotify:album:605jn7Lsj6RD4ovYCsnrxe",
                    "name": "UP (Mert Hakan & Onur Betin Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023a3334b5c3ac49b938312f03",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513a3334b5c3ac49b938312f03",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733a3334b5c3ac49b938312f03",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Jbv2x-1MTC6V5U49XXXO7Q",
                      "shareUrl": "https://open.spotify.com/album/605jn7Lsj6RD4ovYCsnrxe?si=Jbv2x-1MTC6V5U49XXXO7Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3QJqG1fLaNGsgjVUroIPCT",
                    "uri": "spotify:album:3QJqG1fLaNGsgjVUroIPCT",
                    "name": "UP (Filatov & Karas Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02d73086d4cbe065734d124185",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851d73086d4cbe065734d124185",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273d73086d4cbe065734d124185",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "UpRnjWP7RIyF1L9Urh9VVA",
                      "shareUrl": "https://open.spotify.com/album/3QJqG1fLaNGsgjVUroIPCT?si=UpRnjWP7RIyF1L9Urh9VVA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "57NJ9mlC0mPtXJAc6T9Q2g",
                    "uri": "spotify:album:57NJ9mlC0mPtXJAc6T9Q2g",
                    "name": "UP (Bzars Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0237f1c2da634da62a84370a09",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485137f1c2da634da62a84370a09",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27337f1c2da634da62a84370a09",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "gibMG_n2TL6x5FXbkvHp3Q",
                      "shareUrl": "https://open.spotify.com/album/57NJ9mlC0mPtXJAc6T9Q2g?si=gibMG_n2TL6x5FXbkvHp3Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "53kblUkYfsJ5bYAb3yDO0s",
                    "uri": "spotify:album:53kblUkYfsJ5bYAb3yDO0s",
                    "name": "UP (Barlas & Mert Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022af676a3bccbfe4a9cf0408d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512af676a3bccbfe4a9cf0408d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732af676a3bccbfe4a9cf0408d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "46bK1BPZSlWLKWY6YEWR6g",
                      "shareUrl": "https://open.spotify.com/album/53kblUkYfsJ5bYAb3yDO0s?si=46bK1BPZSlWLKWY6YEWR6g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7uAgbC70TWlSaIs8SzmDwU",
                    "uri": "spotify:album:7uAgbC70TWlSaIs8SzmDwU",
                    "name": "UP",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a20f608f337d3e30f5a2e665",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a20f608f337d3e30f5a2e665",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a20f608f337d3e30f5a2e665",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "RNSUOgW_TDmcLVu0A8yFeg",
                      "shareUrl": "https://open.spotify.com/album/7uAgbC70TWlSaIs8SzmDwU?si=RNSUOgW_TDmcLVu0A8yFeg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "46s4mpLHOEpUAcejvR7IpA",
                    "uri": "spotify:album:46s4mpLHOEpUAcejvR7IpA",
                    "name": "UP (Casian Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-10-25T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027286abd5a5eeb280ab512719",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517286abd5a5eeb280ab512719",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737286abd5a5eeb280ab512719",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "aL9lclw6SnmBB_8VCLGm7A",
                      "shareUrl": "https://open.spotify.com/album/46s4mpLHOEpUAcejvR7IpA?si=aL9lclw6SnmBB_8VCLGm7A"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "68t5XuKtgGbDZAr0SYylJg",
                    "uri": "spotify:album:68t5XuKtgGbDZAr0SYylJg",
                    "name": "Like That",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-09-30T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e026254d49df8517a5b5cab9505",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048516254d49df8517a5b5cab9505",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2736254d49df8517a5b5cab9505",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "rVzefqMbRh2T6z1WIn4tWw",
                      "shareUrl": "https://open.spotify.com/album/68t5XuKtgGbDZAr0SYylJg?si=rVzefqMbRh2T6z1WIn4tWw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5sy58Xl79PCDw6aFTzMXTs",
                    "uri": "spotify:album:5sy58Xl79PCDw6aFTzMXTs",
                    "name": "Pretty Please",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-09-24T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c380928f605c4d4a85909040",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c380928f605c4d4a85909040",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c380928f605c4d4a85909040",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "O2gyJp4fSuCo-FlQY--0OQ",
                      "shareUrl": "https://open.spotify.com/album/5sy58Xl79PCDw6aFTzMXTs?si=O2gyJp4fSuCo-FlQY--0OQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1HJj1jSYQlHcIeeOgJVjx0",
                    "uri": "spotify:album:1HJj1jSYQlHcIeeOgJVjx0",
                    "name": "Party",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-09-22T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ba6a65a07d32d3e214af76cc",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ba6a65a07d32d3e214af76cc",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ba6a65a07d32d3e214af76cc",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "668Ncd9XQdOLRaodGfit8Q",
                      "shareUrl": "https://open.spotify.com/album/1HJj1jSYQlHcIeeOgJVjx0?si=668Ncd9XQdOLRaodGfit8Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1kAnhTZUVAXIgmspTcSxqj",
                    "uri": "spotify:album:1kAnhTZUVAXIgmspTcSxqj",
                    "name": "Aici",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-08-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ef6451a062a530d3d2fbf778",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ef6451a062a530d3d2fbf778",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ef6451a062a530d3d2fbf778",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "iMBWku8cRCivKPc2Ahj_Iw",
                      "shareUrl": "https://open.spotify.com/album/1kAnhTZUVAXIgmspTcSxqj?si=iMBWku8cRCivKPc2Ahj_Iw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0fprmuiWAU7cCx64jG58HI",
                    "uri": "spotify:album:0fprmuiWAU7cCx64jG58HI",
                    "name": "Papa",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-07-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024cf5144feb940b6e5ddcf24f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514cf5144feb940b6e5ddcf24f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734cf5144feb940b6e5ddcf24f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "__9MwBsRQXup9IjhUZMmLA",
                      "shareUrl": "https://open.spotify.com/album/0fprmuiWAU7cCx64jG58HI?si=__9MwBsRQXup9IjhUZMmLA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0kCQJStitU54MYB12k7HZU",
                    "uri": "spotify:album:0kCQJStitU54MYB12k7HZU",
                    "name": "Hot (Sound Rush Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-07-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021ba87102ad18c0e87ef56ff8",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511ba87102ad18c0e87ef56ff8",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731ba87102ad18c0e87ef56ff8",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Id0mdISERLa8oFMPHlDSew",
                      "shareUrl": "https://open.spotify.com/album/0kCQJStitU54MYB12k7HZU?si=Id0mdISERLa8oFMPHlDSew"
                    },
                    "tracks": {
                      "totalCount": 2
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1G0XxPLeIcJZzAUILhiOA2",
                    "uri": "spotify:album:1G0XxPLeIcJZzAUILhiOA2",
                    "name": "Summer's Not Ready",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-29T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029d3cdfa53acb7f47ffa753b7",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519d3cdfa53acb7f47ffa753b7",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739d3cdfa53acb7f47ffa753b7",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "INhP4aUvQxyjyHNC4JrhRQ",
                      "shareUrl": "https://open.spotify.com/album/1G0XxPLeIcJZzAUILhiOA2?si=INhP4aUvQxyjyHNC4JrhRQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4z8dKsFCqFSUblEvwyIMh6",
                    "uri": "spotify:album:4z8dKsFCqFSUblEvwyIMh6",
                    "name": "Paris to London",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-25T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0202bbe85b5146f9f18501697c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485102bbe85b5146f9f18501697c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27302bbe85b5146f9f18501697c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "EuAnsn0gTAKBa0QkHSGJuQ",
                      "shareUrl": "https://open.spotify.com/album/4z8dKsFCqFSUblEvwyIMh6?si=EuAnsn0gTAKBa0QkHSGJuQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1Dn758WZneVZvqazEK18Zs",
                    "uri": "spotify:album:1Dn758WZneVZvqazEK18Zs",
                    "name": "Maza",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-11T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027e2fae88294459e096acaf97",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517e2fae88294459e096acaf97",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737e2fae88294459e096acaf97",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "eRrmkjFcQq-wNi-jfZSA8A",
                      "shareUrl": "https://open.spotify.com/album/1Dn758WZneVZvqazEK18Zs?si=eRrmkjFcQq-wNi-jfZSA8A"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6WYUXLCkqa2HT8Ble2RPnl",
                    "uri": "spotify:album:6WYUXLCkqa2HT8Ble2RPnl",
                    "name": "Maza (Robert Cristian Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a8a03cf25e11aa040ff38dbb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a8a03cf25e11aa040ff38dbb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a8a03cf25e11aa040ff38dbb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "qSxo-cBSQpmSsx9DdKwsTQ",
                      "shareUrl": "https://open.spotify.com/album/6WYUXLCkqa2HT8Ble2RPnl?si=qSxo-cBSQpmSsx9DdKwsTQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3URxAZFfZ4rLYMb0goZJNu",
                    "uri": "spotify:album:3URxAZFfZ4rLYMb0goZJNu",
                    "name": "Maza (French Version)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02176fc17fff8a6b468e869eb8",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851176fc17fff8a6b468e869eb8",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273176fc17fff8a6b468e869eb8",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "OeoYQzC8TE2-Z3ALsE-jDQ",
                      "shareUrl": "https://open.spotify.com/album/3URxAZFfZ4rLYMb0goZJNu?si=OeoYQzC8TE2-Z3ALsE-jDQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "56IMULK7a9IkAkgQE9sNrg",
                    "uri": "spotify:album:56IMULK7a9IkAkgQE9sNrg",
                    "name": "Maza (US Version)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-05-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022861cc9d95544297e9ded4a9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512861cc9d95544297e9ded4a9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732861cc9d95544297e9ded4a9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "o0m_C5_nQOmA8bcbHtG72Q",
                      "shareUrl": "https://open.spotify.com/album/56IMULK7a9IkAkgQE9sNrg?si=o0m_C5_nQOmA8bcbHtG72Q"
                    },
                    "tracks": {
                      "totalCount": 3
                    }
                  },
                  {
                    "id": "4p7iyW0drxwDXiMOWdLac8",
                    "uri": "spotify:album:4p7iyW0drxwDXiMOWdLac8",
                    "name": "Maza (US Version)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-06-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c8549cd6223d23367e720e36",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c8549cd6223d23367e720e36",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c8549cd6223d23367e720e36",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "tEacv5HzQauoSLtbQ1mpUA",
                      "shareUrl": "https://open.spotify.com/album/4p7iyW0drxwDXiMOWdLac8?si=tEacv5HzQauoSLtbQ1mpUA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7dmob5pZ4DyfhIPdOW2aWG",
                    "uri": "spotify:album:7dmob5pZ4DyfhIPdOW2aWG",
                    "name": "Maza (Ilkan Günüç Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-05-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0204514813b862e550444e930d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485104514813b862e550444e930d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27304514813b862e550444e930d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "lDj7bK8bQMqaiW3dTY1fiA",
                      "shareUrl": "https://open.spotify.com/album/7dmob5pZ4DyfhIPdOW2aWG?si=lDj7bK8bQMqaiW3dTY1fiA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4hCmUF3sTmagOYzrRrVCHj",
                    "uri": "spotify:album:4hCmUF3sTmagOYzrRrVCHj",
                    "name": "Maza (Casian Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-05-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028fe33d92ca0fefd23bafbe16",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518fe33d92ca0fefd23bafbe16",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738fe33d92ca0fefd23bafbe16",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "ww_xLAGpTWCD2c_N8P1rSg",
                      "shareUrl": "https://open.spotify.com/album/4hCmUF3sTmagOYzrRrVCHj?si=ww_xLAGpTWCD2c_N8P1rSg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5w5UPTvxo2vjCWnP5fbEnc",
                    "uri": "spotify:album:5w5UPTvxo2vjCWnP5fbEnc",
                    "name": "It Don’t Matter - Spotify Singles",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-05-07T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0260b16fc0b0cc5948f2173511",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485160b16fc0b0cc5948f2173511",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27360b16fc0b0cc5948f2173511",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "z81155oASw6QZeX1QTmHuw",
                      "shareUrl": "https://open.spotify.com/album/5w5UPTvxo2vjCWnP5fbEnc?si=z81155oASw6QZeX1QTmHuw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6cHNuGBDX0h3Pf88quyymV",
                    "uri": "spotify:album:6cHNuGBDX0h3Pf88quyymV",
                    "name": "It Don’t Matter (Ekanta Jake Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-05-06T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02264573ea95bea5bb05dad9f4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851264573ea95bea5bb05dad9f4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273264573ea95bea5bb05dad9f4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "ZaZEAgmuRR-Jwp1TjRevNw",
                      "shareUrl": "https://open.spotify.com/album/6cHNuGBDX0h3Pf88quyymV?si=ZaZEAgmuRR-Jwp1TjRevNw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1ieuMbqWl9HW9PUuMLchfi",
                    "uri": "spotify:album:1ieuMbqWl9HW9PUuMLchfi",
                    "name": "Oh My God",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-29T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025320b79cf9b66a3831d31b4d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515320b79cf9b66a3831d31b4d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735320b79cf9b66a3831d31b4d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "tZ5TatrjQz2ZVnVVds8xpw",
                      "shareUrl": "https://open.spotify.com/album/1ieuMbqWl9HW9PUuMLchfi?si=tZ5TatrjQz2ZVnVVds8xpw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1uEwqEReGhPtpvSiScNnne",
                    "uri": "spotify:album:1uEwqEReGhPtpvSiScNnne",
                    "name": "Oh My God (Modern Clvb Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e5c211f9b7f3142b1bcea6a7",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e5c211f9b7f3142b1bcea6a7",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e5c211f9b7f3142b1bcea6a7",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "_-pkA5pHSA6Jw8VhmVym7w",
                      "shareUrl": "https://open.spotify.com/album/1uEwqEReGhPtpvSiScNnne?si=_-pkA5pHSA6Jw8VhmVym7w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3ZNhk2Hi8XrJqopTvccNxu",
                    "uri": "spotify:album:3ZNhk2Hi8XrJqopTvccNxu",
                    "name": "Oh My God (Malik Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02059d7816e0b9ccf7e52f0286",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851059d7816e0b9ccf7e52f0286",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273059d7816e0b9ccf7e52f0286",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "U0_nUAlrT9iqwZ8dWhz0hw",
                      "shareUrl": "https://open.spotify.com/album/3ZNhk2Hi8XrJqopTvccNxu?si=U0_nUAlrT9iqwZ8dWhz0hw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6R0m2DwJEdJhr7SD0DnF2M",
                    "uri": "spotify:album:6R0m2DwJEdJhr7SD0DnF2M",
                    "name": "Oh My God (Kean Dysso Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021bb377640e905ced6108159d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511bb377640e905ced6108159d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731bb377640e905ced6108159d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "7YNf30GOQhOjSsCK2aMrxA",
                      "shareUrl": "https://open.spotify.com/album/6R0m2DwJEdJhr7SD0DnF2M?si=7YNf30GOQhOjSsCK2aMrxA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4OCtCoDnUhXDRLejqZ1nIG",
                    "uri": "spotify:album:4OCtCoDnUhXDRLejqZ1nIG",
                    "name": "Oh My God (DJ Tuncay Albayrak Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022c0820ca8a24c4fecf5f626c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512c0820ca8a24c4fecf5f626c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732c0820ca8a24c4fecf5f626c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "pKBfVUAURD2ntZh6AHcKQw",
                      "shareUrl": "https://open.spotify.com/album/4OCtCoDnUhXDRLejqZ1nIG?si=pKBfVUAURD2ntZh6AHcKQw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3Ah4WxYwvaCtjYi5mBOGIT",
                    "uri": "spotify:album:3Ah4WxYwvaCtjYi5mBOGIT",
                    "name": "Oh My God (Cosmo & Skoro Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02dd4a2ad63d89e8082ca6c4f2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851dd4a2ad63d89e8082ca6c4f2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273dd4a2ad63d89e8082ca6c4f2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "X-7WxxkGQnmeeZSKAB6Bcw",
                      "shareUrl": "https://open.spotify.com/album/3Ah4WxYwvaCtjYi5mBOGIT?si=X-7WxxkGQnmeeZSKAB6Bcw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7ygx7VMBScPeuQ7Zro3FKZ",
                    "uri": "spotify:album:7ygx7VMBScPeuQ7Zro3FKZ",
                    "name": "Cool Me Down",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028cb894fb74049c50127813a9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518cb894fb74049c50127813a9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738cb894fb74049c50127813a9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "cIIuqQgeQkeR1IxZBiM_XQ",
                      "shareUrl": "https://open.spotify.com/album/7ygx7VMBScPeuQ7Zro3FKZ?si=cIIuqQgeQkeR1IxZBiM_XQ"
                    },
                    "tracks": {
                      "totalCount": 2
                    }
                  },
                  {
                    "id": "1JmUG07HKI0ZOgyaUDYWXl",
                    "uri": "spotify:album:1JmUG07HKI0ZOgyaUDYWXl",
                    "name": "Cool Me Down",
                    "type": "SINGLE",
                    "date": {
                      "year": 2021,
                      "isoString": "2021-04-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02bcd63886aa45a6e167f4f5c6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851bcd63886aa45a6e167f4f5c6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273bcd63886aa45a6e167f4f5c6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "OuyHje_7TcqhLh0g75KX1g",
                      "shareUrl": "https://open.spotify.com/album/1JmUG07HKI0ZOgyaUDYWXl?si=OuyHje_7TcqhLh0g75KX1g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5oPp0EN7cEF9CqkWSgaXgy",
                    "uri": "spotify:album:5oPp0EN7cEF9CqkWSgaXgy",
                    "name": "You and I",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024f6a1d2c259a78f5420fbc91",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514f6a1d2c259a78f5420fbc91",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734f6a1d2c259a78f5420fbc91",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "LyPdEAdNTZu0xDFwxt2zDQ",
                      "shareUrl": "https://open.spotify.com/album/5oPp0EN7cEF9CqkWSgaXgy?si=LyPdEAdNTZu0xDFwxt2zDQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1jX4SAgxVO4iQPfkbLIAQ4",
                    "uri": "spotify:album:1jX4SAgxVO4iQPfkbLIAQ4",
                    "name": "Till Forever",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0262d99820075a1a12dcd27b56",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485162d99820075a1a12dcd27b56",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27362d99820075a1a12dcd27b56",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "ZmBNNibNQMmZ5tFHeNQMhQ",
                      "shareUrl": "https://open.spotify.com/album/1jX4SAgxVO4iQPfkbLIAQ4?si=ZmBNNibNQMmZ5tFHeNQMhQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5WdPNBvuCXVPxCIZe1Y6Al",
                    "uri": "spotify:album:5WdPNBvuCXVPxCIZe1Y6Al",
                    "name": "Thicky",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0212718cfb8419859a5784cd6e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485112718cfb8419859a5784cd6e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27312718cfb8419859a5784cd6e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "75bQAGykQGmpYmC2mWiFdg",
                      "shareUrl": "https://open.spotify.com/album/5WdPNBvuCXVPxCIZe1Y6Al?si=75bQAGykQGmpYmC2mWiFdg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3KGzVyVMyXW4kICozPsIoT",
                    "uri": "spotify:album:3KGzVyVMyXW4kICozPsIoT",
                    "name": "Sunset Dinner",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0287bf6955d7e8e9dee358ff5c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485187bf6955d7e8e9dee358ff5c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27387bf6955d7e8e9dee358ff5c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "pNBeeoMWRSqHR91IDN0fBA",
                      "shareUrl": "https://open.spotify.com/album/3KGzVyVMyXW4kICozPsIoT?si=pNBeeoMWRSqHR91IDN0fBA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "43uvYG2S8XEZz88nHYduIm",
                    "uri": "spotify:album:43uvYG2S8XEZz88nHYduIm",
                    "name": "One Reason",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0230a6633acf3934de8eac28c2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485130a6633acf3934de8eac28c2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27330a6633acf3934de8eac28c2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "IA21W1fpTkKrORkhwRa4cA",
                      "shareUrl": "https://open.spotify.com/album/43uvYG2S8XEZz88nHYduIm?si=IA21W1fpTkKrORkhwRa4cA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7JSIWQseOBW63TOHaSgUlG",
                    "uri": "spotify:album:7JSIWQseOBW63TOHaSgUlG",
                    "name": "Maza Jaja",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022fb02b68ded90c2a6ca543a6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512fb02b68ded90c2a6ca543a6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732fb02b68ded90c2a6ca543a6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "21Z7EY50SB-shBRYL3cXQQ",
                      "shareUrl": "https://open.spotify.com/album/7JSIWQseOBW63TOHaSgUlG?si=21Z7EY50SB-shBRYL3cXQQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6Z2qcCOpbbuYlRQ9l41f44",
                    "uri": "spotify:album:6Z2qcCOpbbuYlRQ9l41f44",
                    "name": "Heartbreaker",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02680249bd3c8b35e6e499c875",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851680249bd3c8b35e6e499c875",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273680249bd3c8b35e6e499c875",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "UM9X_aAiRJKQrVDearFnsQ",
                      "shareUrl": "https://open.spotify.com/album/6Z2qcCOpbbuYlRQ9l41f44?si=UM9X_aAiRJKQrVDearFnsQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7d5H1Jur1Wn816sI8slGtr",
                    "uri": "spotify:album:7d5H1Jur1Wn816sI8slGtr",
                    "name": "Gucci Balenciaga",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028b8c56db5cd97ab983558ed9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518b8c56db5cd97ab983558ed9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738b8c56db5cd97ab983558ed9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "oaRcoQSZSne4Vunn0y_39w",
                      "shareUrl": "https://open.spotify.com/album/7d5H1Jur1Wn816sI8slGtr?si=oaRcoQSZSne4Vunn0y_39w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4obDodNku3yyLLZNHkl3c5",
                    "uri": "spotify:album:4obDodNku3yyLLZNHkl3c5",
                    "name": "Flashbacks",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e510e84a79bb58b33495dac5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e510e84a79bb58b33495dac5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e510e84a79bb58b33495dac5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "J4uEB-bDRZC6i7l1o-dYUg",
                      "shareUrl": "https://open.spotify.com/album/4obDodNku3yyLLZNHkl3c5?si=J4uEB-bDRZC6i7l1o-dYUg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "61u4QTomAEmsUDZ9k1gj0M",
                    "uri": "spotify:album:61u4QTomAEmsUDZ9k1gj0M",
                    "name": "Beautiful Lie",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-12-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0271ef4d9db9f7bf56cdcfc35e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485171ef4d9db9f7bf56cdcfc35e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27371ef4d9db9f7bf56cdcfc35e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "B3mYap7wTsSu-uCNumYgdg",
                      "shareUrl": "https://open.spotify.com/album/61u4QTomAEmsUDZ9k1gj0M?si=B3mYap7wTsSu-uCNumYgdg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5HQTa6FgnuL2b6ePYieay5",
                    "uri": "spotify:album:5HQTa6FgnuL2b6ePYieay5",
                    "name": "One Reason (Ferki Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02db0da98593acf906da54422a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851db0da98593acf906da54422a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273db0da98593acf906da54422a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "LzD8LHV9Q1K1SB8Npi7LOA",
                      "shareUrl": "https://open.spotify.com/album/5HQTa6FgnuL2b6ePYieay5?si=LzD8LHV9Q1K1SB8Npi7LOA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "456OCazIPHxeLG7p830H1U",
                    "uri": "spotify:album:456OCazIPHxeLG7p830H1U",
                    "name": "Flashbacks (Yalçın Aşan Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02afa2abf1cf77e05a65c4bffe",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851afa2abf1cf77e05a65c4bffe",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273afa2abf1cf77e05a65c4bffe",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "u8Wz3u6cRyyi60RLUrjRIQ",
                      "shareUrl": "https://open.spotify.com/album/456OCazIPHxeLG7p830H1U?si=u8Wz3u6cRyyi60RLUrjRIQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0lTcqJDMYmahGCOhDYD0Ic",
                    "uri": "spotify:album:0lTcqJDMYmahGCOhDYD0Ic",
                    "name": "Flashbacks (Syde X Nvrmind Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025e895e07ecc011e8c771e8ac",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515e895e07ecc011e8c771e8ac",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735e895e07ecc011e8c771e8ac",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "06ZpMDK-QDqOtp9lJWP4Rw",
                      "shareUrl": "https://open.spotify.com/album/0lTcqJDMYmahGCOhDYD0Ic?si=06ZpMDK-QDqOtp9lJWP4Rw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2Oi38eim2ClvkYETmrw1UK",
                    "uri": "spotify:album:2Oi38eim2ClvkYETmrw1UK",
                    "name": "Flashbacks (Suark Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023a306fff81e2db65dc0dd13d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513a306fff81e2db65dc0dd13d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733a306fff81e2db65dc0dd13d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "3mMqHsDtRuuBj0mfE5dskQ",
                      "shareUrl": "https://open.spotify.com/album/2Oi38eim2ClvkYETmrw1UK?si=3mMqHsDtRuuBj0mfE5dskQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "35VBwoXCW7czQFrpCTplU0",
                    "uri": "spotify:album:35VBwoXCW7czQFrpCTplU0",
                    "name": "Flashbacks (Robert Cristian Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0248b8c1aba98a239d0caf760b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485148b8c1aba98a239d0caf760b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27348b8c1aba98a239d0caf760b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "aKTddfHZQIm3KYQXozxUOQ",
                      "shareUrl": "https://open.spotify.com/album/35VBwoXCW7czQFrpCTplU0?si=aKTddfHZQIm3KYQXozxUOQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6MN3PW9nrqkxjR5zTIJJlt",
                    "uri": "spotify:album:6MN3PW9nrqkxjR5zTIJJlt",
                    "name": "Flashbacks (Nomad Digital Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0241ec20fba0ae19061993c21b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485141ec20fba0ae19061993c21b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27341ec20fba0ae19061993c21b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "j89ezvQyS7KpGWxjUpw6VA",
                      "shareUrl": "https://open.spotify.com/album/6MN3PW9nrqkxjR5zTIJJlt?si=j89ezvQyS7KpGWxjUpw6VA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "12ViO6e8nFT39NW7Wegscd",
                    "uri": "spotify:album:12ViO6e8nFT39NW7Wegscd",
                    "name": "Flashbacks (Maesic Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a0cfba35d3e360195a6609e5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a0cfba35d3e360195a6609e5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a0cfba35d3e360195a6609e5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "JC1g-9o-TJye6guX_6KBKA",
                      "shareUrl": "https://open.spotify.com/album/12ViO6e8nFT39NW7Wegscd?si=JC1g-9o-TJye6guX_6KBKA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5si0w0w3ajLKhYPVvRYyID",
                    "uri": "spotify:album:5si0w0w3ajLKhYPVvRYyID",
                    "name": "Flashbacks (GLDN, FIVE & LAST 60” Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02783c555717721e3b678b226d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851783c555717721e3b678b226d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273783c555717721e3b678b226d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "FTN4DCFCT2KkmGlRZ-wrKg",
                      "shareUrl": "https://open.spotify.com/album/5si0w0w3ajLKhYPVvRYyID?si=FTN4DCFCT2KkmGlRZ-wrKg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4tZKzfdb4d37iyhsviyI7e",
                    "uri": "spotify:album:4tZKzfdb4d37iyhsviyI7e",
                    "name": "Flashbacks (Dj Dark & Mentol Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0260db5f1b39044aea05247c93",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485160db5f1b39044aea05247c93",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27360db5f1b39044aea05247c93",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "q7NX6NkYRoafb3-POxURsg",
                      "shareUrl": "https://open.spotify.com/album/4tZKzfdb4d37iyhsviyI7e?si=q7NX6NkYRoafb3-POxURsg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "13RkwNWWU8WvJ8UiuSjSie",
                    "uri": "spotify:album:13RkwNWWU8WvJ8UiuSjSie",
                    "name": "Flashbacks (Danny Burg Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0245a4b1d76c7781ea8ef7a4ef",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485145a4b1d76c7781ea8ef7a4ef",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27345a4b1d76c7781ea8ef7a4ef",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "TDhVtV9bTs21XVLJrwzOxg",
                      "shareUrl": "https://open.spotify.com/album/13RkwNWWU8WvJ8UiuSjSie?si=TDhVtV9bTs21XVLJrwzOxg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1m82TC7XrBx9Uq5FhMQS1Q",
                    "uri": "spotify:album:1m82TC7XrBx9Uq5FhMQS1Q",
                    "name": "Flashbacks (DJ Tuncay Albayrak Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e026e32336ef5ab966505e3cf74",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048516e32336ef5ab966505e3cf74",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2736e32336ef5ab966505e3cf74",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "pFnMRfSuRWah69WmUiph9g",
                      "shareUrl": "https://open.spotify.com/album/1m82TC7XrBx9Uq5FhMQS1Q?si=pFnMRfSuRWah69WmUiph9g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7uGqnhE91VHClteaLXtXBL",
                    "uri": "spotify:album:7uGqnhE91VHClteaLXtXBL",
                    "name": "Flashbacks (DFM Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025a2ac4f79fde88fbb424b5a2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515a2ac4f79fde88fbb424b5a2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735a2ac4f79fde88fbb424b5a2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "BJd88DeXQh2L5cpL64Nm0g",
                      "shareUrl": "https://open.spotify.com/album/7uGqnhE91VHClteaLXtXBL?si=BJd88DeXQh2L5cpL64Nm0g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1tywrphXZrnsZhg7w1fKKr",
                    "uri": "spotify:album:1tywrphXZrnsZhg7w1fKKr",
                    "name": "Flashbacks (Asher Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02994cd9074c1f2feda6a6a8d1",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851994cd9074c1f2feda6a6a8d1",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273994cd9074c1f2feda6a6a8d1",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "T1ox5nyET7KPLiAUbxVczw",
                      "shareUrl": "https://open.spotify.com/album/1tywrphXZrnsZhg7w1fKKr?si=T1ox5nyET7KPLiAUbxVczw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3axozf8VicioAeHwtZphDl",
                    "uri": "spotify:album:3axozf8VicioAeHwtZphDl",
                    "name": "Call Me Now (Club Mixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-27T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028db8c594e89a442eedd0d4f4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518db8c594e89a442eedd0d4f4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738db8c594e89a442eedd0d4f4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "5Vk5OLIaTn-RzKwigC9lCQ",
                      "shareUrl": "https://open.spotify.com/album/3axozf8VicioAeHwtZphDl?si=5Vk5OLIaTn-RzKwigC9lCQ"
                    },
                    "tracks": {
                      "totalCount": 3
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0eUWQjiE7vMv4ulgUBkOky",
                    "uri": "spotify:album:0eUWQjiE7vMv4ulgUBkOky",
                    "name": "Maza (Adrian Funk X OLiX Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b6e687fda1852e3305d36a20",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b6e687fda1852e3305d36a20",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b6e687fda1852e3305d36a20",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "oOIyE63_QUW3X2RDxWEh5g",
                      "shareUrl": "https://open.spotify.com/album/0eUWQjiE7vMv4ulgUBkOky?si=oOIyE63_QUW3X2RDxWEh5g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1meOpT671M0YXKVleWbNUe",
                    "uri": "spotify:album:1meOpT671M0YXKVleWbNUe",
                    "name": "Heartbreaker (Hayasa G X 2 Duds Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029eaf6dbef90793fcab8754de",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519eaf6dbef90793fcab8754de",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739eaf6dbef90793fcab8754de",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "9DRJTyrnS--oS796CQoZHQ",
                      "shareUrl": "https://open.spotify.com/album/1meOpT671M0YXKVleWbNUe?si=9DRJTyrnS--oS796CQoZHQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3mYosi8SpolghKstXYUUVL",
                    "uri": "spotify:album:3mYosi8SpolghKstXYUUVL",
                    "name": "Flashbacks (Ilkan Günüç x Emrah Turken Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02464f80a3de8081e3ced850e5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851464f80a3de8081e3ced850e5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273464f80a3de8081e3ced850e5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "WK1c6m7pTNy22OreWOIc3g",
                      "shareUrl": "https://open.spotify.com/album/3mYosi8SpolghKstXYUUVL?si=WK1c6m7pTNy22OreWOIc3g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4git7Qdd6SSGo2KTVezvJk",
                    "uri": "spotify:album:4git7Qdd6SSGo2KTVezvJk",
                    "name": "Flashbacks (Frost & NitugaL Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-11-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0248f22660a420a20c5a35578f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485148f22660a420a20c5a35578f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27348f22660a420a20c5a35578f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "fgW1rLSrRRC7yAmDCvQOVw",
                      "shareUrl": "https://open.spotify.com/album/4git7Qdd6SSGo2KTVezvJk?si=fgW1rLSrRRC7yAmDCvQOVw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0YBG91s9UC7YvF8cHBHJKk",
                    "uri": "spotify:album:0YBG91s9UC7YvF8cHBHJKk",
                    "name": "Pretty Thoughts",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-10-30T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0269b119a6758a0b6fad128d13",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485169b119a6758a0b6fad128d13",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27369b119a6758a0b6fad128d13",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "NeLU_xHvQhaEXAfiUc7b6A",
                      "shareUrl": "https://open.spotify.com/album/0YBG91s9UC7YvF8cHBHJKk?si=NeLU_xHvQhaEXAfiUc7b6A"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2DAC8ojG0pgvJUoiwmcS3F",
                    "uri": "spotify:album:2DAC8ojG0pgvJUoiwmcS3F",
                    "name": "Call Me Now",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-10-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02d0357508962439166cb3ffac",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851d0357508962439166cb3ffac",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273d0357508962439166cb3ffac",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "vqXS4XcIRsKLdQwTMtNB0w",
                      "shareUrl": "https://open.spotify.com/album/2DAC8ojG0pgvJUoiwmcS3F?si=vqXS4XcIRsKLdQwTMtNB0w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5femzfalYqis2DdJyWDS1T",
                    "uri": "spotify:album:5femzfalYqis2DdJyWDS1T",
                    "name": "Read My Lips",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-11T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025cf214525404b6d4c455ea7c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515cf214525404b6d4c455ea7c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735cf214525404b6d4c455ea7c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "cng9xPrFSxKG707FVVVxpw",
                      "shareUrl": "https://open.spotify.com/album/5femzfalYqis2DdJyWDS1T?si=cng9xPrFSxKG707FVVVxpw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "72htV6DCLQyi9Wy63SOW3L",
                    "uri": "spotify:album:72htV6DCLQyi9Wy63SOW3L",
                    "name": "Read My Lips (Deejay Killer Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-10T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0292c404bdc6c2a02578e5109e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485192c404bdc6c2a02578e5109e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27392c404bdc6c2a02578e5109e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "wnAJ7s3dTAurzqDHIsPmFA",
                      "shareUrl": "https://open.spotify.com/album/72htV6DCLQyi9Wy63SOW3L?si=wnAJ7s3dTAurzqDHIsPmFA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5a7LjEwDcxYO7gxzK3JlQl",
                    "uri": "spotify:album:5a7LjEwDcxYO7gxzK3JlQl",
                    "name": "Read My Lips (Bttn Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-10T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0241821bcdb43cf83d0dcc519c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485141821bcdb43cf83d0dcc519c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27341821bcdb43cf83d0dcc519c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "UGkImnDuTti6AjC237h0gg",
                      "shareUrl": "https://open.spotify.com/album/5a7LjEwDcxYO7gxzK3JlQl?si=UGkImnDuTti6AjC237h0gg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2UmfNVsAyYfoB0HYsTaRGZ",
                    "uri": "spotify:album:2UmfNVsAyYfoB0HYsTaRGZ",
                    "name": "Read My Lips (Asher Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-10T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ceb541de00133d201d09baec",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ceb541de00133d201d09baec",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ceb541de00133d201d09baec",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "U0a0JlO9T_eJkpG7PY2nzg",
                      "shareUrl": "https://open.spotify.com/album/2UmfNVsAyYfoB0HYsTaRGZ?si=U0a0JlO9T_eJkpG7PY2nzg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "61nRCQts4FH4MlGgq8pEdO",
                    "uri": "spotify:album:61nRCQts4FH4MlGgq8pEdO",
                    "name": "Read My Lips (A-Connection Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-10T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02024e2e55cb72c8d30211b55a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851024e2e55cb72c8d30211b55a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273024e2e55cb72c8d30211b55a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "umXgF6FPQhuFsO1uMG-uFw",
                      "shareUrl": "https://open.spotify.com/album/61nRCQts4FH4MlGgq8pEdO?si=umXgF6FPQhuFsO1uMG-uFw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0YKh5UzzHKZbshkmn6Fq1g",
                    "uri": "spotify:album:0YKh5UzzHKZbshkmn6Fq1g",
                    "name": "Read My Lips (Suark Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0261b6f0dd418c93f28a42fb8c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485161b6f0dd418c93f28a42fb8c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27361b6f0dd418c93f28a42fb8c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "18fM2ByeT-e99vDX_Vj0Pg",
                      "shareUrl": "https://open.spotify.com/album/0YKh5UzzHKZbshkmn6Fq1g?si=18fM2ByeT-e99vDX_Vj0Pg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4zrPEcKbJPnrYR9gQXef02",
                    "uri": "spotify:album:4zrPEcKbJPnrYR9gQXef02",
                    "name": "Read My Lips (Nomad Digital Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0207d5a59643d66e6410bb7a01",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485107d5a59643d66e6410bb7a01",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27307d5a59643d66e6410bb7a01",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "cJkY9uBBQgqDwQWQEu8KpQ",
                      "shareUrl": "https://open.spotify.com/album/4zrPEcKbJPnrYR9gQXef02?si=cJkY9uBBQgqDwQWQEu8KpQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4xusTeCwdS1r5CIi7orUc3",
                    "uri": "spotify:album:4xusTeCwdS1r5CIi7orUc3",
                    "name": "Read My Lips (Mert Hakan & Soner Karaca Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0212f55859323caff028417234",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485112f55859323caff028417234",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27312f55859323caff028417234",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "e32GWNMtS-2Yn6A0MOJ6Iw",
                      "shareUrl": "https://open.spotify.com/album/4xusTeCwdS1r5CIi7orUc3?si=e32GWNMtS-2Yn6A0MOJ6Iw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1lnzxi9DzkaboUP2d2B0wv",
                    "uri": "spotify:album:1lnzxi9DzkaboUP2d2B0wv",
                    "name": "Read My Lips (Live Version)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0288c8a54e9fb51b81fabbf419",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485188c8a54e9fb51b81fabbf419",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27388c8a54e9fb51b81fabbf419",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "i-KJATzqRMyT5KT7yUslJg",
                      "shareUrl": "https://open.spotify.com/album/1lnzxi9DzkaboUP2d2B0wv?si=i-KJATzqRMyT5KT7yUslJg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2YChwuBfvhxBBfbAhwES3e",
                    "uri": "spotify:album:2YChwuBfvhxBBfbAhwES3e",
                    "name": "Read My Lips (Kom Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0287a719081480c4d357d9ec43",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485187a719081480c4d357d9ec43",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27387a719081480c4d357d9ec43",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "KjLC29vhRMeRKCbGmpXVtQ",
                      "shareUrl": "https://open.spotify.com/album/2YChwuBfvhxBBfbAhwES3e?si=KjLC29vhRMeRKCbGmpXVtQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6rv03r6Lbvky1sBJsz91gT",
                    "uri": "spotify:album:6rv03r6Lbvky1sBJsz91gT",
                    "name": "Read My Lips (Enver Yıldırım Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025b28edc36900e3bbbd62a821",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515b28edc36900e3bbbd62a821",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735b28edc36900e3bbbd62a821",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "UsYFMwBVTNqkMsSW2ZZT-Q",
                      "shareUrl": "https://open.spotify.com/album/6rv03r6Lbvky1sBJsz91gT?si=UsYFMwBVTNqkMsSW2ZZT-Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1B6HKEqwxDK62wfNvTYFd2",
                    "uri": "spotify:album:1B6HKEqwxDK62wfNvTYFd2",
                    "name": "Read My Lips (Emrah Is & Furkan Syzo Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-09-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e41f6805869b1a300bef15c4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e41f6805869b1a300bef15c4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e41f6805869b1a300bef15c4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "okOPwmB1Rka_qrzVRO0fvg",
                      "shareUrl": "https://open.spotify.com/album/1B6HKEqwxDK62wfNvTYFd2?si=okOPwmB1Rka_qrzVRO0fvg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0xBL5r92lV5SZDU8FvrZ1u",
                    "uri": "spotify:album:0xBL5r92lV5SZDU8FvrZ1u",
                    "name": "Discoteka",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-07-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025e57bd5850c48cba40516dad",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515e57bd5850c48cba40516dad",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735e57bd5850c48cba40516dad",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "q6B_sZpvS0akJ7cXYvC7eA",
                      "shareUrl": "https://open.spotify.com/album/0xBL5r92lV5SZDU8FvrZ1u?si=q6B_sZpvS0akJ7cXYvC7eA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  },
                  {
                    "id": "41DxWGed4b9UhhlV1NMTUs",
                    "uri": "spotify:album:41DxWGed4b9UhhlV1NMTUs",
                    "name": "Discoteka (feat. INNA)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-07-23T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028385aa1ee819a15f1061845e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518385aa1ee819a15f1061845e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738385aa1ee819a15f1061845e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "SymK50kxTN6WXF0ZsCQiig",
                      "shareUrl": "https://open.spotify.com/album/41DxWGed4b9UhhlV1NMTUs?si=SymK50kxTN6WXF0ZsCQiig"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6IW8o4Lz9P9ujfUgOdHWtu",
                    "uri": "spotify:album:6IW8o4Lz9P9ujfUgOdHWtu",
                    "name": "Discoteka (Remix Bundle)",
                    "type": "EP",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-07-22T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0254089c2162abee141be954ba",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485154089c2162abee141be954ba",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27354089c2162abee141be954ba",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "jXhqo-g2S1-WfdcHV6A6zA",
                      "shareUrl": "https://open.spotify.com/album/6IW8o4Lz9P9ujfUgOdHWtu?si=jXhqo-g2S1-WfdcHV6A6zA"
                    },
                    "tracks": {
                      "totalCount": 4
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4I6pDC6siENO88V77O3Mpb",
                    "uri": "spotify:album:4I6pDC6siENO88V77O3Mpb",
                    "name": "Nobody",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-06-26T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02cea251d1d1e4557d87f72fbd",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851cea251d1d1e4557d87f72fbd",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273cea251d1d1e4557d87f72fbd",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "-Tk-j6NJRDyoMUWvZzzF2g",
                      "shareUrl": "https://open.spotify.com/album/4I6pDC6siENO88V77O3Mpb?si=-Tk-j6NJRDyoMUWvZzzF2g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0Y1Nl1sqnxQApaslRhpwTP",
                    "uri": "spotify:album:0Y1Nl1sqnxQApaslRhpwTP",
                    "name": "Nobody (Extended Mix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-06-25T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023cf558c1af6a3871d6e4c995",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513cf558c1af6a3871d6e4c995",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733cf558c1af6a3871d6e4c995",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "5GjiiCRoRiSsNhoT5dj26g",
                      "shareUrl": "https://open.spotify.com/album/0Y1Nl1sqnxQApaslRhpwTP?si=5GjiiCRoRiSsNhoT5dj26g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2UicE2GticRO28ik8hMHxL",
                    "uri": "spotify:album:2UicE2GticRO28ik8hMHxL",
                    "name": "Nobody (Ferki Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-06-24T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024bb3a004e62ac989ef48003f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514bb3a004e62ac989ef48003f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734bb3a004e62ac989ef48003f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "gaU3AQuFQEePAiWEjgOEcg",
                      "shareUrl": "https://open.spotify.com/album/2UicE2GticRO28ik8hMHxL?si=gaU3AQuFQEePAiWEjgOEcg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "72V1OiTWcASGUaGvQuw34N",
                    "uri": "spotify:album:72V1OiTWcASGUaGvQuw34N",
                    "name": "VKTM",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-05-29T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02cc27c32b789fd5ef45bbba89",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851cc27c32b789fd5ef45bbba89",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273cc27c32b789fd5ef45bbba89",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "v3slQyBMR7WuJSGHfFKKqA",
                      "shareUrl": "https://open.spotify.com/album/72V1OiTWcASGUaGvQuw34N?si=v3slQyBMR7WuJSGHfFKKqA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7ol5R0cGYVflCySSwIsCAl",
                    "uri": "spotify:album:7ol5R0cGYVflCySSwIsCAl",
                    "name": "Sober",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-05-06T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f56f13d5d7f5d62d3ec4f1f6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f56f13d5d7f5d62d3ec4f1f6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f56f13d5d7f5d62d3ec4f1f6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "aI0ZCgQARV-AfKNXiiHQ8w",
                      "shareUrl": "https://open.spotify.com/album/7ol5R0cGYVflCySSwIsCAl?si=aI0ZCgQARV-AfKNXiiHQ8w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5sHU0XJ897eLbktQSsw0ru",
                    "uri": "spotify:album:5sHU0XJ897eLbktQSsw0ru",
                    "name": "Sober (Extended Mix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-05-05T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e020a8c7e22cd6a26d4c5110329",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048510a8c7e22cd6a26d4c5110329",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2730a8c7e22cd6a26d4c5110329",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "G7KXoup2Qwa8Cmv4ZDS7lg",
                      "shareUrl": "https://open.spotify.com/album/5sHU0XJ897eLbktQSsw0ru?si=G7KXoup2Qwa8Cmv4ZDS7lg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7qcWOcpdD7uSZoaJIrReH9",
                    "uri": "spotify:album:7qcWOcpdD7uSZoaJIrReH9",
                    "name": "Not My Baby",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-03T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e572f31d1a5366683877dd83",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e572f31d1a5366683877dd83",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e572f31d1a5366683877dd83",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "YdP-GYstTLaSCD2EX4HK4g",
                      "shareUrl": "https://open.spotify.com/album/7qcWOcpdD7uSZoaJIrReH9?si=YdP-GYstTLaSCD2EX4HK4g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3HhiJjraZFnQmMZcbui1Dv",
                    "uri": "spotify:album:3HhiJjraZFnQmMZcbui1Dv",
                    "name": "Sober (Nomad Digital Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024d5d0bb1d0d38e9bad819e02",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514d5d0bb1d0d38e9bad819e02",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734d5d0bb1d0d38e9bad819e02",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "4DUrzn1bRTuvdqU2XmQInQ",
                      "shareUrl": "https://open.spotify.com/album/3HhiJjraZFnQmMZcbui1Dv?si=4DUrzn1bRTuvdqU2XmQInQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6qx7tgsJj2mH0YLZ7Ruicx",
                    "uri": "spotify:album:6qx7tgsJj2mH0YLZ7Ruicx",
                    "name": "Sober (Mally Gulbetekin Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ee722c8919af60622c90ca31",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ee722c8919af60622c90ca31",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ee722c8919af60622c90ca31",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Rpf_CKgOTPG77V2sw5kBLw",
                      "shareUrl": "https://open.spotify.com/album/6qx7tgsJj2mH0YLZ7Ruicx?si=Rpf_CKgOTPG77V2sw5kBLw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1k6lqf5GPTWDSRwx8Szgbd",
                    "uri": "spotify:album:1k6lqf5GPTWDSRwx8Szgbd",
                    "name": "Sober (Francis VI Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027c276d34771d33cf7169a7dd",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517c276d34771d33cf7169a7dd",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737c276d34771d33cf7169a7dd",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "SbHDNk4KRNqc48dyjP4z8g",
                      "shareUrl": "https://open.spotify.com/album/1k6lqf5GPTWDSRwx8Szgbd?si=SbHDNk4KRNqc48dyjP4z8g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5iby1if3aXBpgDaGsbAyk7",
                    "uri": "spotify:album:5iby1if3aXBpgDaGsbAyk7",
                    "name": "Sober (Delighters & LeGround Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02235c547c488fd5f6c594ac8d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851235c547c488fd5f6c594ac8d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273235c547c488fd5f6c594ac8d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "eDUNz2igRs680MIRg360FA",
                      "shareUrl": "https://open.spotify.com/album/5iby1if3aXBpgDaGsbAyk7?si=eDUNz2igRs680MIRg360FA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3gosVFxZkOlYCHCGqfg12g",
                    "uri": "spotify:album:3gosVFxZkOlYCHCGqfg12g",
                    "name": "Not My Baby (ToldorTunes Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e020bbae3e6bc31eed511b8f322",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048510bbae3e6bc31eed511b8f322",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2730bbae3e6bc31eed511b8f322",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "44WxSRy4Q1eoT8kCGqXauA",
                      "shareUrl": "https://open.spotify.com/album/3gosVFxZkOlYCHCGqfg12g?si=44WxSRy4Q1eoT8kCGqXauA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0edQV0rgh2KSibKbLA5uuj",
                    "uri": "spotify:album:0edQV0rgh2KSibKbLA5uuj",
                    "name": "Not My Baby (Tha Groove Junkeez Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027ecc2ec564797c2e8cbe0744",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517ecc2ec564797c2e8cbe0744",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737ecc2ec564797c2e8cbe0744",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GCHsK3tTQjqPNEcRLuSb-Q",
                      "shareUrl": "https://open.spotify.com/album/0edQV0rgh2KSibKbLA5uuj?si=GCHsK3tTQjqPNEcRLuSb-Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2dHJ2bAHIZtZp66aKUkh1k",
                    "uri": "spotify:album:2dHJ2bAHIZtZp66aKUkh1k",
                    "name": "Not My Baby (Szanto Denis Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022c5ce91a5b5b50739949feba",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512c5ce91a5b5b50739949feba",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732c5ce91a5b5b50739949feba",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "KpxZZysuTiuOX-_TcQlCRA",
                      "shareUrl": "https://open.spotify.com/album/2dHJ2bAHIZtZp66aKUkh1k?si=KpxZZysuTiuOX-_TcQlCRA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7wFMeCNO4f6iHEDS01Tcqy",
                    "uri": "spotify:album:7wFMeCNO4f6iHEDS01Tcqy",
                    "name": "Not My Baby (Stefanescu Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021b3a4a67de9da843c936be87",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511b3a4a67de9da843c936be87",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731b3a4a67de9da843c936be87",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "CgJySE3sRtiVA0suE7x-VQ",
                      "shareUrl": "https://open.spotify.com/album/7wFMeCNO4f6iHEDS01Tcqy?si=CgJySE3sRtiVA0suE7x-VQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3tdWyOltETIFOjlRY3uulB",
                    "uri": "spotify:album:3tdWyOltETIFOjlRY3uulB",
                    "name": "Not My Baby (ScreeN Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a369430de4d4206391cd7d59",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a369430de4d4206391cd7d59",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a369430de4d4206391cd7d59",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "LGi4cytXSvWbF58DYVFo3Q",
                      "shareUrl": "https://open.spotify.com/album/3tdWyOltETIFOjlRY3uulB?si=LGi4cytXSvWbF58DYVFo3Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "77sz6QPMRxZ55DkWg8Myqe",
                    "uri": "spotify:album:77sz6QPMRxZ55DkWg8Myqe",
                    "name": "Not My Baby (Pessto Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0225f966abcf52718b313a9bda",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485125f966abcf52718b313a9bda",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27325f966abcf52718b313a9bda",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "2ds85rxUQ6uciWBUpz9AhQ",
                      "shareUrl": "https://open.spotify.com/album/77sz6QPMRxZ55DkWg8Myqe?si=2ds85rxUQ6uciWBUpz9AhQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4PKedM4KgxevihGjjSnlBE",
                    "uri": "spotify:album:4PKedM4KgxevihGjjSnlBE",
                    "name": "Not My Baby (NRD1 From SHANGUY Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02880bae9ffe7257693c074075",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851880bae9ffe7257693c074075",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273880bae9ffe7257693c074075",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "MbU-gHiMQxWfk8g7vQYRjg",
                      "shareUrl": "https://open.spotify.com/album/4PKedM4KgxevihGjjSnlBE?si=MbU-gHiMQxWfk8g7vQYRjg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "03npYOTfiIASDO45vdBPIk",
                    "uri": "spotify:album:03npYOTfiIASDO45vdBPIk",
                    "name": "Not My Baby (Mia Amare Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02512bce0b2e162074e73bbdf1",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851512bce0b2e162074e73bbdf1",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273512bce0b2e162074e73bbdf1",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "h1IvY62rSfqBwI8iRy9OSg",
                      "shareUrl": "https://open.spotify.com/album/03npYOTfiIASDO45vdBPIk?si=h1IvY62rSfqBwI8iRy9OSg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7CYUTdoS2HF6lG17SePxn2",
                    "uri": "spotify:album:7CYUTdoS2HF6lG17SePxn2",
                    "name": "Not My Baby (Mert Can Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0255453b759c737a7ac4f15526",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485155453b759c737a7ac4f15526",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27355453b759c737a7ac4f15526",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "QSpo7gRVR2af9G3UkInCUw",
                      "shareUrl": "https://open.spotify.com/album/7CYUTdoS2HF6lG17SePxn2?si=QSpo7gRVR2af9G3UkInCUw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4zfpWVqYJeGdweNRaSsBmo",
                    "uri": "spotify:album:4zfpWVqYJeGdweNRaSsBmo",
                    "name": "Not My Baby (Maesic Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e5c112bbb32aec2d06d23acd",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e5c112bbb32aec2d06d23acd",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e5c112bbb32aec2d06d23acd",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "TLMzABIcRySN7zIU4KPz8g",
                      "shareUrl": "https://open.spotify.com/album/4zfpWVqYJeGdweNRaSsBmo?si=TLMzABIcRySN7zIU4KPz8g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  },
                  {
                    "id": "29pBlqYRgZqcloD70S3V7t",
                    "uri": "spotify:album:29pBlqYRgZqcloD70S3V7t",
                    "name": "Not My Baby (Maesic Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-05-08T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ad8bab76702874f729cf3dde",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ad8bab76702874f729cf3dde",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ad8bab76702874f729cf3dde",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "DXvd7S2sTbmf-h_W8tm8UQ",
                      "shareUrl": "https://open.spotify.com/album/29pBlqYRgZqcloD70S3V7t?si=DXvd7S2sTbmf-h_W8tm8UQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "75AwDw9npSxWNt3qcchDpa",
                    "uri": "spotify:album:75AwDw9npSxWNt3qcchDpa",
                    "name": "Not My Baby (Karim Naas Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02fe82f2f244f8661a36106829",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851fe82f2f244f8661a36106829",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273fe82f2f244f8661a36106829",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "YIfDmOzPSRmG_zwDq1xcSw",
                      "shareUrl": "https://open.spotify.com/album/75AwDw9npSxWNt3qcchDpa?si=YIfDmOzPSRmG_zwDq1xcSw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2WFkEF5brxNMq3xO85Pb2f",
                    "uri": "spotify:album:2WFkEF5brxNMq3xO85Pb2f",
                    "name": "Not My Baby (Joe Hike Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e026decca238eb2a137c044de6a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048516decca238eb2a137c044de6a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2736decca238eb2a137c044de6a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "w5rVCOSLQlq7hs0EXVStuQ",
                      "shareUrl": "https://open.spotify.com/album/2WFkEF5brxNMq3xO85Pb2f?si=w5rVCOSLQlq7hs0EXVStuQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3D9j03hHA9ZkYOxHYxQTfg",
                    "uri": "spotify:album:3D9j03hHA9ZkYOxHYxQTfg",
                    "name": "Not My Baby (Ferki Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021bb48791231a97f48b7b1c8e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511bb48791231a97f48b7b1c8e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731bb48791231a97f48b7b1c8e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "bv_wblR-TGms8Czj5Starw",
                      "shareUrl": "https://open.spotify.com/album/3D9j03hHA9ZkYOxHYxQTfg?si=bv_wblR-TGms8Czj5Starw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2wkOPBzIvxH5GGNZ6mXKAv",
                    "uri": "spotify:album:2wkOPBzIvxH5GGNZ6mXKAv",
                    "name": "Not My Baby (Dimarno Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02538bef70eaefb2125c0b1c76",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851538bef70eaefb2125c0b1c76",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273538bef70eaefb2125c0b1c76",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "vUNzxSjgS7aY0oNZCfkGYQ",
                      "shareUrl": "https://open.spotify.com/album/2wkOPBzIvxH5GGNZ6mXKAv?si=vUNzxSjgS7aY0oNZCfkGYQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2TAKSlaoAoagMcfkFP7SH0",
                    "uri": "spotify:album:2TAKSlaoAoagMcfkFP7SH0",
                    "name": "Not My Baby (DJ Criswell Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023054f5bd449a69ea1700a663",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513054f5bd449a69ea1700a663",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733054f5bd449a69ea1700a663",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "8yit-Kn_Q4G1PZ30RU7Gag",
                      "shareUrl": "https://open.spotify.com/album/2TAKSlaoAoagMcfkFP7SH0?si=8yit-Kn_Q4G1PZ30RU7Gag"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2YEL2uJQKXoJvOyK1mu23U",
                    "uri": "spotify:album:2YEL2uJQKXoJvOyK1mu23U",
                    "name": "Not My Baby (Beatz Projekted Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e020cad014bf9be0e4ebbd7e177",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048510cad014bf9be0e4ebbd7e177",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2730cad014bf9be0e4ebbd7e177",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "KssJnne5QoKoLcIFvc4Fuw",
                      "shareUrl": "https://open.spotify.com/album/2YEL2uJQKXoJvOyK1mu23U?si=KssJnne5QoKoLcIFvc4Fuw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1iRjBdGNlO0h6Py3t4LLhm",
                    "uri": "spotify:album:1iRjBdGNlO0h6Py3t4LLhm",
                    "name": "Not My Baby (Adrian Funk X OLiX Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-04-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021dfa9b69baadea88979916b6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511dfa9b69baadea88979916b6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731dfa9b69baadea88979916b6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "2ynSZU_hSnaOorKWGab-Aw",
                      "shareUrl": "https://open.spotify.com/album/1iRjBdGNlO0h6Py3t4LLhm?si=2ynSZU_hSnaOorKWGab-Aw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5olrtJHaVB2Glqnost1w0N",
                    "uri": "spotify:album:5olrtJHaVB2Glqnost1w0N",
                    "name": "Bebe (Eric Deray Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-02-05T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02061996ebe21c8a19281a50df",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851061996ebe21c8a19281a50df",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273061996ebe21c8a19281a50df",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "8fSDOf26SS2_pH2WIAD9iQ",
                      "shareUrl": "https://open.spotify.com/album/5olrtJHaVB2Glqnost1w0N?si=8fSDOf26SS2_pH2WIAD9iQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0zX2LoHcVx0nOCnKpiEaZz",
                    "uri": "spotify:album:0zX2LoHcVx0nOCnKpiEaZz",
                    "name": "Bebe (Asher Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-01-31T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ae466b595a941ed61fb4ab65",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ae466b595a941ed61fb4ab65",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ae466b595a941ed61fb4ab65",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "vDZiUqEaThKlNGs_9nEnww",
                      "shareUrl": "https://open.spotify.com/album/0zX2LoHcVx0nOCnKpiEaZz?si=vDZiUqEaThKlNGs_9nEnww"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "24TeGMl9E5gk5DLI2m7uWP",
                    "uri": "spotify:album:24TeGMl9E5gk5DLI2m7uWP",
                    "name": "Bebe (AYA Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-01-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0256bb6a1a0aea6332599fa406",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485156bb6a1a0aea6332599fa406",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27356bb6a1a0aea6332599fa406",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "saZZ6vpQSOa9bBBNqi-e8g",
                      "shareUrl": "https://open.spotify.com/album/24TeGMl9E5gk5DLI2m7uWP?si=saZZ6vpQSOa9bBBNqi-e8g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3DZMBKBsPRxFyxxDQowtJN",
                    "uri": "spotify:album:3DZMBKBsPRxFyxxDQowtJN",
                    "name": "Bebe (Yaniss Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2020,
                      "isoString": "2020-01-06T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0238f0649af6cbac1f8c4d035e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485138f0649af6cbac1f8c4d035e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27338f0649af6cbac1f8c4d035e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "tZtlrmeLQ6mEzDrvCFiFfw",
                      "shareUrl": "https://open.spotify.com/album/3DZMBKBsPRxFyxxDQowtJN?si=tZtlrmeLQ6mEzDrvCFiFfw"
                    },
                    "tracks": {
                      "totalCount": 2
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3LCHuSmCOUiPOR8J7nd64d",
                    "uri": "spotify:album:3LCHuSmCOUiPOR8J7nd64d",
                    "name": "Bebe (Tennebreck & Disco Biscuit Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-12-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02bf9a5267fabfbba227a6cd01",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851bf9a5267fabfbba227a6cd01",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273bf9a5267fabfbba227a6cd01",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "aLrxlZglQoK9jfOUqy3lHQ",
                      "shareUrl": "https://open.spotify.com/album/3LCHuSmCOUiPOR8J7nd64d?si=aLrxlZglQoK9jfOUqy3lHQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6XWN7tHMATBLsHNOYJpPEx",
                    "uri": "spotify:album:6XWN7tHMATBLsHNOYJpPEx",
                    "name": "Bebe (Stefanescu Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-12-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02be894f81698a4c3a4d0fbc77",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851be894f81698a4c3a4d0fbc77",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273be894f81698a4c3a4d0fbc77",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "6HLvZQo7Sy-HEU-uQ2dKFw",
                      "shareUrl": "https://open.spotify.com/album/6XWN7tHMATBLsHNOYJpPEx?si=6HLvZQo7Sy-HEU-uQ2dKFw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7y6RbuCizvORVv1pPc3muD",
                    "uri": "spotify:album:7y6RbuCizvORVv1pPc3muD",
                    "name": "Bebe (Asproiu Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-12-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028e7c433924f69fa0f6b2b957",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518e7c433924f69fa0f6b2b957",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738e7c433924f69fa0f6b2b957",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "inh0sUnyTTiwDbclVWAYpg",
                      "shareUrl": "https://open.spotify.com/album/7y6RbuCizvORVv1pPc3muD?si=inh0sUnyTTiwDbclVWAYpg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5GMHJZJTk4Mc9CVUh7MxIg",
                    "uri": "spotify:album:5GMHJZJTk4Mc9CVUh7MxIg",
                    "name": "Bebe",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-11-04T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f4faad37074b9ea79fdb486d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f4faad37074b9ea79fdb486d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f4faad37074b9ea79fdb486d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "rJEEb_efRm6qvaLQ7c62Cw",
                      "shareUrl": "https://open.spotify.com/album/5GMHJZJTk4Mc9CVUh7MxIg?si=rJEEb_efRm6qvaLQ7c62Cw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6AnbRr35SS8iy9pXwrpOiW",
                    "uri": "spotify:album:6AnbRr35SS8iy9pXwrpOiW",
                    "name": "Te Vas (Maesic Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-07-12T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028ed7367ee5ad60e1337db2ed",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518ed7367ee5ad60e1337db2ed",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738ed7367ee5ad60e1337db2ed",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GoZFNczLSjG41BO6DwI-Ng",
                      "shareUrl": "https://open.spotify.com/album/6AnbRr35SS8iy9pXwrpOiW?si=GoZFNczLSjG41BO6DwI-Ng"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0ZgEzflxty87XgjrxU3qIJ",
                    "uri": "spotify:album:0ZgEzflxty87XgjrxU3qIJ",
                    "name": "Tu Manera",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-03-08T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02402817409353dd85131f9263",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851402817409353dd85131f9263",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273402817409353dd85131f9263",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "nCJxCNvBSTemqhJQg9lYTA",
                      "shareUrl": "https://open.spotify.com/album/0ZgEzflxty87XgjrxU3qIJ?si=nCJxCNvBSTemqhJQg9lYTA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0miggCdTfw4NsqNfj1pbIW",
                    "uri": "spotify:album:0miggCdTfw4NsqNfj1pbIW",
                    "name": "Sin Ti",
                    "type": "SINGLE",
                    "date": {
                      "year": 2019,
                      "isoString": "2019-01-18T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e026e29f5992b23c4f1277cb11e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048516e29f5992b23c4f1277cb11e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2736e29f5992b23c4f1277cb11e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "LXFA7DYGQV2-sJMke7CjwQ",
                      "shareUrl": "https://open.spotify.com/album/0miggCdTfw4NsqNfj1pbIW?si=LXFA7DYGQV2-sJMke7CjwQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "14mk1H4BOjxc5dO9j41rSK",
                    "uri": "spotify:album:14mk1H4BOjxc5dO9j41rSK",
                    "name": "Iguana",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-11-30T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f2f60663e50d5f561d99966c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f2f60663e50d5f561d99966c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f2f60663e50d5f561d99966c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "czsAE024TfaZJk6r1kdm2w",
                      "shareUrl": "https://open.spotify.com/album/14mk1H4BOjxc5dO9j41rSK?si=czsAE024TfaZJk6r1kdm2w"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5uQmEPXtSJrCwVKFkfcujV",
                    "uri": "spotify:album:5uQmEPXtSJrCwVKFkfcujV",
                    "name": "RA",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-11-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f224e31023fa0cc0f58f232e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f224e31023fa0cc0f58f232e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f224e31023fa0cc0f58f232e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "UfUomkvJTzGDyXKYlMPPSw",
                      "shareUrl": "https://open.spotify.com/album/5uQmEPXtSJrCwVKFkfcujV?si=UfUomkvJTzGDyXKYlMPPSw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5weyIz2s5vuijilcPZyA7Z",
                    "uri": "spotify:album:5weyIz2s5vuijilcPZyA7Z",
                    "name": "No Help",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-09-28T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02478d67b10b8543ba0c0884fb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851478d67b10b8543ba0c0884fb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273478d67b10b8543ba0c0884fb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "xHtmxCP6QXWfIUhHAon2Zg",
                      "shareUrl": "https://open.spotify.com/album/5weyIz2s5vuijilcPZyA7Z?si=xHtmxCP6QXWfIUhHAon2Zg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2VVoUgCn5jWCA67pyrIXR3",
                    "uri": "spotify:album:2VVoUgCn5jWCA67pyrIXR3",
                    "name": "Pentru Că (Dirty Nano Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-06-08T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02de86e3012c591b236ae1bfb8",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851de86e3012c591b236ae1bfb8",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273de86e3012c591b236ae1bfb8",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "cSOJHl9UTDq97XfmhBcrag",
                      "shareUrl": "https://open.spotify.com/album/2VVoUgCn5jWCA67pyrIXR3?si=cSOJHl9UTDq97XfmhBcrag"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3srUNlIfoiCFxKqRMy6iet",
                    "uri": "spotify:album:3srUNlIfoiCFxKqRMy6iet",
                    "name": "Me Gusta (Remixes)",
                    "type": "EP",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-06-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0202efb40096fc56b8d7cb92bb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485102efb40096fc56b8d7cb92bb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27302efb40096fc56b8d7cb92bb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "G8qcsP2JQ_edvd1tXS2ppg",
                      "shareUrl": "https://open.spotify.com/album/3srUNlIfoiCFxKqRMy6iet?si=G8qcsP2JQ_edvd1tXS2ppg"
                    },
                    "tracks": {
                      "totalCount": 5
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2Do322H0G4l7AWAS6R3lAF",
                    "uri": "spotify:album:2Do322H0G4l7AWAS6R3lAF",
                    "name": "Pentru Ca (Dario Vega Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-31T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02965d3e55b9bbca56cff43265",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851965d3e55b9bbca56cff43265",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273965d3e55b9bbca56cff43265",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "nw3HzQ8_SQuCEZZR-DyfJg",
                      "shareUrl": "https://open.spotify.com/album/2Do322H0G4l7AWAS6R3lAF?si=nw3HzQ8_SQuCEZZR-DyfJg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3vUwto7uuXxWRa9IMhDQz0",
                    "uri": "spotify:album:3vUwto7uuXxWRa9IMhDQz0",
                    "name": "Pentru Ca (Asher Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-31T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a6be7a352690274970037598",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a6be7a352690274970037598",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a6be7a352690274970037598",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "5IggZdj4QXGz5TDZKQKGKw",
                      "shareUrl": "https://open.spotify.com/album/3vUwto7uuXxWRa9IMhDQz0?si=5IggZdj4QXGz5TDZKQKGKw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3TIr0srqUVcDCRCLnhzBBs",
                    "uri": "spotify:album:3TIr0srqUVcDCRCLnhzBBs",
                    "name": "Pentru Ca (Nema Cutura Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025d716368c98d04c0026c71c6",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515d716368c98d04c0026c71c6",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735d716368c98d04c0026c71c6",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "KTDOh76XQ-C0RLjQW_lZxA",
                      "shareUrl": "https://open.spotify.com/album/3TIr0srqUVcDCRCLnhzBBs?si=KTDOh76XQ-C0RLjQW_lZxA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5o59pEHruZnGJUcCyehNBf",
                    "uri": "spotify:album:5o59pEHruZnGJUcCyehNBf",
                    "name": "Pentru Ca (Elemer Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e021296f7636c3386c6a32af360",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048511296f7636c3386c6a32af360",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2731296f7636c3386c6a32af360",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "NA2JfYCjQFuNKEyEiJMuQA",
                      "shareUrl": "https://open.spotify.com/album/5o59pEHruZnGJUcCyehNBf?si=NA2JfYCjQFuNKEyEiJMuQA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "04cCLOxEkrqYPk6GhSETkO",
                    "uri": "spotify:album:04cCLOxEkrqYPk6GhSETkO",
                    "name": "Pentru Ca (DJ Criswell Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ddcdef53afd8bd077e626f0a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ddcdef53afd8bd077e626f0a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ddcdef53afd8bd077e626f0a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "3cGKDxrKSE-rWl9X_wovUg",
                      "shareUrl": "https://open.spotify.com/album/04cCLOxEkrqYPk6GhSETkO?si=3cGKDxrKSE-rWl9X_wovUg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1FTYDFA0a6tWiGcFQFTL1f",
                    "uri": "spotify:album:1FTYDFA0a6tWiGcFQFTL1f",
                    "name": "Pentru Că (Vladish Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-07T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02cad6ea2e7dbde0e4856c30f2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851cad6ea2e7dbde0e4856c30f2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273cad6ea2e7dbde0e4856c30f2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "lBP4GpQhRtqGbPIKL4Rn5Q",
                      "shareUrl": "https://open.spotify.com/album/1FTYDFA0a6tWiGcFQFTL1f?si=lBP4GpQhRtqGbPIKL4Rn5Q"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0sdBl2YakeaGt6Kt96boXY",
                    "uri": "spotify:album:0sdBl2YakeaGt6Kt96boXY",
                    "name": "Pentru Că (Midi Culture Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-05-07T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029b52a25ab75a6a8145b1f183",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519b52a25ab75a6a8145b1f183",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739b52a25ab75a6a8145b1f183",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "JoHPETtVQ3irFwlaMqHLVA",
                      "shareUrl": "https://open.spotify.com/album/0sdBl2YakeaGt6Kt96boXY?si=JoHPETtVQ3irFwlaMqHLVA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "70dqTiFt2SG6hNdwTD2IK8",
                    "uri": "spotify:album:70dqTiFt2SG6hNdwTD2IK8",
                    "name": "Pentru Ca",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-04-26T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02372de8e9a478b33f560c904c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851372de8e9a478b33f560c904c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273372de8e9a478b33f560c904c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "j2BTHUOiRP6A9xo2qyS5YA",
                      "shareUrl": "https://open.spotify.com/album/70dqTiFt2SG6hNdwTD2IK8?si=j2BTHUOiRP6A9xo2qyS5YA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1q7V34U3IoZASQfM3salUT",
                    "uri": "spotify:album:1q7V34U3IoZASQfM3salUT",
                    "name": "Nirvana (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-03-30T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0223aa9544a4cfba798904f5ba",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485123aa9544a4cfba798904f5ba",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27323aa9544a4cfba798904f5ba",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "0KH54AtNRdiwTNmd3pBK2g",
                      "shareUrl": "https://open.spotify.com/album/1q7V34U3IoZASQfM3salUT?si=0KH54AtNRdiwTNmd3pBK2g"
                    },
                    "tracks": {
                      "totalCount": 9
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1X9WzQbYgNBbcwzFXyICj9",
                    "uri": "spotify:album:1X9WzQbYgNBbcwzFXyICj9",
                    "name": "Me Gusta",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-03-16T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02741a4481fc6cb06dabb5ad9d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851741a4481fc6cb06dabb5ad9d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273741a4481fc6cb06dabb5ad9d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "NqziwgFHQ-WCxh3PthZGbQ",
                      "shareUrl": "https://open.spotify.com/album/1X9WzQbYgNBbcwzFXyICj9?si=NqziwgFHQ-WCxh3PthZGbQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3P5RyxRSauLp1Zj0kYeAK9",
                    "uri": "spotify:album:3P5RyxRSauLp1Zj0kYeAK9",
                    "name": "Stay (feat. INNA)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-03-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02bc763346904b0eef35628195",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851bc763346904b0eef35628195",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273bc763346904b0eef35628195",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "7TQDX0VnS3-TOy6N2K2VaA",
                      "shareUrl": "https://open.spotify.com/album/3P5RyxRSauLp1Zj0kYeAK9?si=7TQDX0VnS3-TOy6N2K2VaA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1kXwdQazS4Z8BUQ8OavZFI",
                    "uri": "spotify:album:1kXwdQazS4Z8BUQ8OavZFI",
                    "name": "Nirvana",
                    "type": "SINGLE",
                    "date": {
                      "year": 2018,
                      "isoString": "2018-01-05T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023472c52736062ffea856a37c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513472c52736062ffea856a37c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733472c52736062ffea856a37c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "eqODSXmcQFGCvt7opq-aRg",
                      "shareUrl": "https://open.spotify.com/album/1kXwdQazS4Z8BUQ8OavZFI?si=eqODSXmcQFGCvt7opq-aRg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "75dzUE1ofDCtYyQHDB5pUk",
                    "uri": "spotify:album:75dzUE1ofDCtYyQHDB5pUk",
                    "name": "Ruleta (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-08-25T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027205de747ae214897afba6ff",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517205de747ae214897afba6ff",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737205de747ae214897afba6ff",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Lsxwq4ETRVmjeYrwcLkdpw",
                      "shareUrl": "https://open.spotify.com/album/75dzUE1ofDCtYyQHDB5pUk?si=Lsxwq4ETRVmjeYrwcLkdpw"
                    },
                    "tracks": {
                      "totalCount": 12
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5avELfEfgOrXmXU8Ofjw2n",
                    "uri": "spotify:album:5avELfEfgOrXmXU8Ofjw2n",
                    "name": "Ruleta",
                    "type": "SINGLE",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-07-07T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b83cee755c465494fbc6bdff",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b83cee755c465494fbc6bdff",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b83cee755c465494fbc6bdff",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GSwbRf_qSIyA7g8qaxvPRA",
                      "shareUrl": "https://open.spotify.com/album/5avELfEfgOrXmXU8Ofjw2n?si=GSwbRf_qSIyA7g8qaxvPRA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0Q5yXg70PduDW30YhjFAMr",
                    "uri": "spotify:album:0Q5yXg70PduDW30YhjFAMr",
                    "name": "INNA Hits (Remixed by Armageddon Turk)",
                    "type": "EP",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-06-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029b7ea746ddd46d1c0d81de73",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519b7ea746ddd46d1c0d81de73",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739b7ea746ddd46d1c0d81de73",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "egjvtJosSEi-i1mc25mrHg",
                      "shareUrl": "https://open.spotify.com/album/0Q5yXg70PduDW30YhjFAMr?si=egjvtJosSEi-i1mc25mrHg"
                    },
                    "tracks": {
                      "totalCount": 4
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3aD6v38gvpLvrrWvtj7otI",
                    "uri": "spotify:album:3aD6v38gvpLvrrWvtj7otI",
                    "name": "Gimme Gimme (Ness Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-03-14T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022299f1718b98d1f96e2b25a3",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512299f1718b98d1f96e2b25a3",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732299f1718b98d1f96e2b25a3",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "yb8FevaISFmvi_T383IvKQ",
                      "shareUrl": "https://open.spotify.com/album/3aD6v38gvpLvrrWvtj7otI?si=yb8FevaISFmvi_T383IvKQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3PUhRmdioFYRuFoPD11ls0",
                    "uri": "spotify:album:3PUhRmdioFYRuFoPD11ls0",
                    "name": "Gimme Gimme (Andros Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-03-14T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02fd515c049f60be1bc87896e9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851fd515c049f60be1bc87896e9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273fd515c049f60be1bc87896e9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "yIm0787rRPuqzzM34mq9GA",
                      "shareUrl": "https://open.spotify.com/album/3PUhRmdioFYRuFoPD11ls0?si=yIm0787rRPuqzzM34mq9GA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5r4SqFDAVzJ7FZyAo37xxn",
                    "uri": "spotify:album:5r4SqFDAVzJ7FZyAo37xxn",
                    "name": "Hasta la Vista",
                    "type": "SINGLE",
                    "date": {
                      "year": 2017,
                      "isoString": "2017-02-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0260c7a3a88654217418189f17",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485160c7a3a88654217418189f17",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27360c7a3a88654217418189f17",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Lo9XruYoT3uumVEXkleCAg",
                      "shareUrl": "https://open.spotify.com/album/5r4SqFDAVzJ7FZyAo37xxn?si=Lo9XruYoT3uumVEXkleCAg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2RzF0uxGLzL5SFo55pgG4U",
                    "uri": "spotify:album:2RzF0uxGLzL5SFo55pgG4U",
                    "name": "Cum Ar Fi (Pascal Junior Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-11-21T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02fa5c73ce63e3f79822a5a90e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851fa5c73ce63e3f79822a5a90e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273fa5c73ce63e3f79822a5a90e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "GEcSvks-RZCweWyftetWrQ",
                      "shareUrl": "https://open.spotify.com/album/2RzF0uxGLzL5SFo55pgG4U?si=GEcSvks-RZCweWyftetWrQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0pp44LrwCqHh9i5YLeJkZj",
                    "uri": "spotify:album:0pp44LrwCqHh9i5YLeJkZj",
                    "name": "Cum ar fi",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-11-14T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0289e1c29e80594dc2af75a9b1",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485189e1c29e80594dc2af75a9b1",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27389e1c29e80594dc2af75a9b1",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "ehMLM_q-SuWKE6Y5E6hVCw",
                      "shareUrl": "https://open.spotify.com/album/0pp44LrwCqHh9i5YLeJkZj?si=ehMLM_q-SuWKE6Y5E6hVCw"
                    },
                    "tracks": {
                      "totalCount": 6
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6CLFBeQSotMRgbdHLlXofB",
                    "uri": "spotify:album:6CLFBeQSotMRgbdHLlXofB",
                    "name": "Say It with Your Body",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-10-03T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02ded2edc335cf99ad9fbe0423",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851ded2edc335cf99ad9fbe0423",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273ded2edc335cf99ad9fbe0423",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "5hyQN2VPRZi48foKJGTPWw",
                      "shareUrl": "https://open.spotify.com/album/6CLFBeQSotMRgbdHLlXofB?si=5hyQN2VPRZi48foKJGTPWw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5nTdOaxjiWtF5RVekLG6IB",
                    "uri": "spotify:album:5nTdOaxjiWtF5RVekLG6IB",
                    "name": "Heaven (Electric Bodega Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-09-12T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02134e1dd12b0fd2c9bc1b63f5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851134e1dd12b0fd2c9bc1b63f5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273134e1dd12b0fd2c9bc1b63f5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "YKQcrRyMRUiCLt6OGB6K_g",
                      "shareUrl": "https://open.spotify.com/album/5nTdOaxjiWtF5RVekLG6IB?si=YKQcrRyMRUiCLt6OGB6K_g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0w3y38lzQrnd3HaaNZBtuJ",
                    "uri": "spotify:album:0w3y38lzQrnd3HaaNZBtuJ",
                    "name": "Heaven (Smax Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-06-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e020411f93ae3513e700deb1432",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048510411f93ae3513e700deb1432",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2730411f93ae3513e700deb1432",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "8rZnZQzPSae3JJJqzK4nXg",
                      "shareUrl": "https://open.spotify.com/album/0w3y38lzQrnd3HaaNZBtuJ?si=8rZnZQzPSae3JJJqzK4nXg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1wLhCMH6lHA9SEIjvZmySN",
                    "uri": "spotify:album:1wLhCMH6lHA9SEIjvZmySN",
                    "name": "Heaven (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-06-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02120daec6218228e67b20f692",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851120daec6218228e67b20f692",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273120daec6218228e67b20f692",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Ko_7xRVcRF63EHnSkpqsyw",
                      "shareUrl": "https://open.spotify.com/album/1wLhCMH6lHA9SEIjvZmySN?si=Ko_7xRVcRF63EHnSkpqsyw"
                    },
                    "tracks": {
                      "totalCount": 24
                    }
                  },
                  {
                    "id": "3mTfMUFVmydz9KEZTmuF6i",
                    "uri": "spotify:album:3mTfMUFVmydz9KEZTmuF6i",
                    "name": "Heaven (Radio Edit)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-06-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0218e42417f7e262f15b767868",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485118e42417f7e262f15b767868",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27318e42417f7e262f15b767868",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "F08QFwQgQMW-fGexC8donw",
                      "shareUrl": "https://open.spotify.com/album/3mTfMUFVmydz9KEZTmuF6i?si=F08QFwQgQMW-fGexC8donw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2AsLvCaTiwuQxPcxOdCfoA",
                    "uri": "spotify:album:2AsLvCaTiwuQxPcxOdCfoA",
                    "name": "Heaven (Dario Vega Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-06-13T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b0b9edfdc95c7276268f793e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b0b9edfdc95c7276268f793e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b0b9edfdc95c7276268f793e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "nXFsn0XrT_OFnknIaQUCLQ",
                      "shareUrl": "https://open.spotify.com/album/2AsLvCaTiwuQxPcxOdCfoA?si=nXFsn0XrT_OFnknIaQUCLQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4jhLyXVgzTYgBPPBSGm4Qf",
                    "uri": "spotify:album:4jhLyXVgzTYgBPPBSGm4Qf",
                    "name": "Rendez Vous (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-03-24T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02fff45ec905e38ddd9c6873e1",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851fff45ec905e38ddd9c6873e1",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273fff45ec905e38ddd9c6873e1",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "q8rWzmNhRAi6SK63_u5EvA",
                      "shareUrl": "https://open.spotify.com/album/4jhLyXVgzTYgBPPBSGm4Qf?si=q8rWzmNhRAi6SK63_u5EvA"
                    },
                    "tracks": {
                      "totalCount": 8
                    }
                  },
                  {
                    "id": "55GaN4Lfy9XLGJWta3SoGE",
                    "uri": "spotify:album:55GaN4Lfy9XLGJWta3SoGE",
                    "name": "Rendez Vous",
                    "type": "SINGLE",
                    "date": {
                      "year": 2016,
                      "isoString": "2016-02-19T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02d6b9616e761a792c5d22a151",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851d6b9616e761a792c5d22a151",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273d6b9616e761a792c5d22a151",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "s7uF2BIOTVq-0mb_2iurGQ",
                      "shareUrl": "https://open.spotify.com/album/55GaN4Lfy9XLGJWta3SoGE?si=s7uF2BIOTVq-0mb_2iurGQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "70z3qDSsYu33mlsNgNDpAw",
                    "uri": "spotify:album:70z3qDSsYu33mlsNgNDpAw",
                    "name": "Yalla (Remixes)",
                    "type": "EP",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-12-24T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02fadb8b77e6a1aae90b9445e4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851fadb8b77e6a1aae90b9445e4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273fadb8b77e6a1aae90b9445e4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "RnXewyPRQluB-oNCRp-DIw",
                      "shareUrl": "https://open.spotify.com/album/70z3qDSsYu33mlsNgNDpAw?si=RnXewyPRQluB-oNCRp-DIw"
                    },
                    "tracks": {
                      "totalCount": 5
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2OT05NenjJp0bz5SeBmblc",
                    "uri": "spotify:album:2OT05NenjJp0bz5SeBmblc",
                    "name": "Bop Bop (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-12-24T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02cc62449b09359152c903744d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851cc62449b09359152c903744d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273cc62449b09359152c903744d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "rpQ_GcIJRuWQPI7dSwAamw",
                      "shareUrl": "https://open.spotify.com/album/2OT05NenjJp0bz5SeBmblc?si=rpQ_GcIJRuWQPI7dSwAamw"
                    },
                    "tracks": {
                      "totalCount": 8
                    }
                  },
                  {
                    "id": "4lx4cSYhpxcR7NyVL8lrzR",
                    "uri": "spotify:album:4lx4cSYhpxcR7NyVL8lrzR",
                    "name": "Bop Bop",
                    "type": "SINGLE",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-07-30T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0209e9be45e1a84825ce464bcd",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485109e9be45e1a84825ce464bcd",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27309e9be45e1a84825ce464bcd",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "CW7YwiTAQ5W349LPBtuOqg",
                      "shareUrl": "https://open.spotify.com/album/4lx4cSYhpxcR7NyVL8lrzR?si=CW7YwiTAQ5W349LPBtuOqg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0q1Diqp0hfNLbp2lhvvVZQ",
                    "uri": "spotify:album:0q1Diqp0hfNLbp2lhvvVZQ",
                    "name": "Yalla",
                    "type": "SINGLE",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-11-20T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0247370237a755388230a49b4a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485147370237a755388230a49b4a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27347370237a755388230a49b4a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "VQVhrkRgTDabSFasLRx9QQ",
                      "shareUrl": "https://open.spotify.com/album/0q1Diqp0hfNLbp2lhvvVZQ?si=VQVhrkRgTDabSFasLRx9QQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1dgckR0PI6dpwKOx8AZwpI",
                    "uri": "spotify:album:1dgckR0PI6dpwKOx8AZwpI",
                    "name": "Everybody (Mike Candys Remix)",
                    "type": "EP",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-08-07T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e2aebd228f5f359b58b38075",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e2aebd228f5f359b58b38075",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e2aebd228f5f359b58b38075",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "iwex0V__QICGVi2P2qOmlA",
                      "shareUrl": "https://open.spotify.com/album/1dgckR0PI6dpwKOx8AZwpI?si=iwex0V__QICGVi2P2qOmlA"
                    },
                    "tracks": {
                      "totalCount": 4
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3ZYxPQzdPQIyAGQWf0H7BF",
                    "uri": "spotify:album:3ZYxPQzdPQIyAGQWf0H7BF",
                    "name": "We Wanna",
                    "type": "SINGLE",
                    "date": {
                      "year": 2015,
                      "isoString": "2015-06-09T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0244d09645cac7e922028ef0e3",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485144d09645cac7e922028ef0e3",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27344d09645cac7e922028ef0e3",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "QiPAxGd7SZ2_tA8NPZ1kTA",
                      "shareUrl": "https://open.spotify.com/album/3ZYxPQzdPQIyAGQWf0H7BF?si=QiPAxGd7SZ2_tA8NPZ1kTA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "2F3CYuFg2zgENPplV2tKcn",
                    "uri": "spotify:album:2F3CYuFg2zgENPplV2tKcn",
                    "name": "Diggy Down",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-12-03T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0213919f06dec47905a46ab906",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485113919f06dec47905a46ab906",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27313919f06dec47905a46ab906",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "sckCjgiQTHSVf8s2HU5bGQ",
                      "shareUrl": "https://open.spotify.com/album/2F3CYuFg2zgENPplV2tKcn?si=sckCjgiQTHSVf8s2HU5bGQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0LmEG3bIDEk1cpW0ckMOIn",
                    "uri": "spotify:album:0LmEG3bIDEk1cpW0ckMOIn",
                    "name": "Take Me Higher",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-09-16T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02496a25630d6484ac78b98738",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851496a25630d6484ac78b98738",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273496a25630d6484ac78b98738",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "kCfkkRDlQ56lO9hVnVLEaA",
                      "shareUrl": "https://open.spotify.com/album/0LmEG3bIDEk1cpW0ckMOIn?si=kCfkkRDlQ56lO9hVnVLEaA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "7zY7XHPgFLYyfOj1nG0peV",
                    "uri": "spotify:album:7zY7XHPgFLYyfOj1nG0peV",
                    "name": "Cola Song (feat. J Balvin)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-09-02T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c3b3eb37e671dc1b52724f18",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c3b3eb37e671dc1b52724f18",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c3b3eb37e671dc1b52724f18",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "i8Rp_oWiR4qUAma54bEaZg",
                      "shareUrl": "https://open.spotify.com/album/7zY7XHPgFLYyfOj1nG0peV?si=i8Rp_oWiR4qUAma54bEaZg"
                    },
                    "tracks": {
                      "totalCount": 4
                    }
                  },
                  {
                    "id": "3153stlyNnwZT5tDZY6bZL",
                    "uri": "spotify:album:3153stlyNnwZT5tDZY6bZL",
                    "name": "Cola Song (feat. J Balvin)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-04-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023a35e5d94f6cc67f4442e0a7",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513a35e5d94f6cc67f4442e0a7",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733a35e5d94f6cc67f4442e0a7",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "2QVCiO8tSvedzFYmZ52x_g",
                      "shareUrl": "https://open.spotify.com/album/3153stlyNnwZT5tDZY6bZL?si=2QVCiO8tSvedzFYmZ52x_g"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "1MiqNzBTyRXLH4QMbJRkj9",
                    "uri": "spotify:album:1MiqNzBTyRXLH4QMbJRkj9",
                    "name": "Good Time (feat. Pitbull)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-07-15T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024c5da700ff7b6fce06b387df",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514c5da700ff7b6fce06b387df",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734c5da700ff7b6fce06b387df",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Ji0vYF9gShWvXhatlo9FDw",
                      "shareUrl": "https://open.spotify.com/album/1MiqNzBTyRXLH4QMbJRkj9?si=Ji0vYF9gShWvXhatlo9FDw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "63fPelNjpoX8DOm2O7Haud",
                    "uri": "spotify:album:63fPelNjpoX8DOm2O7Haud",
                    "name": "Summer Days",
                    "type": "SINGLE",
                    "date": {
                      "year": 2014,
                      "isoString": "2014-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02782f28dfcc953541a9491627",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851782f28dfcc953541a9491627",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273782f28dfcc953541a9491627",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "Yaj3gPcsQ5WqBYgwLfuEig",
                      "shareUrl": "https://open.spotify.com/album/63fPelNjpoX8DOm2O7Haud?si=Yaj3gPcsQ5WqBYgwLfuEig"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6qggRuPkgmN2b8Yk9XHF27",
                    "uri": "spotify:album:6qggRuPkgmN2b8Yk9XHF27",
                    "name": "In Your Eyes",
                    "type": "SINGLE",
                    "date": {
                      "year": 2013,
                      "isoString": "2013-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0236545cd74dbe9cd9e85fd12a",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485136545cd74dbe9cd9e85fd12a",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27336545cd74dbe9cd9e85fd12a",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "nXbZXuvPQf21KBlFMUUz-w",
                      "shareUrl": "https://open.spotify.com/album/6qggRuPkgmN2b8Yk9XHF27?si=nXbZXuvPQf21KBlFMUUz-w"
                    },
                    "tracks": {
                      "totalCount": 2
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "3D8B1MgaX4LNZqYIiu7i87",
                    "uri": "spotify:album:3D8B1MgaX4LNZqYIiu7i87",
                    "name": "Caliente",
                    "type": "SINGLE",
                    "date": {
                      "year": 2012,
                      "isoString": "2012-07-19T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e8f8953d1677d3706afa002c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e8f8953d1677d3706afa002c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e8f8953d1677d3706afa002c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "A_vmmBM9T0CYyOz6HG9Tlg",
                      "shareUrl": "https://open.spotify.com/album/3D8B1MgaX4LNZqYIiu7i87?si=A_vmmBM9T0CYyOz6HG9Tlg"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "4zU4xquXXCkZ6WOTPukHTF",
                    "uri": "spotify:album:4zU4xquXXCkZ6WOTPukHTF",
                    "name": "Tu si eu",
                    "type": "SINGLE",
                    "date": {
                      "year": 2012,
                      "isoString": "2012-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f925ad52711ca57a32a02856",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f925ad52711ca57a32a02856",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f925ad52711ca57a32a02856",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "htoPYcUIRrWM4F0YUrJ7nw",
                      "shareUrl": "https://open.spotify.com/album/4zU4xquXXCkZ6WOTPukHTF?si=htoPYcUIRrWM4F0YUrJ7nw"
                    },
                    "tracks": {
                      "totalCount": 2
                    }
                  },
                  {
                    "id": "5WfNhiFmN6i3jDgRtqlYy4",
                    "uri": "spotify:album:5WfNhiFmN6i3jDgRtqlYy4",
                    "name": "Tu si eu (Radio Edit)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2012,
                      "isoString": "2012-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0236648e802ac5b0b047bcedb8",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485136648e802ac5b0b047bcedb8",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27336648e802ac5b0b047bcedb8",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "FZzi1hkTSAmrtqNerzjfiw",
                      "shareUrl": "https://open.spotify.com/album/5WfNhiFmN6i3jDgRtqlYy4?si=FZzi1hkTSAmrtqNerzjfiw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "5tnPjusV6KPHtFAIb4I02c",
                    "uri": "spotify:album:5tnPjusV6KPHtFAIb4I02c",
                    "name": "Caliente (Remixes)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2012,
                      "isoString": "2012-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02cfe1bbcbdb5cb65d20ad8bb3",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851cfe1bbcbdb5cb65d20ad8bb3",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273cfe1bbcbdb5cb65d20ad8bb3",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "cNSX3dkvQiK7hH3J907J-Q",
                      "shareUrl": "https://open.spotify.com/album/5tnPjusV6KPHtFAIb4I02c?si=cNSX3dkvQiK7hH3J907J-Q"
                    },
                    "tracks": {
                      "totalCount": 4
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "6mR6Mxl6sIGPBtPoekAytH",
                    "uri": "spotify:album:6mR6Mxl6sIGPBtPoekAytH",
                    "name": "Un Momento",
                    "type": "SINGLE",
                    "date": {
                      "year": 2011,
                      "isoString": "2011-11-22T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028939b528d5af5d5e7784533e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518939b528d5af5d5e7784533e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738939b528d5af5d5e7784533e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "OaVzOM03Tb6aUXmS3De1aA",
                      "shareUrl": "https://open.spotify.com/album/6mR6Mxl6sIGPBtPoekAytH?si=OaVzOM03Tb6aUXmS3De1aA"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "0py3FiA4iTrOq6CZ67VjRv",
                    "uri": "spotify:album:0py3FiA4iTrOq6CZ67VjRv",
                    "name": "Wow",
                    "type": "SINGLE",
                    "date": {
                      "year": 2011,
                      "isoString": "2011-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0210d5c36121482f0c628eeeb3",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485110d5c36121482f0c628eeeb3",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27310d5c36121482f0c628eeeb3",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "TlSAdfCUR2eOhI4xccs1Tw",
                      "shareUrl": "https://open.spotify.com/album/0py3FiA4iTrOq6CZ67VjRv?si=TlSAdfCUR2eOhI4xccs1Tw"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "items": [
                  {
                    "id": "249BI3YVLl3afeZxQOgGRW",
                    "uri": "spotify:album:249BI3YVLl3afeZxQOgGRW",
                    "name": "Endless (Victor Magan Remix)",
                    "type": "SINGLE",
                    "date": {
                      "year": 2011,
                      "isoString": "2011-01-01T00:00:00Z"
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b3f275731c442eaa97efe26c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b3f275731c442eaa97efe26c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b3f275731c442eaa97efe26c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "playability": {
                      "playable": true,
                      "reason": "PLAYABLE"
                    },
                    "sharingInfo": {
                      "shareId": "jvx7-PHPTRKJUKsqxyy7QQ",
                      "shareUrl": "https://open.spotify.com/album/249BI3YVLl3afeZxQOgGRW?si=jvx7-PHPTRKJUKsqxyy7QQ"
                    },
                    "tracks": {
                      "totalCount": 1
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```





## Artist Appears On

Retrieves albums and tracks where the artist appears as a featured artist.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/artist_appears_on/?id=2w9zwq3AktTeYYMuhMjju8", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "data": {
    "artist": {
      "id": "2w9zwq3AktTeYYMuhMjju8",
      "uri": "spotify:artist:2w9zwq3AktTeYYMuhMjju8",
      "profile": {
        "name": "INNA"
      },
      "relatedContent": {
        "appearsOn": {
          "totalCount": 89,
          "items": [
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2qQf72CQ3j5D9AEwvmGvdX",
                    "id": "2qQf72CQ3j5D9AEwvmGvdX",
                    "name": "Sunrise",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:20gsENnposVs2I4rQ5kvrf",
                          "profile": {
                            "name": "Sam Feldt"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0201288d5dc8b701031d97a0d7",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485101288d5dc8b701031d97a0d7",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27301288d5dc8b701031d97a0d7",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "GJlr9JcPTdCBj6jp-0TsFg",
                      "shareUrl": "https://open.spotify.com/album/2qQf72CQ3j5D9AEwvmGvdX?si=GJlr9JcPTdCBj6jp-0TsFg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4QyylR4pPcWRpp3U2gkPcd",
                    "id": "4QyylR4pPcWRpp3U2gkPcd",
                    "name": "Sunrise To Sunset",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:20gsENnposVs2I4rQ5kvrf",
                          "profile": {
                            "name": "Sam Feldt"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0209345bdc4fa847fb5e5898cc",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485109345bdc4fa847fb5e5898cc",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27309345bdc4fa847fb5e5898cc",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "i5fUDbzQQamO3E_6FsQVHA",
                      "shareUrl": "https://open.spotify.com/album/4QyylR4pPcWRpp3U2gkPcd?si=i5fUDbzQQamO3E_6FsQVHA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:66cSCYHzE9eWbgtICJ7ceI",
                    "id": "66cSCYHzE9eWbgtICJ7ceI",
                    "name": "Annual 2021",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0NGAZxHanS9e0iNHpR8f2W",
                          "profile": {
                            "name": "Alok"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b495cce6a4628c518b67adc4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b495cce6a4628c518b67adc4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b495cce6a4628c518b67adc4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "vqDqLMNNTkKpSRPD4FFEvw",
                      "shareUrl": "https://open.spotify.com/album/66cSCYHzE9eWbgtICJ7ceI?si=vqDqLMNNTkKpSRPD4FFEvw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:209j2TtzIAQHRxoBgeoqUM",
                    "id": "209j2TtzIAQHRxoBgeoqUM",
                    "name": "Reloaded",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:14dmbYen0AciYxu5n4Fkpd",
                          "profile": {
                            "name": "DJ BoBo"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025e31e1be55fa05cc9651ce07",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515e31e1be55fa05cc9651ce07",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735e31e1be55fa05cc9651ce07",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "t7O9xuPJR7SLTVs-UtUZ-Q",
                      "shareUrl": "https://open.spotify.com/album/209j2TtzIAQHRxoBgeoqUM?si=t7O9xuPJR7SLTVs-UtUZ-Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:17nkMuRLEPUTt9xt3gQOgy",
                    "id": "17nkMuRLEPUTt9xt3gQOgy",
                    "name": "Antiexemplu",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1n5LD9Ar3D6RK2X2ewGvXb",
                          "profile": {
                            "name": "Carla's Dreams"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028cb919b4f26d3a0d663fd6a0",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518cb919b4f26d3a0d663fd6a0",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738cb919b4f26d3a0d663fd6a0",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "boE_Tm3HQyOTRw_FOlieBA",
                      "shareUrl": "https://open.spotify.com/album/17nkMuRLEPUTt9xt3gQOgy?si=boE_Tm3HQyOTRw_FOlieBA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 2,
                "items": [
                  {
                    "uri": "spotify:album:17B9ZB9opgRGcvN4Svc2si",
                    "id": "17B9ZB9opgRGcvN4Svc2si",
                    "name": "Never Dies",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e022a4f7e877e5755965064961b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048512a4f7e877e5755965064961b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2732a4f7e877e5755965064961b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "YcH_SJR9RAG3HpxIDwYztg",
                      "shareUrl": "https://open.spotify.com/album/17B9ZB9opgRGcvN4Svc2si?si=YcH_SJR9RAG3HpxIDwYztg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:77G3b0NefwZSiYhuSMGIpu",
                    "id": "77G3b0NefwZSiYhuSMGIpu",
                    "name": "Best Dance Hits Ever - Top 50",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b819c668dcc0b22c6fdef4d2",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b819c668dcc0b22c6fdef4d2",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b819c668dcc0b22c6fdef4d2",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "4tXAANlhTu-wx19ApZyFkA",
                      "shareUrl": "https://open.spotify.com/album/77G3b0NefwZSiYhuSMGIpu?si=4tXAANlhTu-wx19ApZyFkA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2knRps90HKMGWoVRxgpvXJ",
                    "id": "2knRps90HKMGWoVRxgpvXJ",
                    "name": "My Gorgeous Drama Queens",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:05qpk4JDcLSFNJSsPIZ8Ye",
                          "profile": {
                            "name": "The Motans"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c577e39bde79b41129b7acea",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c577e39bde79b41129b7acea",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c577e39bde79b41129b7acea",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "RVAJBbXeSnqpn1CeQH8YKQ",
                      "shareUrl": "https://open.spotify.com/album/2knRps90HKMGWoVRxgpvXJ?si=RVAJBbXeSnqpn1CeQH8YKQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3z7A1LFhxzmOGwTZtSWQ1D",
                    "id": "3z7A1LFhxzmOGwTZtSWQ1D",
                    "name": "Ngoc",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1n5LD9Ar3D6RK2X2ewGvXb",
                          "profile": {
                            "name": "Carla's Dreams"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02213d9424796690df42271d6b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851213d9424796690df42271d6b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273213d9424796690df42271d6b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "wzawKsFNQVW1KgaJi-ce9A",
                      "shareUrl": "https://open.spotify.com/album/3z7A1LFhxzmOGwTZtSWQ1D?si=wzawKsFNQVW1KgaJi-ce9A"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0XgKWgSVOG0BLFvROk3AVg",
                    "id": "0XgKWgSVOG0BLFvROk3AVg",
                    "name": "DJ Central Groove Vol, 3",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02da120b23e980081c9354e3fb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851da120b23e980081c9354e3fb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273da120b23e980081c9354e3fb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "eB2gQeqSQvSGDykyPpz0Sw",
                      "shareUrl": "https://open.spotify.com/album/0XgKWgSVOG0BLFvROk3AVg?si=eB2gQeqSQvSGDykyPpz0Sw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6RoGYmxUOIzCDxK7P7P46H",
                    "id": "6RoGYmxUOIzCDxK7P7P46H",
                    "name": "Sober",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6tqRPlUavLUI398ZRw7M6e",
                          "profile": {
                            "name": "yeanix"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027c7c44dd3dacdeedd1f532df",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517c7c44dd3dacdeedd1f532df",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737c7c44dd3dacdeedd1f532df",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "3sSJ60KeTBu8WxFrAGzJUA",
                      "shareUrl": "https://open.spotify.com/album/6RoGYmxUOIzCDxK7P7P46H?si=3sSJ60KeTBu8WxFrAGzJUA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4SIpuXhPR2PhE2H1tU75QM",
                    "id": "4SIpuXhPR2PhE2H1tU75QM",
                    "name": "Supervara 2009",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a395a93d8a438e46e914caeb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a395a93d8a438e46e914caeb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a395a93d8a438e46e914caeb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "1Du2EZyfRM2ECwB5mwJWyg",
                      "shareUrl": "https://open.spotify.com/album/4SIpuXhPR2PhE2H1tU75QM?si=1Du2EZyfRM2ECwB5mwJWyg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 2,
                "items": [
                  {
                    "uri": "spotify:album:0Dufuv6lYFks1aX0GqXfk5",
                    "id": "0Dufuv6lYFks1aX0GqXfk5",
                    "name": "Mai Stai",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0niQ4Q9nI1Qh0BHpT3b4NC",
                          "profile": {
                            "name": "3 Sud Est"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0205a9ab49a99e1940242c4e0e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485105a9ab49a99e1940242c4e0e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27305a9ab49a99e1940242c4e0e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "5Sh_8O2wQhWpWMU_Z8WU5Q",
                      "shareUrl": "https://open.spotify.com/album/0Dufuv6lYFks1aX0GqXfk5?si=5Sh_8O2wQhWpWMU_Z8WU5Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0qsCsajava06qxa5apReib",
                    "id": "0qsCsajava06qxa5apReib",
                    "name": "Reina Istanbul, Vol. 7",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:2K15nwVhvJnIsg6fcfGiSi",
                          "profile": {
                            "name": "Ufuk Akyıldız"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0248d542e04d87ea970ed6f65b",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485148d542e04d87ea970ed6f65b",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27348d542e04d87ea970ed6f65b",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "JeyXJGpxRrm30QEq3yGOVQ",
                      "shareUrl": "https://open.spotify.com/album/0qsCsajava06qxa5apReib?si=JeyXJGpxRrm30QEq3yGOVQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3pcIJIuMpyw7L2fxGETbzk",
                    "id": "3pcIJIuMpyw7L2fxGETbzk",
                    "name": "Baila Conmigo",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0224806be3b400cc478731bfbe",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485124806be3b400cc478731bfbe",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27324806be3b400cc478731bfbe",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "9g7_guLqS2aDJewxeDjtFQ",
                      "shareUrl": "https://open.spotify.com/album/3pcIJIuMpyw7L2fxGETbzk?si=9g7_guLqS2aDJewxeDjtFQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0URMeyN2XosmGKgsibzLuj",
                    "id": "0URMeyN2XosmGKgsibzLuj",
                    "name": "Party Anthems",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027fb0863939fd706bbd4b2494",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517fb0863939fd706bbd4b2494",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737fb0863939fd706bbd4b2494",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "0v66K98NRFCt_c0Ql2gDdQ",
                      "shareUrl": "https://open.spotify.com/album/0URMeyN2XosmGKgsibzLuj?si=0v66K98NRFCt_c0Ql2gDdQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6dCJAD121RDSJ4xrTGewlA",
                    "id": "6dCJAD121RDSJ4xrTGewlA",
                    "name": "Supervara 2009",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c036c933aa73e5aaa7e88272",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c036c933aa73e5aaa7e88272",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c036c933aa73e5aaa7e88272",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "JY2KqtXBTjiKsNZTp2u9SQ",
                      "shareUrl": "https://open.spotify.com/album/6dCJAD121RDSJ4xrTGewlA?si=JY2KqtXBTjiKsNZTp2u9SQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4KDupOYFdmHY0buIQ3w7o7",
                    "id": "4KDupOYFdmHY0buIQ3w7o7",
                    "name": "Home Workout Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0220fb03705b6651066b91e31f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485120fb03705b6651066b91e31f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27320fb03705b6651066b91e31f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "2SAAv7UOR3uZvo1oxYjZIA",
                      "shareUrl": "https://open.spotify.com/album/4KDupOYFdmHY0buIQ3w7o7?si=2SAAv7UOR3uZvo1oxYjZIA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4VgO2rhcyq3Un1gMkg9oJM",
                    "id": "4VgO2rhcyq3Un1gMkg9oJM",
                    "name": "Masquerade Club Istanbul",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:2c9zUiLbT2bm0DPsAbqLzt",
                          "profile": {
                            "name": "Cihat Ugurel"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0294e467b2d6c46d1f3dc41f43",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485194e467b2d6c46d1f3dc41f43",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27394e467b2d6c46d1f3dc41f43",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "nGcuNC-aQvmXY7PxfgRHAg",
                      "shareUrl": "https://open.spotify.com/album/4VgO2rhcyq3Un1gMkg9oJM?si=nGcuNC-aQvmXY7PxfgRHAg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:1Fzq2n9s3YHDajNdQOCOQS",
                    "id": "1Fzq2n9s3YHDajNdQOCOQS",
                    "name": "Can't Get You Out Of My Head Vol. 001",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0NGAZxHanS9e0iNHpR8f2W",
                          "profile": {
                            "name": "Alok"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b0600d2d2af8b00605e022cb",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b0600d2d2af8b00605e022cb",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b0600d2d2af8b00605e022cb",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "F8AEzBFpRwGF3A-yRVXamg",
                      "shareUrl": "https://open.spotify.com/album/1Fzq2n9s3YHDajNdQOCOQS?si=F8AEzBFpRwGF3A-yRVXamg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6m5P0s0ku0wmYjIouBSl1b",
                    "id": "6m5P0s0ku0wmYjIouBSl1b",
                    "name": "Romania Loves the Minimal Beat",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027035255a16f136cbfbf2ac4f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517035255a16f136cbfbf2ac4f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737035255a16f136cbfbf2ac4f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "oXjEBK-SQVuKidi8P032xw",
                      "shareUrl": "https://open.spotify.com/album/6m5P0s0ku0wmYjIouBSl1b?si=oXjEBK-SQVuKidi8P032xw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2YdCfC3dXGQFMNU7OQNIWE",
                    "id": "2YdCfC3dXGQFMNU7OQNIWE",
                    "name": "NR1 Hits 2019 (Special Edition)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0SrNAaJaF8RVQMYbJnwqBJ",
                          "profile": {
                            "name": "Mert Hakan"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027b23747a4261f7c8cbc41c93",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517b23747a4261f7c8cbc41c93",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737b23747a4261f7c8cbc41c93",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "uaMVSqutRoWaQbxt_Yiq9g",
                      "shareUrl": "https://open.spotify.com/album/2YdCfC3dXGQFMNU7OQNIWE?si=uaMVSqutRoWaQbxt_Yiq9g"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5ZQ8lelTkJfwcubKRZrNhX",
                    "id": "5ZQ8lelTkJfwcubKRZrNhX",
                    "name": "Never Dies (The Remixes)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:47z7ZrgFoBvVpCnElCE3Zh",
                          "profile": {
                            "name": "Yellow Claw"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02330218e7107742b2072d00ff",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851330218e7107742b2072d00ff",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273330218e7107742b2072d00ff",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "BtjI2bYHRNGI3HbTGwpztw",
                      "shareUrl": "https://open.spotify.com/album/5ZQ8lelTkJfwcubKRZrNhX?si=BtjI2bYHRNGI3HbTGwpztw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3YxMlVTToT0qu0ReWUQKWn",
                    "id": "3YxMlVTToT0qu0ReWUQKWn",
                    "name": "Amazing Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1omKDrKCcMD79tfK8Vb2Hr",
                          "profile": {
                            "name": "Connect-R"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a903b1cdab9f00c4c5c26603",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a903b1cdab9f00c4c5c26603",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a903b1cdab9f00c4c5c26603",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "-GmlC2pUS_OrLzXC8W0f-w",
                      "shareUrl": "https://open.spotify.com/album/3YxMlVTToT0qu0ReWUQKWn?si=-GmlC2pUS_OrLzXC8W0f-w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2tbufAIPiFlgg3bKp6zzRw",
                    "id": "2tbufAIPiFlgg3bKp6zzRw",
                    "name": "Music Non Stop Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028717741457cdfca25a136cb4",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518717741457cdfca25a136cb4",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738717741457cdfca25a136cb4",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "MIKqdpHWQXWl9J3ucesjSQ",
                      "shareUrl": "https://open.spotify.com/album/2tbufAIPiFlgg3bKp6zzRw?si=MIKqdpHWQXWl9J3ucesjSQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3rgrMDKCWu1hLnMVv9BJiE",
                    "id": "3rgrMDKCWu1hLnMVv9BJiE",
                    "name": "All The Hits 2017",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e027b4758a52ca5e4c84c01ef56",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048517b4758a52ca5e4c84c01ef56",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2737b4758a52ca5e4c84c01ef56",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "0oz9EtqvTva1qqkTnaHwMg",
                      "shareUrl": "https://open.spotify.com/album/3rgrMDKCWu1hLnMVv9BJiE?si=0oz9EtqvTva1qqkTnaHwMg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2n4R0ceMjfqPBgwhdQ0MYJ",
                    "id": "2n4R0ceMjfqPBgwhdQ0MYJ",
                    "name": "Music Non Stop Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f0e68990d144c09eeb7b697e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f0e68990d144c09eeb7b697e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f0e68990d144c09eeb7b697e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "uGUnoZ3nTu2w6CI7rKu2Cw",
                      "shareUrl": "https://open.spotify.com/album/2n4R0ceMjfqPBgwhdQ0MYJ?si=uGUnoZ3nTu2w6CI7rKu2Cw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5lhpCkp46sHTWx7FN3zkwz",
                    "id": "5lhpCkp46sHTWx7FN3zkwz",
                    "name": "Pretty Thoughts (Jean Juan Remix)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02a93255b12dfa8ada534a1d28",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851a93255b12dfa8ada534a1d28",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273a93255b12dfa8ada534a1d28",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "oFgS_6Z3RYGXVZc4jAAC4w",
                      "shareUrl": "https://open.spotify.com/album/5lhpCkp46sHTWx7FN3zkwz?si=oFgS_6Z3RYGXVZc4jAAC4w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6JQZ6mBMYRGR9RQVCRTWNS",
                    "id": "6JQZ6mBMYRGR9RQVCRTWNS",
                    "name": "Declaratie De Dragoste Vol. 6 (I Love You)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02c9a0689fa468e49cb3e02bbe",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851c9a0689fa468e49cb3e02bbe",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273c9a0689fa468e49cb3e02bbe",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "0432tbgCTl6F7j1B5b7ORg",
                      "shareUrl": "https://open.spotify.com/album/6JQZ6mBMYRGR9RQVCRTWNS?si=0432tbgCTl6F7j1B5b7ORg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4pFSLuMPTMIG08VcDyVYLW",
                    "id": "4pFSLuMPTMIG08VcDyVYLW",
                    "name": "Amazing Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02d041b39ca21c1ef3b0a815af",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851d041b39ca21c1ef3b0a815af",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273d041b39ca21c1ef3b0a815af",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "J-KniJlHSfCNVKeIsuUyiw",
                      "shareUrl": "https://open.spotify.com/album/4pFSLuMPTMIG08VcDyVYLW?si=J-KniJlHSfCNVKeIsuUyiw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:0mieUHsgXataLzOx3TqbVh",
                    "id": "0mieUHsgXataLzOx3TqbVh",
                    "name": "Just Dance 3",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f33a43ee55f928012368d66c",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f33a43ee55f928012368d66c",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f33a43ee55f928012368d66c",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "ur8jetkETIKQEtUnKgYzRg",
                      "shareUrl": "https://open.spotify.com/album/0mieUHsgXataLzOx3TqbVh?si=ur8jetkETIKQEtUnKgYzRg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2fKUuHJGZ2MpdNXGKAGs3p",
                    "id": "2fKUuHJGZ2MpdNXGKAGs3p",
                    "name": "Музыка для тренировок и фитнеса",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e028138ea28e4bcd40a90ea9958",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048518138ea28e4bcd40a90ea9958",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2738138ea28e4bcd40a90ea9958",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "cPjLdBGsRBC1ZGN1_FnX7Q",
                      "shareUrl": "https://open.spotify.com/album/2fKUuHJGZ2MpdNXGKAGs3p?si=cPjLdBGsRBC1ZGN1_FnX7Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6RjKlmcnWNBdiYqkT4pegw",
                    "id": "6RjKlmcnWNBdiYqkT4pegw",
                    "name": "Heaven",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6tqRPlUavLUI398ZRw7M6e",
                          "profile": {
                            "name": "yeanix"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e321d1aa8a96f08478e016a5",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e321d1aa8a96f08478e016a5",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e321d1aa8a96f08478e016a5",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "nbgIJOKrS5Wpk7YroxDIUg",
                      "shareUrl": "https://open.spotify.com/album/6RjKlmcnWNBdiYqkT4pegw?si=nbgIJOKrS5Wpk7YroxDIUg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:58BsZ8mCJFe5WqkzjAp9fm",
                    "id": "58BsZ8mCJFe5WqkzjAp9fm",
                    "name": "Summer In December",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1oiZoULxUJDYGOKMgVefP4",
                          "profile": {
                            "name": "Morandi"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025eb4669f0ffa7cfa33afbe72",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515eb4669f0ffa7cfa33afbe72",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735eb4669f0ffa7cfa33afbe72",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "w_HBnbzcSuCdolApGsWSvA",
                      "shareUrl": "https://open.spotify.com/album/58BsZ8mCJFe5WqkzjAp9fm?si=w_HBnbzcSuCdolApGsWSvA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5JNCNkEaTQZ1143ZmSXp8Y",
                    "id": "5JNCNkEaTQZ1143ZmSXp8Y",
                    "name": "Istanbul Party Night",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023ebc1a5ed43ddc9fd649dd33",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513ebc1a5ed43ddc9fd649dd33",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733ebc1a5ed43ddc9fd649dd33",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "04u4ZQUKTkqXhkk0lYokTw",
                      "shareUrl": "https://open.spotify.com/album/5JNCNkEaTQZ1143ZmSXp8Y?si=04u4ZQUKTkqXhkk0lYokTw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:628ZjvbKY81unpsn9yGoVX",
                    "id": "628ZjvbKY81unpsn9yGoVX",
                    "name": "Declaratie De Dragoste Vol. 6 (I Love You)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02e3376729d46194218cd81a77",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851e3376729d46194218cd81a77",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273e3376729d46194218cd81a77",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "LPy4WR6ISU2Ga3xw797gDA",
                      "shareUrl": "https://open.spotify.com/album/628ZjvbKY81unpsn9yGoVX?si=LPy4WR6ISU2Ga3xw797gDA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5360U9j5P8feL2QIi8D2Mk",
                    "id": "5360U9j5P8feL2QIi8D2Mk",
                    "name": "No Help",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6p1Ylc4wEo82ZBH2x8uMsg",
                          "profile": {
                            "name": "Loxic"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e0288d44279bbbb019cc0651f95",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000485188d44279bbbb019cc0651f95",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b27388d44279bbbb019cc0651f95",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "5mZr8NusRUisgmoZenHaMw",
                      "shareUrl": "https://open.spotify.com/album/5360U9j5P8feL2QIi8D2Mk?si=5mZr8NusRUisgmoZenHaMw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:64FOKKm6B0hwtK5Wid8kaN",
                    "id": "64FOKKm6B0hwtK5Wid8kaN",
                    "name": "Ethnic Electronic Dance Party",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02759e1d586388b5ca130dbc9d",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851759e1d586388b5ca130dbc9d",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273759e1d586388b5ca130dbc9d",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "nEvzwqceTXyWlGEolpkfZA",
                      "shareUrl": "https://open.spotify.com/album/64FOKKm6B0hwtK5Wid8kaN?si=nEvzwqceTXyWlGEolpkfZA"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:2fTPL12rFhmWDrDBYCEyzK",
                    "id": "2fTPL12rFhmWDrDBYCEyzK",
                    "name": "Pop Star, The Album",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6hKA4fRHqmcL8WYEmJfCaY",
                          "profile": {
                            "name": "Brian Cross"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e025fc0797d0a9d40292a4e40e9",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048515fc0797d0a9d40292a4e40e9",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2735fc0797d0a9d40292a4e40e9",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "tFiVemITSP-OPv9CBRu86Q",
                      "shareUrl": "https://open.spotify.com/album/2fTPL12rFhmWDrDBYCEyzK?si=tFiVemITSP-OPv9CBRu86Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:3aXVTZ29s79xq1v0Mu7TAb",
                    "id": "3aXVTZ29s79xq1v0Mu7TAb",
                    "name": "Alesta (All New Hit Singles)",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0BmLNz4nSLfoWYW1cYsElL",
                          "profile": {
                            "name": "Alexandra Stan"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e024e6579a23b9c4521a551295f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048514e6579a23b9c4521a551295f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2734e6579a23b9c4521a551295f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "Vg2OKuS7SneOuz6nyu6g_w",
                      "shareUrl": "https://open.spotify.com/album/3aXVTZ29s79xq1v0Mu7TAb?si=Vg2OKuS7SneOuz6nyu6g_w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4Xi7OvKSQfOm63HXFKrjVr",
                    "id": "4Xi7OvKSQfOm63HXFKrjVr",
                    "name": "Metro Fm Dance Hits 2016",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b7301e4f0460aa19ef38d9b8",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b7301e4f0460aa19ef38d9b8",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b7301e4f0460aa19ef38d9b8",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "XsNWNJTCRgiw6LDC6EE0Ng",
                      "shareUrl": "https://open.spotify.com/album/4Xi7OvKSQfOm63HXFKrjVr?si=XsNWNJTCRgiw6LDC6EE0Ng"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 2,
                "items": [
                  {
                    "uri": "spotify:album:1BLdgA7RV3psnshSAwlpax",
                    "id": "1BLdgA7RV3psnshSAwlpax",
                    "name": "Tu Si Eu",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:1n5LD9Ar3D6RK2X2ewGvXb",
                          "profile": {
                            "name": "Carla's Dreams"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f20518349ca2aeb77cac9901",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f20518349ca2aeb77cac9901",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f20518349ca2aeb77cac9901",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "gxrLyRmnQPm6PKQh1cv-tQ",
                      "shareUrl": "https://open.spotify.com/album/1BLdgA7RV3psnshSAwlpax?si=gxrLyRmnQPm6PKQh1cv-tQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6wUuR0PAzIbD8Su4AGW5qH",
                    "id": "6wUuR0PAzIbD8Su4AGW5qH",
                    "name": "NR1 Summer Hits 2016",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02eef937a4eabb506d40150c7f",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851eef937a4eabb506d40150c7f",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273eef937a4eabb506d40150c7f",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "7AO0kBetTKmqfAvQ7GfaxQ",
                      "shareUrl": "https://open.spotify.com/album/6wUuR0PAzIbD8Su4AGW5qH?si=7AO0kBetTKmqfAvQ7GfaxQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:7aDmHqyRrT4u5e6Q2hPZrk",
                    "id": "7aDmHqyRrT4u5e6Q2hPZrk",
                    "name": "Nr1 Dance Hits 2014",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02f09cb904a62c3c8cad3a2f8e",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851f09cb904a62c3c8cad3a2f8e",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273f09cb904a62c3c8cad3a2f8e",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "sJa_Y7gsRM61kMJu6znRHg",
                      "shareUrl": "https://open.spotify.com/album/7aDmHqyRrT4u5e6Q2hPZrk?si=sJa_Y7gsRM61kMJu6znRHg"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:1n9h2BwMms4Ns71Z9cPkvq",
                    "id": "1n9h2BwMms4Ns71Z9cPkvq",
                    "name": "SPECIAL HITS by Yeni Dünya Müzik",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b6217188b65c83b16158fb99",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b6217188b65c83b16158fb99",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b6217188b65c83b16158fb99",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "lHROm5OtQZ2tMLDEpZX22Q",
                      "shareUrl": "https://open.spotify.com/album/1n9h2BwMms4Ns71Z9cPkvq?si=lHROm5OtQZ2tMLDEpZX22Q"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5wDdbOq0qu5IoY9x1bXsMf",
                    "id": "5wDdbOq0qu5IoY9x1bXsMf",
                    "name": "Gimme Gimme",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:6tqRPlUavLUI398ZRw7M6e",
                          "profile": {
                            "name": "yeanix"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b549f31f8d3cba9fc6665723",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b549f31f8d3cba9fc6665723",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b549f31f8d3cba9fc6665723",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "kZ0FGNhXQ7mgYH5Ik4318w",
                      "shareUrl": "https://open.spotify.com/album/5wDdbOq0qu5IoY9x1bXsMf?si=kZ0FGNhXQ7mgYH5Ik4318w"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:5droCbtu6i8RlbSyY2zPij",
                    "id": "5droCbtu6i8RlbSyY2zPij",
                    "name": "Fie Ce-o Fi",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e020a63c6055ed1e4e076797273",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048510a63c6055ed1e4e076797273",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2730a63c6055ed1e4e076797273",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "HDn7j4FYRbCtIaueORjsIw",
                      "shareUrl": "https://open.spotify.com/album/5droCbtu6i8RlbSyY2zPij?si=HDn7j4FYRbCtIaueORjsIw"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:6K5znXEhKmprKllzt4thhM",
                    "id": "6K5znXEhKmprKllzt4thhM",
                    "name": "Non Stop Hits",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e02b6b675628bda3fe485a69b37",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d00004851b6b675628bda3fe485a69b37",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b273b6b675628bda3fe485a69b37",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "epPKEGiXSUSZqeRZLz7idQ",
                      "shareUrl": "https://open.spotify.com/album/6K5znXEhKmprKllzt4thhM?si=epPKEGiXSUSZqeRZLz7idQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:7MH1sw6RnUkjSMTEoM5EGF",
                    "id": "7MH1sw6RnUkjSMTEoM5EGF",
                    "name": "Cadoul Tau De Craciun",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e023a3575f3e313c2743b6128f1",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048513a3575f3e313c2743b6128f1",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2733a3575f3e313c2743b6128f1",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "lf2ZEDsAT7iqiSYyFI4OoQ",
                      "shareUrl": "https://open.spotify.com/album/7MH1sw6RnUkjSMTEoM5EGF?si=lf2ZEDsAT7iqiSYyFI4OoQ"
                    }
                  }
                ]
              }
            },
            {
              "releases": {
                "totalCount": 1,
                "items": [
                  {
                    "uri": "spotify:album:4VCmuQ3aAPQZhOpwun5edv",
                    "id": "4VCmuQ3aAPQZhOpwun5edv",
                    "name": "Buna dimineata la Mos Ajun",
                    "artists": {
                      "items": [
                        {
                          "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of",
                          "profile": {
                            "name": "Various Artists"
                          }
                        }
                      ]
                    },
                    "coverArt": {
                      "sources": [
                        {
                          "url": "https://i.scdn.co/image/ab67616d00001e029874b85c97b795bd1eab6447",
                          "width": 300,
                          "height": 300
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d000048519874b85c97b795bd1eab6447",
                          "width": 64,
                          "height": 64
                        },
                        {
                          "url": "https://i.scdn.co/image/ab67616d0000b2739874b85c97b795bd1eab6447",
                          "width": 640,
                          "height": 640
                        }
                      ]
                    },
                    "sharingInfo": {
                      "shareId": "kyt6W9vyRImHTPE86wFTVA",
                      "shareUrl": "https://open.spotify.com/album/4VCmuQ3aAPQZhOpwun5edv?si=kyt6W9vyRImHTPE86wFTVA"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```







## Artist Related

Retrieves artists similar to the specified artist.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/artist_related/?id=2w9zwq3AktTeYYMuhMjju8", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "artists": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/6RQDTlies3nrNDJwXvbBZT"
      },
      "followers": {
        "href": null,
        "total": 164914
      },
      "genres": [
        "romanian pop"
      ],
      "id": "6RQDTlies3nrNDJwXvbBZT",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb0d6cf2887a3a062e07e473c2",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051740d6cf2887a3a062e07e473c2",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1780d6cf2887a3a062e07e473c2",
          "width": 160
        }
      ],
      "name": "Otilia",
      "popularity": 57,
      "type": "artist",
      "uri": "spotify:artist:6RQDTlies3nrNDJwXvbBZT"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/57Pw3FSi1qi2fOY4wKOKjK"
      },
      "followers": {
        "href": null,
        "total": 141785
      },
      "genres": [
        "disco polo",
        "europop",
        "romanian house",
        "romanian pop"
      ],
      "id": "57Pw3FSi1qi2fOY4wKOKjK",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebe9b9fbdd998a20f9d3d28068",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174e9b9fbdd998a20f9d3d28068",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178e9b9fbdd998a20f9d3d28068",
          "width": 160
        }
      ],
      "name": "Akcent",
      "popularity": 55,
      "type": "artist",
      "uri": "spotify:artist:57Pw3FSi1qi2fOY4wKOKjK"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/0BmLNz4nSLfoWYW1cYsElL"
      },
      "followers": {
        "href": null,
        "total": 343639
      },
      "genres": [
        "dance pop",
        "electropop",
        "romanian pop"
      ],
      "id": "0BmLNz4nSLfoWYW1cYsElL",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb07447480bbae1da5b3a2d014",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab6761610000517407447480bbae1da5b3a2d014",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f17807447480bbae1da5b3a2d014",
          "width": 160
        }
      ],
      "name": "Alexandra Stan",
      "popularity": 65,
      "type": "artist",
      "uri": "spotify:artist:0BmLNz4nSLfoWYW1cYsElL"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/2b01rwtcqW5LyfVBMzIFQ4"
      },
      "followers": {
        "href": null,
        "total": 58620
      },
      "genres": [
        "romanian pop"
      ],
      "id": "2b01rwtcqW5LyfVBMzIFQ4",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebd7fc46d6b21a51bcb57e55eb",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174d7fc46d6b21a51bcb57e55eb",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178d7fc46d6b21a51bcb57e55eb",
          "width": 160
        }
      ],
      "name": "Kate Linn",
      "popularity": 55,
      "type": "artist",
      "uri": "spotify:artist:2b01rwtcqW5LyfVBMzIFQ4"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/1oqThNqOfhev071PvmOwWQ"
      },
      "followers": {
        "href": null,
        "total": 124325
      },
      "genres": [
        "romanian house",
        "romanian pop"
      ],
      "id": "1oqThNqOfhev071PvmOwWQ",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eba8f9dce9103e30a3f9a3d781",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174a8f9dce9103e30a3f9a3d781",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178a8f9dce9103e30a3f9a3d781",
          "width": 160
        }
      ],
      "name": "DJ Project",
      "popularity": 51,
      "type": "artist",
      "uri": "spotify:artist:1oqThNqOfhev071PvmOwWQ"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/0rDSGIC4lIxx1zc0eGJY42"
      },
      "followers": {
        "href": null,
        "total": 49860
      },
      "genres": [
        "groove room",
        "romanian pop"
      ],
      "id": "0rDSGIC4lIxx1zc0eGJY42",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb2a928cbcd0adc5bdc3dc9eaf",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051742a928cbcd0adc5bdc3dc9eaf",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1782a928cbcd0adc5bdc3dc9eaf",
          "width": 160
        }
      ],
      "name": "Dj Sava",
      "popularity": 51,
      "type": "artist",
      "uri": "spotify:artist:0rDSGIC4lIxx1zc0eGJY42"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/1oiZoULxUJDYGOKMgVefP4"
      },
      "followers": {
        "href": null,
        "total": 43140
      },
      "genres": [
        "europop",
        "romanian pop"
      ],
      "id": "1oiZoULxUJDYGOKMgVefP4",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb2a7ed9042a0122efcc29cccc",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051742a7ed9042a0122efcc29cccc",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1782a7ed9042a0122efcc29cccc",
          "width": 160
        }
      ],
      "name": "Morandi",
      "popularity": 49,
      "type": "artist",
      "uri": "spotify:artist:1oiZoULxUJDYGOKMgVefP4"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/2Rum2rwDio2My0Md24m3Oa"
      },
      "followers": {
        "href": null,
        "total": 83716
      },
      "genres": [
        "romanian pop"
      ],
      "id": "2Rum2rwDio2My0Md24m3Oa",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebb82cdb8180bb919a8502046c",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174b82cdb8180bb919a8502046c",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178b82cdb8180bb919a8502046c",
          "width": 160
        }
      ],
      "name": "Fly Project",
      "popularity": 54,
      "type": "artist",
      "uri": "spotify:artist:2Rum2rwDio2My0Md24m3Oa"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/4TLzMoEaUDkcAfIlY3Xhxn"
      },
      "followers": {
        "href": null,
        "total": 106788
      },
      "genres": [
        "romanian pop"
      ],
      "id": "4TLzMoEaUDkcAfIlY3Xhxn",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebd42df33b004a1fbb03bd9620",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174d42df33b004a1fbb03bd9620",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178d42df33b004a1fbb03bd9620",
          "width": 160
        }
      ],
      "name": "Antonia",
      "popularity": 51,
      "type": "artist",
      "uri": "spotify:artist:4TLzMoEaUDkcAfIlY3Xhxn"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/0TmLIfQje5MdX2ovu4yQKz"
      },
      "followers": {
        "href": null,
        "total": 29781
      },
      "genres": [
        "romanian pop"
      ],
      "id": "0TmLIfQje5MdX2ovu4yQKz",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb9892d1e00cda3efacd23afd0",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051749892d1e00cda3efacd23afd0",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1789892d1e00cda3efacd23afd0",
          "width": 160
        }
      ],
      "name": "Monoir",
      "popularity": 54,
      "type": "artist",
      "uri": "spotify:artist:0TmLIfQje5MdX2ovu4yQKz"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/6XwwFnewNgWp81MYMK8zLq"
      },
      "followers": {
        "href": null,
        "total": 185741
      },
      "genres": [
        "romanian house",
        "romanian pop"
      ],
      "id": "6XwwFnewNgWp81MYMK8zLq",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebb20698cf6048254eea007587",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174b20698cf6048254eea007587",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178b20698cf6048254eea007587",
          "width": 160
        }
      ],
      "name": "Edward Maya",
      "popularity": 65,
      "type": "artist",
      "uri": "spotify:artist:6XwwFnewNgWp81MYMK8zLq"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/7hQmAXAzWI6D350VTgkKTG"
      },
      "followers": {
        "href": null,
        "total": 146138
      },
      "genres": [
        "persian pop"
      ],
      "id": "7hQmAXAzWI6D350VTgkKTG",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eba70ab4d7f3d5795603d2a4f8",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174a70ab4d7f3d5795603d2a4f8",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178a70ab4d7f3d5795603d2a4f8",
          "width": 160
        }
      ],
      "name": "Arash",
      "popularity": 61,
      "type": "artist",
      "uri": "spotify:artist:7hQmAXAzWI6D350VTgkKTG"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/3ZASW3RrHBbSRkNLjOrAFF"
      },
      "followers": {
        "href": null,
        "total": 33701
      },
      "genres": [
        "romanian house",
        "romanian pop"
      ],
      "id": "3ZASW3RrHBbSRkNLjOrAFF",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb5985f3c672438221b2d6d663",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051745985f3c672438221b2d6d663",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1785985f3c672438221b2d6d663",
          "width": 160
        }
      ],
      "name": "Sasha Lopez",
      "popularity": 51,
      "type": "artist",
      "uri": "spotify:artist:3ZASW3RrHBbSRkNLjOrAFF"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/4T8dF8zYAxgtlPPICuFQ5w"
      },
      "followers": {
        "href": null,
        "total": 57206
      },
      "genres": [
        "groove room",
        "pop dance"
      ],
      "id": "4T8dF8zYAxgtlPPICuFQ5w",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb524369d15fb6006b3c61a9d8",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174524369d15fb6006b3c61a9d8",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178524369d15fb6006b3c61a9d8",
          "width": 160
        }
      ],
      "name": "Pascal Junior",
      "popularity": 57,
      "type": "artist",
      "uri": "spotify:artist:4T8dF8zYAxgtlPPICuFQ5w"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/2rcsCDLsJw6erBukvjEsrP"
      },
      "followers": {
        "href": null,
        "total": 28060
      },
      "genres": [
        "romanian pop"
      ],
      "id": "2rcsCDLsJw6erBukvjEsrP",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb3270ef9055672c6138c7dbd5",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051743270ef9055672c6138c7dbd5",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1783270ef9055672c6138c7dbd5",
          "width": 160
        }
      ],
      "name": "Claydee",
      "popularity": 53,
      "type": "artist",
      "uri": "spotify:artist:2rcsCDLsJw6erBukvjEsrP"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/05qpk4JDcLSFNJSsPIZ8Ye"
      },
      "followers": {
        "href": null,
        "total": 250211
      },
      "genres": [
        "romanian pop"
      ],
      "id": "05qpk4JDcLSFNJSsPIZ8Ye",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebdbe3b95bf72c04d0669e0eb1",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174dbe3b95bf72c04d0669e0eb1",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178dbe3b95bf72c04d0669e0eb1",
          "width": 160
        }
      ],
      "name": "The Motans",
      "popularity": 53,
      "type": "artist",
      "uri": "spotify:artist:05qpk4JDcLSFNJSsPIZ8Ye"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/72FGvJgYbs0NBeJqECy6cF"
      },
      "followers": {
        "href": null,
        "total": 203631
      },
      "genres": [
        "classic romanian pop",
        "romanian pop"
      ],
      "id": "72FGvJgYbs0NBeJqECy6cF",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5ebc663ffd5c1034ccee2985aed",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab67616100005174c663ffd5c1034ccee2985aed",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f178c663ffd5c1034ccee2985aed",
          "width": 160
        }
      ],
      "name": "Andra",
      "popularity": 53,
      "type": "artist",
      "uri": "spotify:artist:72FGvJgYbs0NBeJqECy6cF"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/4oE7f7lNFkh0EbEZWEawBF"
      },
      "followers": {
        "href": null,
        "total": 12187
      },
      "genres": [
        "romanian pop"
      ],
      "id": "4oE7f7lNFkh0EbEZWEawBF",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb69be3df5d247c29d7e90283a",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab6761610000517469be3df5d247c29d7e90283a",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f17869be3df5d247c29d7e90283a",
          "width": 160
        }
      ],
      "name": "SICKOTOY",
      "popularity": 58,
      "type": "artist",
      "uri": "spotify:artist:4oE7f7lNFkh0EbEZWEawBF"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/5v7efr4mqt3RQxkT0Mmh5g"
      },
      "followers": {
        "href": null,
        "total": 139277
      },
      "genres": [
        "desi pop"
      ],
      "id": "5v7efr4mqt3RQxkT0Mmh5g",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb5ddbc60af905a570589a2a1d",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051745ddbc60af905a570589a2a1d",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1785ddbc60af905a570589a2a1d",
          "width": 160
        }
      ],
      "name": "Faydee",
      "popularity": 62,
      "type": "artist",
      "uri": "spotify:artist:5v7efr4mqt3RQxkT0Mmh5g"
    },
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/5T0j6On1EthT2QVNXh8vqc"
      },
      "followers": {
        "href": null,
        "total": 87444
      },
      "genres": [
        "romanian pop"
      ],
      "id": "5T0j6On1EthT2QVNXh8vqc",
      "images": [
        {
          "height": 640,
          "url": "https://i.scdn.co/image/ab6761610000e5eb4d6f226b185b33b6a0cc3038",
          "width": 640
        },
        {
          "height": 320,
          "url": "https://i.scdn.co/image/ab676161000051744d6f226b185b33b6a0cc3038",
          "width": 320
        },
        {
          "height": 160,
          "url": "https://i.scdn.co/image/ab6761610000f1784d6f226b185b33b6a0cc3038",
          "width": 160
        }
      ],
      "name": "Minelli",
      "popularity": 66,
      "type": "artist",
      "uri": "spotify:artist:5T0j6On1EthT2QVNXh8vqc"
    }
  ]
}




## Track Lyrics

Retrieves lyrics for a specific track including synchronized lyrics data.

```python
import http.client

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/track_lyrics/?id=4snRyiaLyvTMui0hzp8MF7", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

**Response:**
```json
{
  "lyrics": {
    "syncType": "LINE_SYNCED",
    "lines": [
      {
        "startTimeMs": "0",
        "words": "Run like this, run, I",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "5120",
        "words": "Run like this, run, love you",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "9690",
        "words": "But you run like this, run like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "15060",
        "words": "Run like this, run, love you",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "20420",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "30130",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "39960",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "49100",
        "words": "Run like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "59410",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "69340",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "76700",
        "words": "(Like, like, like)",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "78540",
        "words": "Run like this, run, I",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "83320",
        "words": "Run like this, run, love you",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "87870",
        "words": "But you run like this, run, I",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "92910",
        "words": "Run like this, run, love",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "97540",
        "words": "",
        "syllables": [],
        "endTimeMs": "0"
      }
    ],
    "provider": "MusixMatch",
    "providerLyricsId": "198920318",
    "providerDisplayName": "Musixmatch",
    "syncLyricsUri": "",
    "isDenseTypeface": false,
    "alternatives": [],
    "language": "en",
    "isRtlLanguage": false,
    "capStatus": "UNCAPPED",
    "isSnippet": false,
    "previewLines": [
      {
        "startTimeMs": "0",
        "words": "Run like this, run, I",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "5120",
        "words": "Run like this, run, love you",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "9690",
        "words": "But you run like this, run like",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "15060",
        "words": "Run like this, run, love you",
        "syllables": [],
        "endTimeMs": "0"
      },
      {
        "startTimeMs": "20420",
        "words": "Like",
        "syllables": [],
        "endTimeMs": "0"
      }
    ]
  },
  "colors": {
    "background": -1241843,
    "text": -16777216,
    "highlightText": -1
  },
  "hasVocalRemoval": false
}
```




