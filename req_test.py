import requests
import time
start = time.time()
for i in range(10000):

    r = requests.post('http://127.0.0.1:8080/user?name=mudak')
    #print(r.status_code, r.content)
t = time.time() - start
print(t)