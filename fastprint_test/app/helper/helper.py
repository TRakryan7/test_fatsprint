import hashlib
import requests
from datetime import datetime

url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
today = datetime.now()


def get_data():
    username = generate_username()
    password = generate_password()
    form_data = {"username": username, "password":password}
    
    
    
    #print("reponse",response.headers.get('X-Credentials-Username'))
    try:
        response = requests.post(url, data=form_data)
        if response.status_code == 200:
            products = response.json()
            return products  
        else:
            return print(f"Failed to fetch data: {response.status_code}")
    except:
        raise Exception("Maaf ada yng salah")


def generate_password():
    
    dd = today.strftime("%d")
    mm = today.strftime("%m")
    yy = today.strftime("%y")
    
    result = f"bisacoding-{dd}-{mm}-{yy}"
    
    password = hashlib.md5(result.encode()).hexdigest()
    return password
    

def generate_username():
        
    response = requests.post(url)
    variable = response.headers.get('X-Credentials-Username')
    result = variable.split(" ")[0]
    
    return result