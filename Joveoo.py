import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

def findnth(ReqData, needle, n):
    parts= ReqData.split(needle, n+1)
    print parts[1]
    if len(parts)<=n+1:
        return -1
    return len(ReqData)-len(parts[-1])-len(needle)

def Ripple_Bayard_Clickcast(raw_data,n): #n= The number of fields
	start_string = "Ripple - Bayard Clickcast</a></td>"
	end_string = '<a href="/adverts/4992/adverts/29613/edit-rate?czid=34035">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	#print ReqData
	#ClickStart=ReqData.find('<td class="numeric">')
	#ClickEnd=ReqData.find('</td>')
	#Clicks=ReqData[ClickStart+len('<td class="numeric">'):ClickEnd]
	#print type(Clicks)
	#AppStart=ReqData.find(Clicks)
	#AppEnd=ReqData.find(
	#Applications=ReqData[AppStart+len('<td class="numeric">'):]
	#print Applications
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate
	#print findnth(ReqData,needle,5)
	
def Ripple_Bayard_Joveo_DE(raw_data,n): #n= The number of fields
	start_string = "Ripple - Bayard Joveo DE</a></td>"
	end_string = '<a href="/adverts/4992/adverts/26432/edit-rate?czid=30640">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate
	
def Ripple_Clickcast_DE(raw_data,n): #n= The number of fields
	start_string = "Ripple - Clickcast DE</a></td>"
	end_string = '<a href="/adverts/4992/adverts/25885/edit-rate?czid=30028">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate

def Ripple_Clickcast_JB(raw_data,n): #n= The number of fields
	start_string = "Ripple - Clickcast JB</a></td>"
	end_string = '<a href="/adverts/4992/adverts/26898/edit-rate?czid=31108">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate
	
def Ripple_Joveo_DE(raw_data,n): #n= The number of fields
	start_string = "Ripple - Joveo DE</a></td>"
	end_string = '<a href="/adverts/4992/adverts/29601/edit-rate?czid=34024">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate
	
def Ripple_Joveo_JB(raw_data,n): #n= The number of fields
	start_string = "Ripple - Joveo JB</a></td>"
	end_string = '<a href="/adverts/4992/adverts/29611/edit-rate?czid=34033">edit</a>'
	startData=raw_data.find(start_string)
	endData=raw_data.find(end_string)
	#print raw_data.find(start_string)
	ReqData = raw_data[startData+len(start_string):raw_data.find(end_string)-len(end_string)]
	needle='</td>'
	parts= ReqData.split(needle, n+1)
	Clicks1=parts[0]
	Clicks1=Clicks1[Clicks1.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Clicks1
	Apps=parts[1]
	Apps=Apps[Apps.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Apps
	Avg_CPC=parts[2].replace("$", "")
	Avg_CPC=Avg_CPC[Avg_CPC.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Avg_CPC
	Total=parts[3].replace("$", "")
	Total=Total[Total.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Total
	Current_Rate=parts[4].replace("$", "")
	Current_Rate=Current_Rate[Current_Rate.find('<td class="numeric">')+len('<td class="numeric">'):]
	print Current_Rate

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://advertiser.nexxt.com/')

# View available forms
for f in br.forms():
    print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)

# User credentials
br.form['UserName'] = 'kevin@ripplemedia.io'
br.form['Password'] = 'R!pple17'

# Login
br.submit()

raw_data=(br.open('https://advertiser.nexxt.com/adverts/4992/summary').read())
#print (raw_data)
fields = 5

Ripple_Bayard_Clickcast(raw_data,fields)
Ripple_Bayard_Joveo_DE(raw_data,fields)
Ripple_Clickcast_DE(raw_data,fields)
Ripple_Clickcast_JB(raw_data,fields)
Ripple_Joveo_DE(raw_data,fields)
Ripple_Joveo_JB(raw_data,fields)


