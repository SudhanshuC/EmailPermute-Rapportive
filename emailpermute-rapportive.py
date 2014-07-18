#!/usr/bin/python
#Based Upon Email Permutator: https://docs.google.com/spreadsheet/ccc?key=0AoW7aksoVU98dGNFSUtfeXg4akpNTWM0Z2pHWjJzZUE
#Based upon the service Rapportive: http://www.rapportive.com/
#Credits: This code is based upon the research and code of Jordan Wright.
#Blog Link: http://jordan-wright.github.io/blog/2013/10/14/automated-social-engineering-recon-using-rapportive/
#Code Link: https://github.com/jordan-wright/rapportive

import requests
fn=raw_input('Enter First Name: ')
mn=raw_input('Enter Middle Name: ')
ln=raw_input('Enter Last Name: ')
dm=raw_input('Enter Domain: ')

fi=fn[0]
if len(mn):
 mi=mn[0]
else:
 mi="" 
li=ln[0]
print ""

emaillist=[fn+'@'+dm,
ln+'@'+dm,
fn+ln+'@'+dm,
fn+'.'+ln+'@'+dm,
fi+ln+'@'+dm,
fi+'.'+ln+'@'+dm,
fn+li+'@'+dm,
fn+'.'+li+'@'+dm,
fi+li+'@'+dm,
fi+'.'+li+'@'+dm,
ln+fn+'@'+dm,
ln+'.'+fn+'@'+dm,
ln+fi+'@'+dm,
ln+'.'+fi+'@'+dm,
li+fn+'@'+dm,
li+'.'+fn+'@'+dm,
li+fi+'@'+dm,
li+'.'+fi+'@'+dm,
fi+mi+ln+'@'+dm,
fi+mi+'.'+ln+'@'+dm,
fn+mi+ln+'@'+dm,
fn+'.'+mi+'.'+ln+'@'+dm,
fn+mn+ln+'@'+dm,
fn+'.'+mn+'.'+ln+'@'+dm,
fn+'-'+ln+'@'+dm,
fi+'-'+ln+'@'+dm,
fn+'-'+li+'@'+dm,
fi+'-'+li+'@'+dm,
ln+'-'+fn+'@'+dm,
ln+'-'+fi+'@'+dm,
li+'-'+fn+'@'+dm,
li+'-'+fi+'@'+dm,
fi+mi+'-'+ln+'@'+dm,
fn+'-'+mi+'-'+ln+'@'+dm,
fn+'-'+mn+'-'+ln+'@'+dm,
fn+'_'+ln+'@'+dm,
fi+'_'+ln+'@'+dm,
fn+'_'+li+'@'+dm,
fi+'_'+li+'@'+dm,
ln+'_'+fn+'@'+dm,
ln+'_'+fi+'@'+dm,
li+'_'+fn+'@'+dm,
li+'_'+fi+'@'+dm,
fi+mi+'_'+ln+'@'+dm,
fn+'_'+mi+'_'+ln+'@'+dm,
fn+'_'+mn+'_'+ln+'@'+dm]


for email in emaillist:
  
	random_email="randome.mail@gmail.com"
	response = requests.get('https://rapportive.com/login_status?user_email=' + random_email).json()
	profile = requests.get('https://profiles.rapportive.com/contacts/email/' + email, headers = {'X-Session-Token' : response['session_token']}).json()
	print " "
	print "Results for Email: "+email
	print " "

	if profile['contact']['name']:
	  print "Name: "
	  print profile['contact']['name']
	  print " "

	if profile['contact']['location']:
	  print "Location: "
	  print profile['contact']['location']
	  print " "

	if profile['contact']['headline']:
	  print "Profile Headline: "
	  print profile['contact']['headline']
	  print " "

	if profile['contact']['occupations']:
	  print "Occupation(s): "
	  for occupation in profile['contact']['occupations']:
		print occupation['job_title']
		print occupation['company']
		print " "

	if profile['contact']['memberships']:
	  print "Membership(s): "
	  for membership in profile['contact']['memberships']:
		print membership['site_name']
		print membership['profile_url']
		print " "
	print " "
	print "*************************************"
	print " "
