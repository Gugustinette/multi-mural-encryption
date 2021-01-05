message = "9639639639439639639639839639639639939639639639439639639639339639639639339639639639439639639639839639639639939639639639439639639639739639639639339639639639439639639639839639639639839639639639439639639639839639639639739639639639439639639639739639639639:3963963963943963963963973963963963953963963963943963963963983963963963983963963963943963963963963963963963993963963963943963963963963963963963993963963963943963963963983963963963983" #str(input("Enter a message to decode"))
key = "002012CADB-7236211013CBDA331053206" #str(input("Enter the key"))

def MM_Decrypt(encrypted_message, key) :
    def Decrypt(encrypted_message, key) :
        caraList = list(encrypted_message)

        a_value = 0
        b_value = 0
        d_value = 0

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

        def breakWallC(list_a) : # Re-Order Method
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

        def breakWallD(list_a, d_value) : # Break wall E (Oct Encryption)
            nbElement = len(list_a) // 3
            kLet = ''
            for i in range(len(list_a)) : # Convert into one big string
                kLet = str(kLet + list_a[i])
            kLet = UnShift(kLet, d_value) # UnShift
            list_a = Seperate(kLet, nbElement) # Seperate back into many elements of a string
            kLet = ''
            for i in range(len(list_a)) : # Convert back from oct
                kLet = chr(int(list_a[i], 8))
                list_a[i] = kLet
            return list_a

        def callDecrypt(list_a, str_input) : # Break wall depending of the string (A, B, C, ...)
            if str_input == 'A' :
                list_a = breakWallA(list_a, int(a_value))
            else :
                if str_input == 'B' :
                    list_a = breakWallB(list_a, int(b_value))
                else :
                    if str_input == 'C' :
                        list_a = breakWallC(list_a)
                    else :
                        list_a = breakWallD(list_a, int(d_value))
            return list_a

        def getValue(list_decrypt, offset, key, x) : # Add wall value to the list, using index of type bx (lenght of value number, before it)
            kLet = ''
            offset = 0
            y = int(key[x])
            for i in range(y) :
                kLet = str(kLet + key[x + i + 1])
                offset += 1
            list_decrypt.append(kLet)
            return list_decrypt, offset

        list_decrypt = []
        offset = 0

        x = 3

        for i in range(4) : # Get Order
            list_decrypt.append(key[x])
            x -= 1

        if key[4] == '-' :
            list_decrypt.append(-int(key[5])) # Get wall A value
            next_value = 6
        else :
            list_decrypt.append(key[4]) # Get wall A value
            next_value = 5

        list_decrypt, offset = getValue(list_decrypt, offset, key, next_value) # Get wall B value
        next_value += offset + 1
        list_decrypt, offset = getValue(list_decrypt, offset, key, next_value) # Get wall D value

        a_value = list_decrypt[4]
        b_value = list_decrypt[5]
        d_value = list_decrypt[6]

        print(list_decrypt)

        for i in range(4) : # Decrypt
            caraList = callDecrypt(caraList, list_decrypt[i])

        pMes = ''
        for i in range(len(caraList)) :
            pMes = str(pMes + caraList[i])

        return pMes

    decrypt_list = []

    force = int(key[0:3])

    decrypt_list.append(force)

    selected_value = 3

    for i in range(force) :
        wall_length_in_key = int(key[selected_value:selected_value + 3])
        decrypt_list.append(wall_length_in_key)
        decrypt_list.append(key[selected_value + 3:selected_value + 3 + wall_length_in_key])
        selected_value += 3 + wall_length_in_key

    mes_temp = ''
    mes_final = encrypted_message

    offset = force

    for n in range(force) :
        mes_temp = Decrypt(mes_final, decrypt_list[2*offset])
        mes_final = mes_temp
        print("Force " + str(n + 1) + " is done")
        offset -= 1

    return mes_final

original_message = MM_Decrypt(message, key)

print("Decrypted message is : ")
print(original_message)