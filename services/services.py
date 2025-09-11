# services.py fayli
from utils.env import BASE_URL
import requests




def createUser(user_id: int, first_name: str):
    url = f"{BASE_URL}/auth/register/"
    payload = {
        "tg_id": int(user_id),
        "first_name": first_name,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        print(response)
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            return {
                "error": "Backend JSON emas javob qaytardi",
                "status_code": response.status_code,
                "text": response.text
            }

        if not response.ok:
            return {
                "error": data,
                "status_code": response.status_code
            }

        return data

    except Exception as e:
        print("createUser error:", e)
        return {"error": str(e)}

    
    

def getProduct():
    url = f"{BASE_URL}/product/"
    response = requests.get(url)
    
    try:
        data = response.json()
        products = data["data"]["results"]  # faqat result listini olamiz
        return products
    except Exception as e:
        print(e)
        
        
        

def getProductDetail(title):
    url = f"{BASE_URL}/product/{title}/"
    response = requests.get(url)
    
    try:
        data = response.json()
        return data
    except Exception as e:
        print(e)