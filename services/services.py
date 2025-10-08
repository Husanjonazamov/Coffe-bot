# services.py fayli
from utils.env import BASE_URL
import requests




def createUser(user_id: int, first_name: str, lang):
    url = f"{BASE_URL}/auth/register/"
    payload = {
        "tg_id": int(user_id),
        "first_name": first_name,
        "lang": lang
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



def getUser(user_id):
    url = f"{BASE_URL}/auth/me/{user_id}/"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    
    except Exception as e:
        return {"error": str(e)}
    
    


def patchUser(tg_id, lang):
    url = f"{BASE_URL}/auth/user-update/"
    payload = {
        "tg_id": tg_id,
        "lang": lang
    }
    try:
        response = requests.patch(url, json=payload)
        response.raise_for_status() 
        data = response.json()
        return data.get('data', data) 
    except Exception as e:
        return {"error": str(e)}

    

def getProduct(lang: str = "uz"):
    url = f"{BASE_URL}/product/"
    headers = {"Accept-Language": lang}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        products = data["data"]
        return products
    except Exception as e:
        print("getProduct error:", e)
        return {"error": str(e)}


def getProductDetail(title: str, lang: str = "uz"):
    url = f"{BASE_URL}/product/{title}/"
    headers = {"Accept-Language": lang}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        print("getProductDetail error:", e)
        return {"error": str(e)}