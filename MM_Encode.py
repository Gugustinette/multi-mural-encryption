import random

# Multi-Mural Encryption
"""
Explanation :

    Takes a string and return an encrypted one with its key
    Output is written on terminal and stored in a text file named "encrypt.txt"

    Basics :
    Multi-Mural Encryption (MM Encryption) is based on 2 concepts :
        - Number of Wall
        - Strength

    Number of wall :
        A wall is just a method of encryption, that allready exists
        First wall is wall A, second is wall B,...

        On this example, wall A is a basic Ceaser Cypher in Ascii, with a key from -9 to 9
        It'll just shift every character in a list, by -9 to 9, on the Ascii table

        The more wall you have, the more MM Encryption is powerfull

        The basic operation of MM Encryption is applying every wall in a random order with random values
        Then the key is just the order of the walls, with every values for each one

        Example (with 5 wall):
                ADCBE3112547225

                First 5 characters are the order of the walls,
                All others number are values for each walls, in the same order

    Strenght (not coded yet):
        The second concept is what makes MM Encryption powerfull

        Basic encryption method can't be used many times 'cause it would just loop
        First Ceaser cypher method as a limit, because it uses all 26 character of the alphabet

        Applying it many times doesn't make any sense, a key of 48 is purely a key of 22, which looped
        one time across the alphabet

        MM Encryption can be used many times with no problem, since it uses many different encryption method,
        which give different results depending on the order you apply these

        Then the strenght is just the number of time you apply the MM Encryption
        In this example, the force is 1.
Key :
    The key is of form :
        ABCDE ax + a_value + bx + b_value +...
        
        ABCDE correspond to the order of the wall, could be BCDAE, ACEDB,...

        a_value is the number which has been used to apply wall A
        ax then corresponed to the len of a_value, it is usefull when reading the key and decoding
        (-> if a_value is 897, ax will be 3 so you'll know 3 next numbers in key are a_value)

        a_value is called a "Wall Value"
        ax is called a "Len Value"

        Then :
            Key = Wall Order + Len Value 1 + Wall Value 1 + Len Value 2 + Wall Value 2 +...

    In this example, a_value is always between -9 and 9 so there no need of ax

    You can then personnalize the encryption, by adding other possibilities

    Here the wall C also output a value called "max_char_binary"
    Wall C uses binary form of character, so this value is used to know what's the biggest binary number
    in the message, and then make every character the same size
    (101 and 11001 will become : 00101 and 11001 so they're all the same size)

    max_char_binary does not use any value for its size since we're not using any binary
    bigger than 9 bits
Decrypting :
    Decrypting the message is fairly easy once you understand MM Encryption concept

    All you have to do is reversing the whole process :

        - Read the wall order part of the key upside down
        - Find the wall value using a loop
            If you want wall B's wall value :
                - Read wall A's len value
                - Go forward by len value + 1 in the key
                - You're on wall B's len value
                - Read it
                - Wall B's wall value is the next wall B's len value character
            Doing this process one time gives wall A wall value
            Doing this process two time gives wall B wall value
            ...
        - Apply the wall backward using the wall value
        - Do it for each wall
More :
    Output can takes many different forms and looks different, specially depending on which wall
    has been applied last
"""

# Takes the input message to encode
message = str(input("Give a message to encode"))

def Encrypt(message) :

    # Init the list
    caraList = list(message)

    key = ''

    a_value = ''
    b_value = ''
    b_len = ''
    d_value = ''
    d_len = ''

    max_char_binary = 0

    def BinaryToString(binary):  
            
        binary1 = binary  
        decimal, i, n = 0, 0, 0
        while(binary != 0):  
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)  
            binary = binary//10
            i += 1
        str_decimal = chr(decimal)
        return (str_decimal)

    def ToMaxChar(str_nb, nb_char) : # Add one or many zero before a number to make it longer (return the number as a string)
        x = nb_char - len(str_nb)
        for i in range(x) :
            str_nb = str('0' + str_nb)
        return str_nb

    def Even(nb) : # Return true if even, else false
        if nb % 2 == 0 :
            return True
        else :
            return False

    def CutElements(list_a) : # Divide elements of many character into many elements of one character (takes and return a list)
        x = 0
        y = 0
        g = 0
        for i in range(len(list_a)) :
            g = 0
            if len(list_a[x]) > 1 :
                aLet = list_a[x]
                list_a.pop(x)
                y = len(aLet) - 1
                for n in range(len(aLet)) :
                    list_a.insert(x, aLet[y])
                    y -= 1
                    g += 1
                x += g - 1
            x += 1
        return list_a

    def Shift(str_input, value) : # Shift all characters of a string by a certain value (return a string)
        y = value
        fLet = ''
        for i in range(value) :
            fLet = str(fLet + str_input[len(str_input) - y])
            y -= 1
        for i in range(len(str_input) - value) :
            fLet = str(fLet + str_input[i])
        return fLet

    def Seperate(str_input, nbElement) : # Seperate a string into x element (of equal number of character) in a list (return a list)
        list_s = []
        nbChar = len(str_input) // nbElement
        kLet = ''
        x = 0
        for i in range(nbElement) :
            for i in range(nbChar) :
                kLet = str(kLet + str_input[x])
                x += 1
            list_s.append(kLet)
            kLet = ''
        return list_s

    def wallA(list_a) : # -9 to 9 Ascii Ceasar Method (0 not included)
        a_value = random.randint(-9, 9)
        while a_value == 0 :
            a_value = random.randint(-9, 9)
        for i in range(len(list_a)):
            kLet = ord(list_a[i])
            kLet += a_value
            list_a[i] = chr(kLet)
        list_a = CutElements(list_a)
        return list_a, str(a_value)

    def wallB(list_a) : # Hex Encryption Shift
        nbElement = len(list_a)
        x = 0
        for i in range(len(list_a)): # Convert all element to hex
            kLet = hex(ord(list_a[x])).replace('0x', '')
            list_a[x] = kLet
            x += 1
        fLet = ''
        for i in range(len(list_a)) : # Make it one big string
            fLet = str(fLet + list_a[i])
        list_a = []
        b_value = random.randint(1, len(fLet) - 1)
        fLet = Shift(fLet, b_value) # Shift
        list_a = Seperate(fLet, nbElement) # Seperate back into many elements of a list
        list_a = CutElements(list_a) # Cut every elements of many character into many elements of one character
        return list_a, str(b_value)

    def wallC(list_a) : # Re-Order Method
        if Even(len(list_a)) :
            d_range = len(list_a) // 2
        else : # Odd
            d_range = (len(list_a) - 1) // 2
        x = 0
        for i in range(d_range) :
            stock = list_a[x]
            list_a[x] = list_a[x + 1]
            list_a[x + 1] = stock
            x += 2
        d_value = 1
        return list_a, str(d_value)

    def wallD(list_a) : #Octal Encryption Shift
        nbElement = len(list_a)
        for i in range(len(list_a)) : # Convert all element to oct
            kLet = oct(ord(list_a[i])).replace('0o', '')
            if len(kLet) < 3 :
                kLet = ToMaxChar(kLet, 3)
            list_a[i] = kLet
        fLet = ''
        for i in range(len(list_a)) : # Make it one big string
            fLet = str(fLet + list_a[i])
        list_a = []
        e_value = random.randint(1, len(fLet) - 1)
        fLet = Shift(fLet, e_value) # Shift
        list_a = Seperate(fLet, nbElement) # Seperate back into many elements of a list
        list_a = CutElements(list_a) # Cut every elements of many character into many elements of one character
        return list_a, str(e_value)

    def callEncrypt(list_a, str_input) : # Apply wall depending of the string (A, B, C, ...)
        if str_input == 'A' :
            list_a, key_value = wallA(list_a)
            wall_applied = 'A'
        else :
            if str_input == 'B' :
                list_a, key_value = wallB(list_a)
                wall_applied = 'B'
            else :
                if str_input == 'C' :
                    list_a, key_value = wallC(list_a)
                    wall_applied = 'C'
                else :
                    list_a, key_value = wallD(list_a)
                    wall_applied = 'D'
        return list_a, wall_applied, key_value

    list_wall = ['A', 'B', 'C', 'D']
    list_order = []

    for i in range(len(list_wall)) : # Initialize the order of the wall
        x = random.randint(0, len(list_wall) - 1)
        kLet = list_wall[x]
        list_wall.pop(x)
        list_order.append(kLet)

    wall_applied = ''
    key_value = 0

    for i in range(len(list_order)) : # Call the wall in order
        caraList, wall_applied, key_value = callEncrypt(caraList, list_order[i])
        if wall_applied == 'A' :
            a_value = key_value
        else :
            if wall_applied == 'B' :
                b_value = key_value
                b_len = len(b_value)
            else :
                if wall_applied == 'D' :
                    d_value = key_value
                    d_len = len(d_value)

    # Add wall order to the key
    for i in range(len(list_order)) :
        key = str(key + list_order[i])

    # Add wall values and len values to the key
    key = str(key + a_value)
    key = str(key + str(b_len))
    key = str(key + b_value)
    key = str(key + str(d_len))
    key = str(key + d_value)

    pMes = ''
    for i in range(len(caraList)) :
        pMes = str(pMes + caraList[i])

    return pMes, key

encrypted_message, key = Encrypt(message)

print("Encrypted message is : ")
print(encrypted_message)

print("Key is : ")
print(key)
