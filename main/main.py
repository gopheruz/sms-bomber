from send_script import startBomb

def sendSms():

    print("Sms bomber uzb\n")
    phone = input("Telefon raqam: (+998909546895): ")
    counter = input("Nechta sms jo'natasiz: ")
    
    if(len(phone) != 13 or phone.startswith("+")is not True): 
        print("Incorrect number!")
        return

    startBomb(phone, int(counter))
    
def main():
    sendSms()

if __name__ == "__main__":
    main()

