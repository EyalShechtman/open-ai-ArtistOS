#!/usr/bin/env python3
"""
Simple Spotify RapidAPI Tester
Test any of the Spotify API endpoints through RapidAPI.
"""

import http.client
import json
import sys

# Configuration
RAPIDAPI_KEY = "7a0eb17e5emsh2414592ba7c4a38p1f1d91jsn5e83c66c0259"
RAPIDAPI_HOST = "spotify23.p.rapidapi.com"

def make_api_call(endpoint, params=""):
    """Make an API call to RapidAPI"""
    try:
        conn = http.client.HTTPSConnection(RAPIDAPI_HOST)

        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': RAPIDAPI_HOST
        }

        url = f"/{endpoint}"
        if params:
            url += f"?{params}"

        print(f"🔗 Making request to: {RAPIDAPI_HOST}{url}")

        conn.request("GET", url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            response_json = json.loads(data.decode("utf-8"))
            print("✅ Success!")
            print("\n📄 Response:")
            print(json.dumps(response_json, indent=2, ensure_ascii=False))

            # Ask user if they want to save the response
            save_choice = input("\n💾 Save response to JSON file? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                filename = input("📝 Enter filename (without .json extension): ").strip()
                if not filename:
                    filename = f"{endpoint}_response"
                filename += ".json"

                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(response_json, f, indent=2, ensure_ascii=False)

                print(f"💾 Response saved to {filename}")
        else:
            print(f"❌ Error: {res.status}")
            print(data.decode("utf-8"))

    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    print("🎵 Spotify RapidAPI Tester")
    print("=" * 40)

    # Endpoint menu
    endpoints = {
        "1": ("albums", "Get Albums", "ids"),
        "2": ("album_tracks", "Album Tracks", "id,offset,limit"),
        "3": ("album_metadata", "Album Metadata", "id"),
        "4": ("artist_overview", "Artist Overview", "id"),
        "5": ("artist_discography_overview", "Artist Discography", "id"),
        "6": ("artist_singles", "Artist Singles", "id,offset,limit"),
        "7": ("artist_appears_on", "Artist Appears On", "id"),
        "8": ("artist_related", "Artist Related", "id"),
        "9": ("track_lyrics", "Track Lyrics", "id")
    }

    print("\n📋 Available endpoints:")
    for key, (endpoint, description, params) in endpoints.items():
        print(f"  {key}. {description} ({endpoint})")

    choice = input("\n🎯 Choose endpoint (1-9): ").strip()

    if choice not in endpoints:
        print("❌ Invalid choice!")
        sys.exit(1)

    endpoint, description, param_names = endpoints[choice]
    print(f"\n🎵 Testing: {description}")
    print(f"🔧 Endpoint: {endpoint}")

    # Build parameters
    params = []
    param_list = param_names.split(",")

    for param in param_list:
        value = input(f"📝 Enter {param}: ").strip()
        if value:
            params.append(f"{param}={value}")

    params_str = "&".join(params)

    print("\n🚀 Making API call...")
    make_api_call(endpoint, params_str)

if __name__ == "__main__":
    main()
