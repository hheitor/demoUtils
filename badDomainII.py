import dns.resolver
import random
import string

#here we genrate random characters

chars = string.ascii_letters.lower()+ string.digits

# then we set the bigip GTM virtual server that will be rx bad domain queries
DNS = dns.resolver.Resolver()
DNS.nameservers = ['10.1.10.201']
# if VS it nos answering, this will stop execution due to timeout error. 

# define a TLD to attach at the end of  the hostnames we're dynamically generating
#+ we can add all TLDs in the future as an array an  then add it to the join 

dom = ".co"

#initializing shit

j = 0

# here we start genrating random hostnames, attaching '.co' at then end of them #+ an put in all this in a query directed to our VS that has DNS configured.
   
print "these are de Random generated domains\n\n"
while j < 102:

        name = ''.join(random.choice(chars) for i in range (6))
        badDomain = ''.join((name,dom))
	from dns.resolver import NXDOMAIN
	try:
        		query = dns.resolver.query(badDomain, 'A')
			print "WHOOOOOAAAAA i didn't expect this to resolve"
	except NXDOMAIN:
        		print " looking for C&C server on------>", badDomain,"but it doesn't exist :( "

        j+=1
print "End of execution"
