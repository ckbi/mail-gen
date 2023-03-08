from bs4 import BeautifulSoup
import requests
import time
import os

def getEmail():
	URL_Email = "https://10minutemail.net/"
	email_page = requests.get(URL_Email)
	handle_email = BeautifulSoup(email_page.content, 'html.parser')
	email = handle_email.find(class_='div-m-0 text-c')
	email = str(email)[84:].replace("\"/></div>", '')
	return email

def clear(): 
	if os.name == 'nt':
		os.system('cls') 
	else:
		os.system('clear')

def banner():
	clear()
	

def writeToFile(email):
	file = open("emails.txt", 'a')
	write = ''
	write += email + '\n'
	file.write(write)
	file.close()

def main():
	banner()
	try:
		numEmails = int(input("[+] How much? "))
	except:
		print("[!] Invalid Value Entered. Restarting in 2 secs...")
		time.sleep(2)
		main()
	writeOrNot = str(input("[+] Wanna save them in a file? (Y/N): "))
	write = False
	if 'y' == writeOrNot[0].lower():
		write = True
	if write == True:
		print("[*] Writing to file has been enabled!")
	print("[*] Creating {} emails".format(numEmails))
	try:
		for x in range(numEmails):
			email = getEmail()
			if '@' not in email:
				print("""
					[!] IP BANNED USE A VPN OR RESTART THE ROUTER!
						
					""")
				break
			else:
				if write == True:
					writeToFile(email)
				print("Email number {} : {}".format(x+1, email))
	except:
		print("Exiting...")
		exit()
if __name__ == "__main__":
	main()
