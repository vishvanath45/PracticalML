# see 
#   i/p   o/p
#  0 0 1   0
#  1 1 1   1
#  1 0 1   1
#  0 1 1   0
# see mai hamesha top left wala print kar raha
# par NN ko nahi pata. 

import numpy as np 
from numpy import *


# here input will be sum(xi*wi)
def sigmo(x):
	return 1/(1+np.exp(-x))

#here also input will be sum(xi*wi)
def sigmo_derivative(x):
	return exp(-x)/((1+exp(-x))*(1+exp(-x)))


training_input_arr = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
training_output_arr = array([[0,1,1,0]]).T

# print training_input_arr
# print training_output_arr

#seed me aise hi kuch likh do, bas yeh ki iske corresponding same random no
#hamesha generate karega
#relation aisa h ki same seed(beej) p same ped(random nos) aate h

np.random.seed(99)


#choosing initial weight
#yaha (3,1) ka matlab 3 #of ip, and 1# of op
#abhi yaha random.random [0,1) ki range ke deta h,
#muhje toh -1 se 1 ke chaiye isiliye *2 -1 kiya
weights = 2*random.random((3,1))-1


def kitna_sahi_kitna_galat(input):
	return sigmo(dot(input,weights))


#Training begins

for iteration in xrange(100000):
#sigmoid ne bola ki value -ve aa rahi h ya +ve
	output = kitna_sahi_kitna_galat(training_input_arr)
# abhi maine check kiya ki thik h asal value kya tha
	error = training_output_arr-output
# bas phir adjuct kiya ab
# yaha p dhyan dene wali baat h ki mujhe karna toh sirf error*value chahhiye tha but maine aakhir me
# rate of change of sigmoid (+ve se -ve ) ki taraf se bhi kiya. ( yeh cheeze bahut imp h.)

	adjustment = dot(training_input_arr.T , error*sigmo_derivative(dot(training_input_arr,weights)))
	weights += adjustment
	if (iteration%10000==0):
		print "~~~ weight adjusted ~~~"
		print weights


print "-----------------"
# finally kya weights aaye

# print weights

# yeh ek naye k liye test kiya
print "traning input was \n", training_input_arr
print "------"
print "training output was \n", training_output_arr
print "------"
# print "initial random weights choosen\n", duplicate_weights
# print "------"
print "final weights became\n", weights
print "------"
print "the answer for new input 1 0 0  is\n"
print kitna_sahi_kitna_galat(array([1,0,0]))

# _/\_
# https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1

