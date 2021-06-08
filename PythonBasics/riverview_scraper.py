import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# print(EMAIL_ADDRESS)

URL_OFFER = 'https://www.irvinecompanyapartments.com/content/icac/ica/home/' \
      'special-offers/san-jose.html#community=RiverView'

URL_AVAILABILITY = 'https://www.irvinecompanyapartments.com/locations/' \
                   'northern-california/san-jose/river-view/availability.html#availability'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}


def check_riverview_offer():
    page = requests.get(URL_OFFER, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('title').get_text()
    print('Title -', title)
    assert 'San Jose' in title, 'Title mismatch'

    offer_description_element = soup.select(".description > p:nth-of-type(1)")  # Even ".description > p" would work
    offer_description = offer_description_element[0].get_text()
    print('Offer description -', offer_description)

    if 'April' in offer_description:
        print('** Offer in April **')
        send_email('Still April')
    elif 'May' in offer_description:
        print('** Offer in May **')
        send_email('Hurray, Its May offer!')


def check_riverview_availability():
    page = requests.get(URL_AVAILABILITY, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('title').get_text()
    print('Title -', title)
    assert 'San Jose' in title, 'Title mismatch'

    print(soup.find_all("p", class_="fapt-fp-map__note"))
    # print(soup.find(id='//body[1]/div[3]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/svg[1]/g[1]/g[1]/g[8]/path[62]'))
    # print('Availability -', availability)
    # print(availability.find_all('class'))
    # offer_description = offer_description_element[0].get_text()


def send_email(month):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = f'{month} - Riverview Offer - Self Bot'
    body = f'{month} Riverview Offer Details - Self Bot \n ' \
           f'https://www.irvinecompanyapartments.com/content/icac/ica/home' \
           f'/special-offers/san-jose.html#community=RiverView'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        EMAIL_ADDRESS,
        EMAIL_ADDRESS,
        msg
    )

    server.quit()


check_riverview_availability()
# try:
#     check_riverview_offer()
#     print('Email sent!')
#
# except Exception as e:
#     print('Script failing\n', e.__class__)
#     send_email('Script failing!')

# while True:
#     check_riverview_offer()
#     time.sleep(60*60*6)

'''
	In crontab -e: 
	* * * * * $HOME/cron_job.sh
	
	In cron_job.sh: 
	!/bin/bash
	source $HOME/.bash_profile
	/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 
	/Users/paragshah/PythonCoding/PythonPractice/PythonBasics/riverview_scraper.py
	
	EC2: 
/usr/bin/python3 /home/ubuntu/riverview_scrapper.py > /tmp/riverview
'''
