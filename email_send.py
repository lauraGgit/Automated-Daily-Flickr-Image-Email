import smtplib
import flickr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import random
import os
import sys


def get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, per_page=number)
    urls = []
    for photo in photos:
        urls.append(photo.getURL(size='Large', urlType='source'))
    return urls

def selectRandomfromList(urls):
	r = random.randrange(0, len(urls))
	return urls[r]


# Create the body of the message (a plain-text and an HTML version).
def imgMsg(imgUrl, text):
	email = """\
	<html>
	<head></head>
	<body>
	"""
	email_text = text

	with open (email_text, "r") as emailbody:
		email += emailbody.read()

	email += """
	</body>
	</html>
	"""
	img = '<img src="'+imgUrl+'">'
	reg = email.replace('<image_url>', img)
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(reg, 'plain')
	part2 = MIMEText(reg, 'html')
	return part1, part2

def emailSend(from_addr, to_addr_list, cc_addr_list,
              subject, text_message, html_message, login, password,
              smtpserver= config.email_settings['smtp_settings']['server']):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = from_addr
    message['To'] = ', '.join(to_addr_list)
    message['Cc'] = ', '.join(cc_addr_list)
    message.attach(text_message)
    message.attach(html_message)

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list+cc_addr_list, message.as_string())
    server.quit()
    return problems
if __name__ == "__main__":
	flickr.API_KEY = config.flick_settings['api_params']['key']
	flickr.API_SECRET = config.flick_settings['api_params']['secret']
	cfgEm = config.email_settings
	urls = get_urls_for_tags(config.flick_settings['search_params']['tags'], 50)
	img = selectRandomfromList(urls)

	sys_path = os.path.dirname(os.path.realpath(__file__))
	part1, part2 = imgMsg(img, sys_path+'/'+cfgEm['text_file'])
	emailSend(cfgEm['email_sender'], cfgEm['email_recipients'], [], cfgEm['subject'], part1, part2, cfgEm['smtp_settings']['username'], cfgEm['smtp_settings']['password'])
	#print img
