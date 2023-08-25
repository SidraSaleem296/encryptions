import base64 
import time #decryption code is after the encryption code and will run after decommenting that code beacuse i have added it as a comment

#encryption

Characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

Characters = Characters.lower()

List_of_agents = ['Behemoth_arooj','Skipper_sana','Ghoul_hamde','Cryptonic_sid' ,'Drake_zeean ','Gloom_tanzeela','Diablo_areeba']

Barrac_codes = { 234,163,264,296,121,232,198,}

agent_name_check = (input('enter your agent/cover name :'))

print(agent_name_check)

barrac_code_check = eval(input('enter barrac code : '))

keyword_check = input("enter your specific keyword : ")

keyword = {'ONE ': "D",'SHOULD':"N",'READ': " E",'GOOD': "O",'INFORMTIVE':"T",'AWSOME': " K",'BOOKS ': "D"}

if keyword.get(keyword_check) != None: print("Well ! You have crossed the third check point ! Hurry up decode what team has sent \n Might be it''s urgent ")

elif agent_name_check in List_of_agents and barrac_code_check in Barrac_codes : print(' Hi BUDDY!!! Seems like YOU ARE OUR TEAM''S SPY')

else: print("SUSPICIOUS ACTIVITY ALERT !!!! \n SOMEONE OUT OF THE TEAM IS TRYING TO REACH OUT THE ENCRYPTION " "CODE \n you might forgot the barrac agent name \n Otherwise You are a spy \n CAUGHT YOU ")

check_point_4 = [] n = eval(input("Enter number of elements : ")) for i in range(0, n): elements = eval(input()) check_point_4.append(elements)

print(check_point_4) if check_point_4[3] == 20:

def encrypt(message, key):

    encrypted = ''
    for chars in message:
        if chars in Characters:
            num = Characters.find(chars)
            num += key
            encrypted += Characters[num]
    return encrypted


def main():

    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        (encrypt(message, key))

        plain_text = (encrypt(message, key))
        cipher_text = base64.b64encode(plain_text.encode())

        print(cipher_text.decode())

    else:
        print('warning !!!! who are u ? you are not from this team!!!')


if __name__ == '__main__':
    main()
    if time.time()>= 30 :
        start_time = time.time()
        main()
        print("%s seconds " % (time.time() - start_time))
        print('you took pretty less time ,just',"--- %s seconds ---" % (time.time() - start_time))
        print('you took pretty less time ,just',"--- %s seconds ---" % (time.time() - start_time))
        print('remember the codes and details carefully .You should not take that much time ')
        print('************************************')
        print('following are your details given ,plz remember next time ')
        print('Barrac code : ' , Barrac_codes)
        print('keyword :' , keyword_check)
        print('Agent name :' , agent_name_check)
        print('key_in_list: 20')
    else:
        start_time = time.time()
        main()
        print("%s seconds " % (time.time() - start_time))
        print('you took pretty much time ,',"--- %s seconds ---" % (time.time() - start_time))
        print('remember the codes and details carefully .You should not take that much time ')
        print('************************************')
        print('following are your details given ,plz remember next time ')
        print('Barrac code : ' , Barrac_codes)
        print('keyword :' , keyword_check)
        print('Agent name :' , agent_name_check)
        print('key_in_list:' , check_point_4)
else: print(('warning !!!! ENEMY : /' ' who are u ? /' 'you are not from this team!!!'))
