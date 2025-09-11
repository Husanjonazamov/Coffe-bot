# services.py fayli
from utils.env import BASE_URL
import requests





def getProduct():
    url = f"{BASE_URL}/product/"
    response = requests.get(url)
    
    try:
        data = response.json()
        products = data["data"]["results"]  # faqat result listini olamiz
        return products
    except Exception as e:
        print(e)