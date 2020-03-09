'''
Created on Mar 4, 2020

@author: jlatz
'''

print('quit|encrypt|decrypt')
choice = input()

def quit():
    return "We will now quit"

def encrypt():
    return "We will now encrypt"

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
