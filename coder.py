import unittest




###Unittesting
class Base64Tests(unittest.TestCase):
    def testEncoder(self):
        self.assertEqual(encode("Test"), "VGVzdA==", "Base64 encoder works fine!")
    def testDecoder(self):
        self.assertEqual(decode('VGVzdA=='), 'Test')


def main():
    unittest.main()

#Base64 dict
dict = {
    0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J', 10 : 'K', 11 : 'L',
    12 : 'M', 13 : 'N', 14 : 'O', 15 : 'P', 16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 20 : 'U', 21 : 'V', 22 : 'W',
    23 : 'X', 24 : 'Y', 25 : 'Z', 26 : 'a', 27 : 'b', 28 : 'c', 29 : 'd', 30 : 'e', 31 : 'f', 32 : 'g', 33 : 'h',
    34 : 'i', 35 : 'j', 36 : 'k', 37 : 'l', 38 : 'm', 39 : 'n', 40 : 'o', 41 : 'p', 42 : 'q', 43 : 'r', 44 : 's',
    45 : 't', 46 : 'u', 47 : 'v', 48 : 'w', 49 : 'x', 50 : 'y', 51 : 'z', 52 : '0', 53 : '1', 54 : '2', 55 : '3',
    56 : '4', 57 : '5', 58 : '6', 59 : '7', 60 : '8', 61 : '9', 62 : '+', 63 : '/', 64 : '='}

#Change letter to binary and append zeros to give length of 8
def to_binary(str):

    str_bin = format(ord(str), 'b')
    if len(str_bin) != 8:
        str_bin = (8 - len(str_bin))*'0' + str_bin
    return str_bin


#Encode passed string to base64 format
def encode(str):
    str_enc = ""

    mod = len(str) % 3

    for i in range(0, len(str)-mod, 3):
        s = ''
        for k in range(3):
            s += to_binary(str[i:i+3][k])

#   s var has 24 bits, divide it into groups of 4 bit and calculate value

        for k in range(0, len(s),6):
            str_enc += dict.get(int(s[k:k+6], 2))

    if(mod > 0):
        lst_bin = ''
        for s in str[-mod:]:
            lst_bin += to_binary(s)
        lst_bin += (3-mod)*8*'0'
        for k in range(0, len(lst_bin),6):
            l = int(lst_bin[k:k+6], 2)

            if k >= (18-6*mod) and l == 0:
                str_enc += '='
            else:
                str_enc += dict.get(l)

    return str_enc

def decode(str):
    equals_count = str.count('=')
    str_bin = ''
    for s in str:
        str_bin += find_in_dict(s)

    decoded = ''
    str_dec = str_bin[:len(str_bin)-8*equals_count]
    for i in range(0, len(str_dec), 8):
        decoded = decoded + chr(int(str_dec[i:i+8],2))

    return decoded



def find_in_dict(str_value):
    for index, value in dict.items():
        if value == str_value and index == 64:
            return 6*'0'
        elif value == str_value and index != 64:
            bin = str(format(index,'b'))
            if len(bin) != 6:
                bin = (6-len(bin)) * '0' + bin
            return bin



if __name__ == '__main__':
    main()
    # print 'My own base64 decoder/encoder'
    # res = encode("Test")
    # print res
    #
    # print int('10101110',2)
    print decode("VGVzdA==")




