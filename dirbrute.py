import requests

url = input("Digite a url: ")

with open("wordlist.txt", "r") as file:
        wordlist = file.readlines()

for word in wordlist:
	url_final = "{}/{}".format(url, word.strip())
	response = requests.get(url_final)
	code = response.status_code
	if code != 404:
		print("{} --> {}".format(url_final, code))
