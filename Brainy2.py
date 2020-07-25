#!/usr/bin/python3
#===============================================
#________------Open--source_______________--
#
#==========___author_NIght_KIng_
#telegram : https://t.me/chill_vibez
#git    : http://github.com/David-848
#=====================================
#-----------//////////////modules///////////
import hashlib
#//////////////////modules///////////////
print("\033[94m")
print("      _---~~(~~-_.")
print("    _{        )   )")
print("  ,   ) -~~- ( ,-' )_")
print(" (  `-,_..`., )-- '_,)")
print("( ` _)  (  -~( -_ `,  }")
print("(_-  _  ~_-~~~~`,  ,' )")
print("  `~ -^(    __;-,((()))")
print("       ~~~~ {_ -_(())")
print("              `\  }")
print("                { }            \033[mv2.0")
print("[~]Made with \033[94m<3\033[m by \033[92mNIght KIng\033[m")
#------------------///show category/////---------
try:
    category = input("\033[92m[1]\033[mHash a Value\n\033[92m[2]\033[mDe-hash a Value\n[~]Destination: ")
except KeyboardInterrupt:
    exit('\033[91m\nprogram broken\033[m')
if category=="":
    exit('\033[91m\nInvalid Input\033[m')
elif category=="1":
    print("[~]HASH A VALUE")
    cat1 = input("\033[92m[1]\033[mMD5\n\033[92m[2]\033[mSHA1\n\033[92m[3]\033[mSHA224\n\033[92m[4]\033[mSHA256\n\033[92m[5]\033[mSHA384\n[~]Enter Command: ")
    print(cat1)
    if cat1=="":
        exit('\033[91m\nInvalid Input\033[m')
    elif cat1=="1":
        def md5_1():
            user_in = input(str("Enter Value: "))
            password = hashlib.md5()
            password.update(user_in.encode("utf-8"))
            return password.hexdigest()
        print(md5_1())
    elif cat1=="2":
        def sha1_1():
          user_1 = input(str("Enter Value: "))
          password = hashlib.sha1()
          password.update(user_1.encode("utf-8"))
          return password.hexdigest()
        print(sha1_1())
    elif cat1=="3":
        def sha224():
            user_2 = input(str("Enter Value: "))
            password = hashlib.sha224()
            password.update(user_2.encode("utf-8"))
            return password.hexdigest()
        print(sha224())
    elif cat1=="4":
        def sha256():
            user_3 = input(str("Enter Value: "))
            password = hashlib.sha256()
            password.update(user_3.encode("utf=8"))
            return password.hexdigest()
        print(sha256())
    elif cat1=="5":
        def sha384():
            usr_4 = input(str("Enter Value: "))
            password = hashlib.sha384()
            password.update(usr_4.encode("utf=8"))
            return password.hexdigest()
        print(sha384())
    else:
        exit('\033[91m\nInvalid Input\033[m')
if category=="2":
    print("DE-HASH VALUE")
    cat2 = input("\033[92m[1]\033[mMD5\n\033[92m[2]\033[mSHA1\n\033[92m[3]\033[mSHA224\n\033[92m[4]\033[mSHA256\n\033[92m[5]\033[mSHA384\n\033[92m[~]\033[mEnter Command: ")
    print(cat2)
    if cat2=="":
        exit('\033[91m\nInvalid Input\033[m')
    elif cat2=="1":
        place = 0
        va_lu = input("Enter Hash: ")
        fi_le = input("Enter filename: ")
        f_dir = open(fi_le,'r')
        for word in f_dir:
            enc_wrd = word.encode('utf-8')
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest == va_lu:
            print("\033[92m[+]\033[mpassword found")
            print("\033[92m[+]\033[mpassword is " + word)
            place = 1
            exit()
        if place == 0:
            print("\033[91m[!!!]\033[mpassword not in list")
    elif cat2=="2":
        land = 0
        v_al = input("Enter Hash: ")
        f_il = input("Enter filename:")
        f_id = open(f_il,'r')
        for word in f_id:
            en_wrd = word.encode('utf-8')
            chew = hashlib.sha1(en_wrd.strip()).hexdigest()
        if chew == v_al:
            print("\033[92m[+]\033[mpassword found")
            print("\033[92m[+]\033[mpassword is " + word)
            land = 1
            exit()
        if place == 0:
            print("\033[91m[!!!]\033[mpassword not in list")
    elif cat2=="3":
        zoo = 0
        usr_1 = input("Enter Hash: ")
        file_1 = input("Enter filename: ")
        file_cut = open(file_1,'r')
        for word in file_cut:
            ec_wrd = word.encode('utf-8')
            chase = hashlib.sha224(ec_wrd.strip()).hexdigest()
        if chase == usr_1:
            print("\033[92m[+]\033[mpassword found")
            print("\033[92m[+]\033[mpassword is " + word)
            zoo = 1
            exit()
        if zoo == 0:
            print("\033[91m[!!!]\033[mpassword not in list")
    elif cat2=="4":
        farm = 0
        usr_2 = input("Enter Hash: ")
        file_2 = input("Enter filename: ")
        file_break = open(file_2,'r')
        for word in file_break:
            cry_wrd = word.encode('utf-8')
            catch = hashlib.sha256(cry_wrd.strip()).hexdigest()
        if catch == usr_2:
            print("\033[92m[+]\033[mpassword found")
            print("\033[92m[+]\033[mpassword is " + word)
            farm = 1
            exit()
        if farm == 0:
            print("\033[91m[!!!]\033[mpassword not in list")
    elif cat2=="5":
        yard = 0
        usr_3 = input("Enter Hash: ")
        file_3 = input("Enter filename: ")
        file_crush = open(file_3,'r')
        for word in file_crush:
            key_wrd = word.encode('utf-8')
            roast = hashlib.sha384(key_wrd.split()).hexdigest()
        if roast == usr_3:
            print("\033[92m[+]\033[mpassword found")
            print("\033[92m[+]\033[mpassword is " + word)
            yard = 1
            exit()
        if yard == 0:
            print("\033[91m[!!!]\033[mpassword not in list")
    else:
        exit('\033[91m\nInvalid Input\033[m')
