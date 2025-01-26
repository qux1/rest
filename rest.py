from requests import *
from user_agent import generate_user_agent

email = 'alexwashere2023@Fuck.com'
class Rest:
	def __init__(self):
		
		# Get Cookies from link rest 
		Cookie = get("https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",headers={'user-agent':str(generate_user_agent())}).cookies.get_dict()
		
		self.csrfToken=Cookie['csrftoken']
		self.ig_did=Cookie['ig_did']
		self.mid=Cookie['mid']
		
	#Call the rest function .	
		self.rest()
		
	def rest(self):
		
		# Send Rest with Email 
		Send_Requets = post("https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",headers={'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'62',
'content-type':'application/x-www-form-urlencoded',
'cookie':f'csrftoken={self.csrfToken}; mid={self.mid}; ig_did={self.ig_did}',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/accounts/password/reset/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'"Chromium";v="111",                                  "Not(A:Brand";v="8"',
         'sec-ch-ua-mobile':'?1',
         'sec-ch-ua-platform':'"Android"',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':str(generate_user_agent()),
         'viewport-width':'412',
         'x-asbd-id':'198387',
         'x-csrftoken':str(self.csrfToken),
         'x-ig-app-id':'1217981644879628',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'150e106c61a4',
         'x-requested-with':'XMLHttpRequest"'},data={'email_or_username':str(email),'recaptcha_challenge_field':''})
		if "checkpoint_required"in Send_Requets.text:
			return True
		else:
			return False
