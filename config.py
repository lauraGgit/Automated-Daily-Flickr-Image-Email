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
	email_recipients = ['your_cool_friend@gmail.com'],
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