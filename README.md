# Gmail-API-Send
## 藉由Gmail API寄送郵件，授權後免輸入帳號密碼
https://developers.google.com/gmail/api/quickstart/python
1. Download credentials.json [DOWNLOAD CLIENT CONFIGURATION ]
2. pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
3. python quickstart.py create 2 token files
4. token.json、token.pickle
5. 將token.pickle、token.json、credentials.json放置同目錄下
6. pip install ezgmail
7. python send_mail_ezgmail.py.py
