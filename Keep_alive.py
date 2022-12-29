import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo"

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["Keep-Alive"] = "timeout=5, max=10"
