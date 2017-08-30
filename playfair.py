def matrix(key):
	matrix = []
	for e in key.upper():
		if e not in matrix:
			matrix.append(e)
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

	for e in alphabet:
		if e not in matrix:
			matrix.append(e)
	

	matrix_group=[]
	for e in range(5):
		matrix_group.append('')
	#print (matrix_group)

	for e in range(5):
		matrix_group[e] = matrix[5*e:5*e+5]
	print ("key matrix :%s" %(matrix_group));
	return matrix_group;

def digraphs(message_original):
	message = []
	for e in message_original:
		message.append(e)

	for space in range(len(message)):
		if " " in message:
			message.remove(" ")

	i=0
	for e in range(len(message)/2):
		if message[i]==message[i+1]:
			message.insert(i+1,'X')
		i=i+2

	if len(message)%2 == 1:
		message.append("X")

	i=0;
	new = []
	for x in xrange(1,len(message)/2 + 1):
		new.append(message[i:i+2])
		i=i+2
	print ("group of charector:%s" %(new));
	return new

def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			
			if key_matrix[i][j]==letter:
				
				x=i
				y=j
	return x,y

def encrypt(message):
	message = digraphs(message)
	key_matrix = matrix(key)
	#print key_matrix
	cipher=[]
	for e in message:
		#print e;
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		if(p1==p2):
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
				p2=-1;
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	return cipher

print "Playfair Cipher"
key = raw_input("Please input the key : ")
message = raw_input("Please input the message : ")
print "Encrypting message..."

print "Ciphering..."
var= encrypt(message)
#print "hdfjh"
output=""
for e in var:
	output+=e;
print output
