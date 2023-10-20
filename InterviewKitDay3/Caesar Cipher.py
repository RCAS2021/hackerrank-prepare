def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in (s):
        if(char.isupper()):
            encrypted += alphabet[(ord(char) - ord("A") + k) % 26].capitalize() #Capitalize the letter -> 
                                                                                #ord gets the unicode of a specific letter, EX(A, 2):  ord(A) -> 65, 26 -> length(alphabet) /// (65 - 65 + 2) % 26 = 2
        elif(char.islower()):
            encrypted += alphabet[(ord(char) - ord("a") + k) % 26]
        else:
            encrypted += char
    print(encrypted)

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)