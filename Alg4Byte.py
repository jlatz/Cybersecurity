'''
Created on Mar 4, 2020

@author: jlatz
'''

print('quit|encrypt|decrypt')
choice = input()

def quit():
    return "We will now quit"

def encrypt():
    print("Message: ")
    msg = input()
    print("Key:")
    key = input()
    
    #removes all the white space from the string
    newMsg = msg.replace(" ", "") 
    newKey = key.replace(" ", "")
    
    #slices the string and stores all the values in a list
    msgArr = [newMsg[0:2], newMsg[2:4], newMsg[4:6], newMsg[6:8]]
    keyArr = [newKey[0:2], newKey[2:4], newKey[4:6], newKey[6:8]]
    
    #going to loop 4 times
    #for i in range(4):
    #need to get the value of the key to know how many times to loop
    keyDec = int(keyArr[0],16)
    print(keyDec)
    #every time it is shifted 8 bits it becomes the original message
    keyMod = keyDec % 8
    print(keyMod)
    #for k in range(keyMod):
    msgDec = int(msgArr[0], 16)
    msgBin = bin(msgDec)
    
    
    #takes off the 0b when the number is converted to binary
    sliceMsgBin = msgBin[2:]
    
    #calculates how many zeros to add to make the string an 8 bit number
    numZero = 10 - len(msgBin)
    
    #adds the zeros to the string to make the number 8 bits
    for j in range(numZero):
        sliceMsgBin = '0' + sliceMsgBin
        
    
    #print(sliceMsgBin)
    #print(sliceMsgBin[0])
    #want to check if the most significant bit is a 0 or a 1 
    if(sliceMsgBin[0] == '0'):
        sliceMsgBin[2] = '1'
        print(sliceMsgBin)
        print('in ZERO')
    else:
        print("in ONE") 
    
    
    return 'yes'

def decrypt():
    return "We will now decrypt"
     
def choice_switch(choice):
    switcher = {
        'quit': quit,
        'encrypt': encrypt,
        'decrypt': decrypt
    }
    #Get the function from switcher dictionary
    func = switcher.get(choice, lambda: "Invalid Choice")
    #Execute the function
    print(func())

choice_switch(choice) 

