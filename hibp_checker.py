from hibp import HIBP
import requests
import gevent
import time
import json

emails = []

breach_list = []
pwned = []

for email in emails:

	req = HIBP.get_account_breaches(email)
	req.execute()
	if req.response == 'object has not been pwned.':
		pass
	else:
		print(json.dumps(req.response, indent=4, sort_keys=True))
		pwned.append(email)
		for item in req.response:
			breach_list.append(item['Domain'])
	time.sleep(1.3)

print(breach_list)
print('Total UIDs pwned: %s' % len(pwned))