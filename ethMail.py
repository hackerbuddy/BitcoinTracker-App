import smtplib
from email.mime.text import MIMEText


def sendMail():
	textfile = "ethAlert.txt"  
	fromaddr = "**"
	toaddr = "**"

	with open(textfile) as fp:
		# Create a text/plain message
		msg = MIMEText(fp.read())

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Price Alert For Ethereum"

	 
	server = smtplib.SMTP('smtp.gmail.com', 587, None, 30)
	server.starttls()
	server.login(fromaddr, "*******")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	return 
	
	
	
