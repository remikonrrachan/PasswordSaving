def Wirte():
    f = open('D:\password(remake).txt', 'w') #สามารถเปลี่ยนแปลงที่อยู่ในการจัดเก็บ file ได้
    P_label=int(input('How many do you want to save: '))
    for i in range(1,P_label+1):
        print('Program',i)
        name=input('Name: ')
        ID=input('ID: ')
        Password=input('Password:')
        f.write(name+','+ID+','+Password+'\n')
    f.close()
def Wirte_More():
    f = open('D:\password(remake).txt', 'a+') #สามารถเปลี่ยนแปลงที่อยู่ในการจัดเก็บ file ได้
    P_label=int(input('How many do you want to save: '))
    for i in range(1,P_label+1):
        print('Program',i)
        name=input('Name: ')
        ID=input('ID: ')
        Password=input('Password:')
        f.write(name+','+ID+','+Password+'\n')
    f.close()

while True:
    Menu=input('Do you want to Create(1st time) Save file or Add more (1:Create,2:Add): ')
    if Menu=='1':
        Wirte()

    elif Menu =='2':
        Wirte_More()

    elif Menu =='check':
        Key_input =input('Input Keyword: ')
        f = open('D:\password(remake).txt', 'r')
        while True:
            s = f.readline()
            if s=='':
                break

            d = s.rstrip().split(',')
            word=Key_input
            if d[0]==word:
                print('ID: '+d[1]+'\n'+'Password: '+d[2])
                break
        f.close()

    elif Menu =='test':
        f = open('D:\password(remake).txt', 'r')
        while True:
            s = f.readline()
            if s == '':
                break

            d = s.rstrip().split(',')
            print('ID: ' + d[1] + '\n' + 'Password: ' + d[2])
        f.close()

    else :
        print("Please choose again")
        continue
    while True:
        CHECK=input('DO YOU WANT TO EXIT (Y/N): ')
        if CHECK =='y'or CHECK=='Y':
            exit()
        elif CHECK =='n'or CHECK=='N':
            break
        else:
            print("Please choose again")

#print(d[0])


