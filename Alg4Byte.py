'''
Created on Mar 4, 2020
Completed on Mar 31, 2020

@author: john_latz
'''

#infinite loop
while True:
    
    print('quit|encrypt|decrypt')
    choice = input()

    #if quit is inputed, exit the program
    def quit():
        exit()

    #encrypt the message
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
    
        #going to loop 4 times for the 4 pairs of 2 bits
        for i in range(4):
            #convert the hex number to an integer, then to binary
            msgDec = int(msgArr[i], 16)
            msgBin = bin(msgDec)
    
    
            #takes off the 0b when the number is converted to binary
            sliceMsgBin = msgBin[2:]
    
            #calculates how many zeros to add to make the string an 8 bit number
            numZero = 10 - len(msgBin)
    
            #adds the zeros to the string to make the number 8 bits
            j = 0
            while j < numZero:
                sliceMsgBin = '0' + sliceMsgBin
                j += 1
        
            #need to get the value of the key to know how many times to loop
            keyDec = int(keyArr[i],16)
            #every time it is shifted 8 bits it becomes the original message
            keyMod = keyDec % 8
    
            k = 0
            #logic for rotating the bits
            while k < keyMod:
                #want to check if the most significant bit is a 0 or a 1 
                #rolling the bits to the left
                if(sliceMsgBin[0] == '0'):
                    #if bit is a 0, remove it from the first position and add it to the last position
                    list1 = list(sliceMsgBin)
                    list1[0] = ''
                    sliceMsgBin = ''.join(list1)
                    sliceMsgBin = ''.join(('',sliceMsgBin, '0'))
                else:
                    #if the bit is a 1, remove it from the first position and add it ot the last position
                    list1 = list(sliceMsgBin)
                    list1[0] = ''
                    sliceMsgBin = ''.join(list1)
                    sliceMsgBin = ''.join(('',sliceMsgBin, '1'))                
                k += 1 
        
            msgArr[i] = sliceMsgBin
    
        #stores the 32bit binary number
        totalMsg = msgArr[3] + msgArr[2] + msgArr[1] + msgArr[0]
    
        #now we want to rotate the bits to the right based on the keyArr[0] value
        
        #convert from hex to integer
        keyDec = int(keyArr[0],16)
        
        #every time it is shifted 32 bits it becomes the original message
        keyMod = keyDec % 32  
    
        #logic for rotating the bits
        m = 0 
        while m < keyMod:
            #want to check if the least significant bit is a 0 or a 1 
            if(totalMsg[31] == '0'):
                #if lsb is a 0 remove it and make it the msb
                list1 = list(totalMsg)
                list1[31] = ''
                totalMsg = ''.join(list1)
                totalMsg = ''.join(('0',totalMsg, ''))
            else:
                #if the lsb is a 1 remove it and make it the msb
                list1 = list(totalMsg)
                list1[31] = ''
                totalMsg = ''.join(list1)
                totalMsg = ''.join(('1',totalMsg, ''))        
            m += 1
        
        #parse the total message
        totalMsgArr = [totalMsg[0:8], totalMsg[8:16], totalMsg[16:24], totalMsg[24:32]]
    
    
        #change the keyArr from hex to all binary values
        totalKeyArr = []
        for h in range(4):
            
            #loop through the entire keyArr, convert hex to integer then to binary
            keyDec = int(keyArr[h], 16)
            keyBin = bin(keyDec)
    
            #takes off the 0b when the number is converted to binary
            sliceKeyBin = keyBin[2:]
            numsZero = 10 - len(keyBin)
            #adds the zeros to the string to make the number 8 bits
    
            p = 0
            while p < numsZero:
                sliceKeyBin = '0' + sliceKeyBin
                p += 1
            
            totalKeyArr.append(sliceKeyBin)
        
        
        finishedKeyArr = totalKeyArr[3] + totalKeyArr[2] + totalKeyArr[1] + totalKeyArr[0] 
        finishedMsgArr = totalMsgArr[3] + totalMsgArr[2] + totalMsgArr[1] + totalMsgArr[0]
        
        #exclusive or operation
        encodeMsg = str(int(finishedKeyArr) ^ int(finishedMsgArr))
        
        '''
        #exclusive or operation
        encodeMsg = []
        for q in range(4):
            encodeMsg.append(str(int(totalKeyArr[q]) ^ int(totalMsgArr[q])))
            
        #convert each value back into hex
        
        encodedMsg = ''
        for w in range(4):
            decimalMsg = int(encodeMsg[w], 2)
            hexMsg = hex(decimalMsg)
            encodedMsg += hexMsg + " "
        
        return encodedMsg
        '''
        return encodeMsg 
    def decrypt():
        print("Cipher: ")
        cipher = input()
        print("Key:")
        key = input()
    
        #removes all the white space from the string
        newMsg = cipher.replace(" ", "") 
        newKey = key.replace(" ", "")
    
        #parses the keyArr into 4 pairs of 2
        keyArr = [newKey[0:2], newKey[2:4], newKey[4:6], newKey[6:8]]
    
        #convert the key array into an array of binary values 
        totalKeyArr = []
        for h in range(4):
            keyDec = int(keyArr[h], 16)
            keyBin = bin(keyDec)
    
            #takes off the 0b when the number is converted to binary
            sliceKeyBin = keyBin[2:]
            
            #calculates the number of 0s to add
            numsZero = 10 - len(keyBin)
            
            #adds the zeros to the string to make the number 8 bits
            p = 0
            while p < numsZero:
                sliceKeyBin = '0' + sliceKeyBin
                p += 1
            
            totalKeyArr.append(sliceKeyBin)
        
        #store the array as a 32 bit string
        finishedKeyArr = totalKeyArr[3] + totalKeyArr[2] + totalKeyArr[1] + totalKeyArr[0]
        
        #get the encoded msg by doing another xor operation
        decrypt = int(newMsg) ^ int(finishedKeyArr)
        strDecrypt = str(decrypt)
        zeroNum = 32 - len(strDecrypt)
    
        #adds the zeros to the string to make the number 32 bits
        j = 0
        while j < zeroNum:
            strDecrypt = '0' + strDecrypt
            j += 1
        
            
        keyDec = int(keyArr[0],16)
        #every time it is shifted 32 bits it becomes the original message
        keyMod = keyDec % 32  
    
        m = 0
        #logic for rotating the bits 
        while m < keyMod:
            #want to rotate the bits to the left first
            #want to check if the most significant bit is a 0 or a 1 
            if(strDecrypt[0] == '0'):
                #if the msb is a 0, remove it and add it to the lsb
                list1 = list(strDecrypt)
                list1[0] = ''
                strDecrypt = ''.join(list1)
                strDecrypt = ''.join(('',strDecrypt, '0'))
            else:
                #if the msb is a 1, remove it and add it to the lsb
                list1 = list(strDecrypt)
                list1[0] = ''
                strDecrypt = ''.join(list1)
                strDecrypt = ''.join(('',strDecrypt, '1'))        
            m += 1
    
        #puts the array back in terms of [0],[1],[2],[3]
        totalMsgArr = [strDecrypt[24:32], strDecrypt[16:24], strDecrypt[8:16], strDecrypt[0:8]]
    
        for i in range(4):
            #need to get the value of the key to know how many times to loop
            keyDec = int(keyArr[i],16)
        
            #every time it is shifted 8 bits it becomes the original message
            keyMod = keyDec % 8
        
            #store the index value in a temp variable
            sliceMsgBin = totalMsgArr[i]
            
            #logic for rotating the bits
            k=0
            while k < keyMod:
                #want to check if the least significant bit is a 0 or a 1 
                if(sliceMsgBin[7] == '0'):
                    #if lsb is a 0, remove it and add it to msb
                    list1 = list(sliceMsgBin)
                    list1[7] = ''
                    sliceMsgBin = ''.join(list1)
                    sliceMsgBin = ''.join(('0',sliceMsgBin, ''))
                else:
                    #if lsb is a 1, remove it and add it to msb
                    list1 = list(sliceMsgBin)
                    list1[7] = ''
                    sliceMsgBin = ''.join(list1)
                    sliceMsgBin = ''.join(('1',sliceMsgBin, '0'))
                k += 1 
        
            #add the value to the array
            totalMsgArr[i] = sliceMsgBin
        
        #convert the values to hexadecimal 
        decodedMsg = ''
        for q in range(4):
            decimalMsg = int(totalMsgArr[q], 2)
            hexMsg = hex(decimalMsg)
            decodedMsg += hexMsg + " "

        #returns the decoded message
        return decodedMsg
    
    
    #function to control which option is chosen     
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

    #calls the function
    choice_switch(choice) 
