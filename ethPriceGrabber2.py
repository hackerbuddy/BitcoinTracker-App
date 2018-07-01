import urllib.request
from bs4 import BeautifulSoup
import time
import datetime
import ethMail



import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.Request("***", headers={'User-Agent' : "Magic Browser"})
response = urllib.request.urlopen(req)
html= response.read()
#parse with our Beautiful Soup!
soup= BeautifulSoup(html, "html5lib")
startPrice= soup('span', {'id' : 'quote_price'})[0]
startPrice= str(startPrice)
startPrice=startPrice[43:49]
print(startPrice)

#some globals
startTime= None
printed= False
isPositive = True
isZero= True
badAlerted1= False
badAlerted2= False
badAlerted3= False

goodAlerted0= False 
goodAlerted1= False
goodAlerted2= False
goodAlerted3= False
goodAlerted4= False

elapsedSeconds=0
elapsedMinutes=0
elapsedHours=0
elapsedDays=0

minutes= 0
seconds= 0
hours= 0
days= 0


if startTime is None:
	startTime= time.time();
	startDateString= datetime.datetime.fromtimestamp(startTime).strftime('%m-%d-%Y %H:%M:%S')
currentTime = time.time()
elapsedTime = int(currentTime - startTime)

while elapsedTime < 43200:  #8 hours
	currentTime= time.time()
	elapsedTime = int(currentTime - startTime)
	elapsedSeconds= int(elapsedTime);
	
	if elapsedTime%60 == 0 and printed is False:
	#everything important happens here! Every 10s
		#read in the request
		print("60 seconds have passed...Updating...")
		req = urllib.request.Request("https://coinmarketcap.com/currencies/ethereum/", headers={'User-Agent' : "Magic Browser"})
		response = urllib.request.urlopen(req)
		html= response.read()
		#parse with our Beautiful Soup!
		soup= BeautifulSoup(html, "html5lib")
		price= soup('span', {'id' : 'quote_price'})[0]
		price= str(price)
		price=price[43:49]
		print(price) 
		
		#write to file and print in console
		dateString= datetime.datetime.fromtimestamp(currentTime).strftime('%m-%d-%Y %H:%M:%S')
		delta= float(price)- float(startPrice) 
		#check if number has increased or decreased
		if delta == 0:
			isZero=True
			isPositive= False
			deltaStatus= "is unchanged: "
		elif delta > 0:
			isZero=False
			isPositive= True
			deltaStatus= "is UP "
		else:
			isZero=False
			isPositive= False	
			deltaStatus= "is DOWN "
		
		print("Ethereum price is $" + price + " at " + dateString + "\nPrice " + deltaStatus + "$" + ("%.2f" % round(delta,2)) + " from " 
		+ startDateString + ", " + str(hours) +" hour(s) ago and " + str(minutes)+ " minutes ago\n") 
		pp= open('priceETH.txt','a+')
		pp.write(price + " " + dateString + "\n")
		printed= True;
		
		if float(price) > 300.00 and badAlerted1 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nWARNING! Uh,oh, Ethereum price has fallen to $" + price + "." + "\n\nIt is strongly reccomended that you take action now and sell if there is a negative downward trend.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A sad email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has fallen to $" + price + "at " + dateString + ".\n")
			ep.close()
			badAlerted1 = True
		if float(price) < 295.00 and badAlerted2 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nWARNING! Ethereum price has fallen to $" + price + "." + "\n\nIt is strongly reccomended that you take action now and sell if there is a negative downward trend.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A sad email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has fallen to $" + price + "at " + dateString + ".\n")
			ep.close()
			badAlerted2 = True
		if float(price) < 290.00 and badAlerted3 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nWARNING! Ethereum price has fallen to $" + price + "." + "\n\GET THE HELL OUT OF THERE!!!\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A sad email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has fallen to $" + price + " at " + dateString + ".\n")
			ep.close()
			badAlerted3 = True	
		
		if float(price) > 303.00 and goodAlerted0 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nCONGRATS! Ethereum price has risen to $" + price + "." + "\n\nWell played, sire.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A happy email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has risen to $" + price + " at " + dateString + ".\n")
			ep.close()
			goodAlerted0 = True
		if float(price) > 305.00 and goodAlerted1 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nCONGRATS! Ethereum price has risen to $" + price + "." + "\n\nWell played, sire.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A happy email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has risen to $" + price + " at " + dateString + ".\n")
			ep.close()
			goodAlerted1 = True
		if float(price) > 310.00 and goodAlerted2 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nCONGRATS! Ethereum price has risen to $" + price + "." + "\n\nWell played, sire.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A happy email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has risen to $" + price + " at " + dateString + ".\n")
			ep.close()
			goodAlerted2 = True			
		if float(price) > 315.00 and goodAlerted3 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nCONGRATS! Wow! Ethereum price has risen to $" + price + "." + "\n\nKeep up the good work!.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A happy email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has risen to $" + price + " at " + dateString+ ".\n")
			ep.close()
			goodAlerted3 = True
		if float(price) > 320.00 and goodAlerted4 is False:
			ep= open('ethAlert.txt','w')
			ep.write("Dear User,\n\nCONGRATS! Ethereum price has risen to $" + price + "." + "\n\nKeep up the good work!.\n" + "\nSincerely,\n\n" + "Braden")
			ep.close()
			printed= True;
			ethMail.sendMail() #uses email script to send alert
			print("A happy email alert was sent!")
			ep= open('mailSentLog.txt','a+')
			ep.write("Email sent: Ethereum price has risen to $" + price + " at " + dateString+ ".\n")
			ep.close()
			goodAlerted4 = True
			
		
		minutes+=1
		elapsedSeconds = 0
		
		if elapsedMinutes == 60:
				hours+=1
				minutes= 0
		if elapsedHours == 24:
				days+=1
				hours = 0
	elif elapsedTime%60 != 0:
		printed= False;
				
				
pp.close()

