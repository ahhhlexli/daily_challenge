"""Make a function that encrypts a given input with these steps:

Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:

a => 0 e => 1 o => 2 u => 3
#"1lpp0" 

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"
encrypt("karaca") ➞ "0c0r0kaca"
encrypt("burak") ➞ "k0r3baca"
encrypt("alpaca") ➞ "0c0pl0aca" """

def encrypt(string):

    string = list(string[::-1])
    for i in range(len(string)):
        if string[i] == 'a':
            string[i] = '0'
        elif string[i] == 'e':
            string[i] = '1'
        elif string[i] == 'o':
            string[i] = '2'
        elif string[i] == 'u':
            string[i] = '3'
    string = ''.join(string) + 'aca'

    return string

print(encrypt('banana'))
print(encrypt('karaca'))
print(encrypt('burak'))
print(encrypt('alpaca'))
