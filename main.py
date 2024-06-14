import argparse
import requests
import json
from colorama import init, Fore

# Initialize colorama to automatically reset color changes
init(autoreset=True)

def get_public_ip():
    """
    Function to get the public IP address of the current user.
    
    Returns:
    str: The public IP address.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip = response.json().get("ip")
        return ip
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching public IP: {e}")
        return None

def get_ip_location(ip, api_key):
    """
    Function to get the location of an IP address using the provided API.
    
    Args:
    ip (str): The IP address to lookup.
    api_key (str): The API key for authentication.
    """
    url = f"https://api.api-aries.online/v1/lookup/iplookup/?ip={ip}"
    headers = {
        'APITOKEN': api_key,
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        data = response.json()

        # Add Google Maps link to the response
        if 'lat' in data and 'lon' in data:
            data['google_maps_link'] = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"

        # Pretty print the JSON response
        formatted_response = json.dumps(data, indent=4)
        print(Fore.GREEN + "Response:")
        print(Fore.WHITE + formatted_response)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error occurred during request: {e}")
    except json.JSONDecodeError as e:
        print(Fore.RED + f"Error decoding JSON response: {e}")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")

def parse_arguments():
    """
    Function to parse command-line arguments.
    
    Returns:
    Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='IP to Location Lookup')
    parser.add_argument('-ip', '--ip', metavar='IP', help='Find IP location - Example: python3 main.py -ip 111.111.1.111')
    return parser.parse_args()

def main():
    """
    Main function to execute the script.
    """
    args = parse_arguments()
    api_key = "111-111-111-111"  # API Token : https://support.api-aries.online/hc/articles/1/3/8/ip-lookup-api

    if args.ip:
        # Use the provided IP address
        get_ip_location(args.ip, api_key)
    else:
        # Get the public IP address of the current user
        public_ip = get_public_ip()
        if public_ip:
            print(Fore.BLUE + f"Using public IP address: {public_ip}")
            get_ip_location(public_ip, api_key)
        else:
            print(Fore.RED + "Unable to determine public IP address.")

if __name__ == "__main__":
    main()
