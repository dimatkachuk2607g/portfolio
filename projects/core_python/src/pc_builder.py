"""
PC Builder Project

This script allows users to select a PC build (low, mid or high budget) and
platform (AMD or Intel)
loads component details from a JSON file, and prints a summary with full details
"""

import json
from pathlib import Path

def get_build_choice():
    """Prompt the user to select a valid build type"""
    while True:
        choice = input("""\
=============================
Welcome to the PC Builder!
=============================
Please enter your choice:
1 - for our low budget build
2 - for our mid budget build
3 - for our high budget build

Your choice: """)

        if choice in ("1", "2", "3"):
            return choice
        else:
            print(f'Your choice was: "{choice}", Please enter a valid choice')


def get_platform_choice():
    """Prompt the user to select a valid build platform"""
    while True:
        platform_choice = input("""
Please enter your choice of preferred platform:
1 - AMD
2 - Intel

Your choice: """)

        if platform_choice in ("1", "2"):
            return platform_choice
        else:
            print(f'Your choice was: "{platform_choice}", Please enter a valid choice')


def json_load_parts():
    "Loads the part list from the json file"
    json_file = Path(__file__).parent / "part_list.json"
    try:
        with open(json_file, "r") as fh:
            builds = json.loads(fh.read())
            return builds
    except (FileNotFoundError, json.JSONDecodeError) as error:
        raise RuntimeError(f"JSON file is invalid: {error}")


def print_summary(customer_build):
    total_order_price = sum(customer_build.values())

    print("=" * 100)
    print("\nBuild and price details:")
    print("=" * 100)

    for part, price in customer_build.items():
        print(f'Part: {part:<60}| \t\t\t Value: ${price}')

    print("=" * 100)
    print(f'Total order price: ${total_order_price}')
    print("=" * 100)
    print(f'Thanks for using the PC Builder!')





def main():
    choice = get_build_choice()
    platform_choice = get_platform_choice()
    customer_build = json_load_parts()[choice][platform_choice]
    print_summary(customer_build)


if __name__ == "__main__":
    main()