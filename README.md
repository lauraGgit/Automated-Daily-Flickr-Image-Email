#Python Automated Daily
Image Email
This repository will set up an automated email that will send a daily email to you with custom text and a random flickr image based of a certain search term. It uses a python generated cronjob to perform this task.

##Setup
1. Install [Python-crontab](https://pypi.python.org/pypi/python-crontab) on your machine
2. Grab a [Flickr Api Key](https://www.flickr.com/services/apps/create/)
3. Fill out config.py for your settings
4. Modify the email text in the text.txt file. By sure to include HTML tags in the document and also the <image_url> tag to tell the code where to put the image.
5. Run install_email.py
6. Enjoy your daily email

## Config.py Paramters
    flick_settings = dict(
            search_params = dict(
                    tags = 'search_tags',
                    text = 'search_text'
                    ),
            api_params = dict(
                    key = 'Flickr_api_key',
                    secret = 'Flickr_api_secret'
                    )
    )
    
    email_settings = dict(
            text_file = 'text.txt',
            email_sender = 'you@gmail.com',
            email_recipients = ['your_cool_friend@gmail.com', 'your_second_cool_friend@gmail.com'],
            subject = 'Email Subject',
            smtp_settings = dict(
                    server = 'smtp.your_email_provider.com',
                    username='your_email_username',
                    password='your_email_password'
            )
    )
    
    date_settings = dict(
            date_start = '01-12',
            date_end = '10-15',
            time_to_send = '07:15'
    )

###Flickr Settings
*Search Parameters - What Flickr tags or text you would like to search on. It is recommended to just use one tag or term. See the [Flickr.py](https://code.google.com/p/flickrpy/) documentation or the [Flickr API documentation](https://www.flickr.com/services/api/flickr.photos.search.html) to learn more.
*Api Parameters - These are the Flickr Api Key and Secret that you will have obtained from [Flickr's Developer Website](https://www.flickr.com/services/apps/create/)

###Email Settings
You will need some sort of SMTP access to send your emails.
*Text File - This is the HTML of your body of your email. You should be able to keep text.txt, but you can also add a different file in the same directory.
*Email Sender - The sender of the email
*Email Recipients - A list of all the recipients that you would like to send your daily image email
*Subject - The subject of the email
*SMTP Settings - These are the settings for authentication for an outgoing mail server. If you are using GMAIL check out the Google's [settings and special requirements to send](http://lifehacker.com/111166/how-to-use-gmail-as-your-smtp-server).

### Date Settings
Enter the dates you would like the email to be sent and the time of day you would like to send the email in the above format.
