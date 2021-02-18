print('Hello World')

import requests

url = "https://seekingalpha.com/article/4406922-wesfarmers-limited-wfaff-ceo-rob-scott-on-half-year-2021-results-earnings-call-transcript"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0."
}
res = requests.get(url)
print('status code {}'.format(res.status_code))

with open('transcript_result.txt', 'w+') as file:
    file.write(res.text)
    file.close()
