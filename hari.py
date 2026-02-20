import requests

BASE_URL = "https://petstore.swagger.io/v2"
PETS_URL = f"{BASE_URL}/pet"


def get_all_pets(status:str ='available'):
    PET_STATUS_URL = f"{PETS_URL}/findByStatus?status={status}"
    response = requests.get(
        PET_STATUS_URL,
        timeout=30)
    print(response)

    pets = response.json()
    for pet in pets:
        if 'id' in pet and 'name' in pet:
            print(f"{pet['id']} <==> {pet['name']}")
        else:
            print(pet)


if __name__ == "__main__":
    get_all_pets()

