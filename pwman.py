import hashlib,sys
ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
			 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			 '0123456789')
SECRET_KEY = 'rOast3dP_e4Nut5'

def getHexDigest(salt,plaintext):
	content = salt + plaintext
	
	return hashlib.sha256(content.encode('utf-8')).hexdigest()

def makePassword(service,master):
	salt = getHexDigest(SECRET_KEY,service)[:20]
	hsh = getHexDigest(salt,master)
	return ''.join((salt,hsh))

if sys.argv[1] == 'help':
	print('Put in service then secret')
	print('You can add the sym option at the end to include symbols')
	quit()

if len(sys.argv) == 4 and sys.argv[3] == 'sym':
	ALPHABET += '!@#$%^&*()-_'

def password(service,plaintext,length=10,alphabet=ALPHABET):
	raw_hexdigest = makePassword(service,plaintext)
	num = int(raw_hexdigest,16)
	num_chars = len(alphabet)
	chars = []
	while len(chars) < length:
		num,idx = divmod(num,num_chars)
		chars.append(alphabet[idx])
	return ''.join(chars)

print(password(sys.argv[1],sys.argv[2]))