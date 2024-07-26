import sys
import requests

def get_location(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    # Replace 'your_token_here' with your actual ipinfo token
    token = '54c517a4cfbb6e'

    # Get the IP address from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python ip_location.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    location_data = get_location(ip_address, token)

    print(f"IP Address: {location_data.get('ip', 'N/A')}")
    print(f"City: {location_data.get('city', 'N/A')}")
    print(f"Region: {location_data.get('region', 'N/A')}")
    print(f"Country: {location_data.get('country', 'N/A')}")
    print(f"Location: {location_data.get('loc', 'N/A')}")
    print(f"Postal: {location_data.get('postal', 'N/A')}")
    print(f"Organization: {location_data.get('org', 'N/A')}")
