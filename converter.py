# Convert message to int according to ASCII
def str2int(Input):
    s = ''
    for c in Input:
        temp = str(ord(c))
        if len(temp) < 3:
            temp = '0' + temp
        s = s + temp
    return int(s)

# Convert decrypted int to original message
def int2str(Input):
    s = ''
    while len(Input) != 0:
        temp = int(Input[-3:])
        s = chr(temp) + s
        Input = Input[:-3]
    return s

def converter():
    var = input("Convert String to Integer press 1\nConvert Integer to String press 2\n")
    if var in ["1", "2"]:
        Input = input("Type your input: ")
        if var == "1":
            print (str2int(Input))
        if var == "2":
            print (int2str(Input))
    else:
        print ("Invalid!")

if __name__ == "__main__":
    converter()
