# This is Number Converter written in Python

def DectoBin() :
    dec_num = input("Enter a decimal number :")
    
    try :
        bin_num = bin(int(dec_num)).replace("0b", "")  
        print("The binary value of {} is {}".format(dec_num,bin_num))

    except ValueError : 
        print("Invalid Decimal number !!")



def BintoDec() :
    bin_num = input("Enter a binary number :")

    try :
        dec_num = int(bin_num,2)  
        print("The decimal value of {} is {}".format(bin_num,dec_num))
    
    except ValueError :
        print("Invalid binary number !!")



def DectoOct() :
    dec_num = int(input("Enter a decimal number : "))

    try :
        oct_num = oct(dec_num).replace("0o","")
        print("The octal value of {} is {}".format(dec_num,oct_num))
    
    except ValueError :
        print("Invalid Decimal Number !!")


def OcttoDec() :
    oct_num = input("Enter octal number : ")
    
    try :
        dec_num = int(oct_num,8)
        print("The decimal value of {} is {}".format(oct_num,dec_num))

    except ValueError :
        print("Invalid Octal Number !!")



def DectoHex() :
    dec_num = int(input("Enter a decimal number : "))

    try :
        hex_num = hex(dec_num).replace("0x","")
        print("The hexadecimal value of {} is {}".format(dec_num,hex_num))
    
    except ValueError :
        print("Invalid Decimal Number !!")


def HextoDec() :
    hex_num = input("Enter hexadecimal number : ")

    try :
        dec_num = int(hex_num,16)
        print("The decimal value of {} is {}".format(hex_num,dec_num))

    except ValueError:
        print("Invalid HexaDecimal Number !!")



def Main() :

    print("Enter the option you want to perform")
    print("1: Decimal to Binary")
    print("2: Binary to Decimal")
    print("3: Decimal to Octal")
    print("4: Octal to Decimal")
    print("5: Decimal to Hexa-Decimal")
    print("6: Hexa-Decimal to Decimal")
    opt = int (input("Enter the option : "))

    if opt == 1 : DectoBin()    
        
    elif opt == 2 : BintoDec()

    elif opt == 3 : DectoOct()

    elif opt == 4 : OcttoDec()

    elif opt == 5 : DectoHex()

    elif opt == 6 : HextoDec()

    else :
        print("OOPS !!")
        print("Please check your input.")




if __name__ == "__main__" :
    Main()

