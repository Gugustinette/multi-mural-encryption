# multi-mural-encryption
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
        On this example, wall A is a basic Ceaser Cypher in Ascii, with a key from 1 to 9
        It'll just shift every character in a list, by 1 to 9, on the Ascii table
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
    In this example, a_value is always between 1 and 9 so there no need of ax
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
