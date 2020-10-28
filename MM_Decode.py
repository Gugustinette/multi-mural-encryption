message = "133303033333133333033333037303133313136373133333037333036373132303033333" #str(input("Enter a message to decode"))
key = "ACEBD-7216237717" #str(input("Enter the key"))

caraList = list(message)

a_value = 0
b_value = 0
c_value = 0
e_value = 0

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

def Even(nb) : # Take a number, true if even, false if odd
    if nb % 2 == 0 :
        return True
    else :
        return False

def CutElements(list_a) : # Divide elements of many character into many elements of one character
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

def UnShift(str_input, value) : # Shift all characters of a string back by a certain value (return a string)
    y = value
    fLet = ''
    x = y
    for i in range(len(str_input) - value) :
        fLet = str(fLet + str_input[x])
        x += 1
    for i in range(value) :
        fLet = str(fLet + str_input[i])
    return fLet

def Seperate(str_input, nbElement) : #Seperate a string into x element (of equal number of character) in a list (return a list)
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

def breakWallA(list_a, a_value) : # Break wall A (Ceasar Method)
    for i in range(len(list_a)):
        kLet = ord(list_a[i])
        kLet -= a_value
        list_a[i] = chr(kLet)
    list_a = CutElements(list_a)
    return list_a

def breakWallB(list_a, b_value) : # Break wall B (Hex Encryption)
    nbElement = len(list_a) // 2
    kLet = ''
    for i in range(len(list_a)) : # Convert into one big string
        kLet = str(kLet + list_a[i])
    kLet = UnShift(kLet, b_value) # UnShift
    list_a = Seperate(kLet, nbElement) # Seperate back into many elements of a string
    kLet = ''
    for i in range(len(list_a)) : # Convert back from hex
        kLet = bytes.fromhex(list_a[i]).decode('utf-8', errors='ignore')
        list_a[i] = kLet
    return list_a

def breakWallC(list_a, c_value, nb_char_per_binary) : # Break wall C (Binary)
    nbElement = len(list_a)
    for i in range(len(list_a)) : # Convert to binary
        kLet = bin(ord(list_a[i])).replace('0b', '')
        if len(kLet) < nb_char_per_binary : # Make binary longer if needed (0010 instead of 10)
            kLet = ToMaxChar(kLet, nb_char_per_binary)
        list_a[i] = kLet
    fLet = ''
    for i in range(len(list_a)) : # Convert into one big string
        fLet = str(fLet + list_a[i])
    fLet = UnShift(fLet, c_value) # UnShift the string
    list_a = Seperate(fLet, nbElement) # Seperate the string back into a list
    for i in range(len(list_a)) : # Convert every binary element to string
        kLet = list_a[i]
        kLet = BinaryToString(int(kLet))
        list_a[i] = kLet
    return list_a

def breakWallD(list_a) : # Re-Order Method
    if Even(len(list_a)) :
        d_value = len(list_a) // 2
    else : # Odd
        d_value = (len(list_a) - 1) // 2
    x = 0
    for i in range(d_value) :
        stock = list_a[x]
        list_a[x] = list_a[x + 1]
        list_a[x + 1] = stock
        x += 2
    return list_a

def breakWallE(list_a, e_value) : # Break wall E (Oct Encryption)
    nbElement = len(list_a) // 3
    kLet = ''
    for i in range(len(list_a)) : # Convert into one big string
        kLet = str(kLet + list_a[i])
    kLet = UnShift(kLet, e_value) # UnShift
    list_a = Seperate(kLet, nbElement) # Seperate back into many elements of a string
    kLet = ''
    for i in range(len(list_a)) : # Convert back from oct
        kLet = chr(int(list_a[i], 8))
        list_a[i] = kLet
    return list_a

def callDecrypt(list_a, str_input) : # Break wall depending of the string (A, B, C, ...)
    global a_value, b_value, max_char_binary, c_value, e_value
    if str_input == 'A' :
        list_a = breakWallA(list_a, int(a_value))
    else :
        if str_input == 'B' :
            list_a = breakWallB(list_a, int(b_value))
        else :
            if str_input == 'C' :
                list_a = breakWallC(list_a, int(c_value), int(max_char_binary))
            else :
                if str_input == 'D' :
                    list_a = breakWallD(list_a)
                else :
                    list_a = breakWallE(list_a, int(e_value))
    return list_a

def getValue(x) : # Add wall value to the list, using index of type bx (lenght of value number, before it)
    global list_decrypt, offset, key
    kLet = ''
    offset = 0
    y = int(key[x])
    for i in range(y) :
        kLet = str(kLet + key[x + i + 1])
        offset += 1
    list_decrypt.append(kLet)
    return list_decrypt

list_decrypt = []
offset = 0

x = 4
for i in range(5) : # Get Order
    list_decrypt.append(key[x])
    x -= 1

if key[5] == '-' :
    list_decrypt.append(-int(key[6])) # Get wall A value
    next_value = 7
else :
    list_decrypt.append(key[5]) # Get wall A value
    next_value = 6

list_decrypt = getValue(next_value) # Get wall B value
next_value += offset + 1
list_decrypt = getValue(next_value) # Get wall C value
next_value += offset + 2
list_decrypt.append(key[next_value - 1]) # Get max_char_binary value
list_decrypt = getValue(next_value) # Get wall E value

a_value = list_decrypt[5]
b_value = list_decrypt[6]
c_value = list_decrypt[7]
max_char_binary = list_decrypt[8]
e_value = list_decrypt[9]

print(list_decrypt)

for i in range(5) : # Decrypt
    caraList = callDecrypt(caraList, list_decrypt[i])

pMes = ''
for i in range(len(caraList)) :
    pMes = str(pMes + caraList[i])

print("Decrypted list is : ")
print(caraList)

print("Decrypted message is : ")
print(pMes)