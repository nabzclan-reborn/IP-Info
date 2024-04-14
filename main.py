import argparse
import requests
import json
from colorama import init, Fore

init(autoreset=True)

def get_ip_location(ip, token_type, api_key):
    url = f"https://api.api-aries.online/v1/lookup/iplookup/?ip={ip}"
    headers = {
        'Type': token_type,
        'APITOKEN': api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 

        formatted_response = json.dumps(response.json(), indent=4)
        print(Fore.GREEN + "Response:")
        print(Fore.WHITE + formatted_response)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error occurred during request: {e}")
    except json.JSONDecodeError as e:
        print(Fore.RED + f"Error decoding JSON response: {e}")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='IP TO LOCATION')
    parser.add_argument('-ip', '--ip', metavar='IP', help='Find IP location - Example: python3 main.py -ip 111.111.1.111')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.ip:
        # REQUIRED
        token_type = "1" # token type :  https://support.api-aries.online/hc/articles/1/3/13/p12-password-cracker#token-types-required
        api_key = "111-111-111"  #API Token : https://support.api-aries.online/hc/articles/1/3/13/p12-password-cracker
        get_ip_location(args.ip, token_type, api_key)
    else:
        print(Fore.RED + "Please provide an IP address.")
        print("Usage: python3 main.py -ip <IP>")
        exit()

if __name__ == "__main__":
    main()
