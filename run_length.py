'''
Run-length encoding is a fast and simple method of encoding strings.
 The basic idea is to represent repeated successive characters as a single count and character.
 For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
 You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
  You can assume the string to be decoded is valid.

Written By Austin Bursey
Created On: 6/29/2020
Updated On: 6/29/2020
'''

def rl_encode(string) : 
    '''
    Params: 
        A plaintext string to be encoded. 
    
    Returns: 
        The ciphertext string encoded in run-length encoding 
    '''
    encoded_string = "" 
    n = len(string)
    char_length = 1
    last_char = string[0]
    for i in range(1 ,n) : 
        if last_char == string[i]: 
            char_length +=1 
        else : 
            encoded_string += str(char_length)
            encoded_string += last_char
            char_length = 1
        last_char = string[i]
    encoded_string += str(char_length)
    encoded_string += last_char
    return encoded_string

    
def rl_decode(string) : 
    '''
    Params: 
        A run-length encoded string or ciphertext string . 
    
    Returns: 
        The plaintext stringS
    '''
    decoded_string = ""
    n = len(string)
    digit = "" 
    for i in range(n ): 
        if string[i].isdigit() : 
            digit += string[i] 
        else : 
            decoded_string += int(digit) * string[i]
            digit = "" 
    return decoded_string

if __name__ == "__main__" : 

    string = "ABBBCCDA" 
    print("The plaintext String is :\n[%s] "%(string))

    #encoding
    encoded_string = rl_encode(string)
    print("The ciphertext encoded String is :\n[%s] "%(encoded_string))

    #decoding
    decoded_string = rl_decode(encoded_string)
    print("The plaintext decoded String is :\n[%s] "%(decoded_string))

