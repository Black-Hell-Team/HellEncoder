import os
import base64
import requests
import time

def main():
    os.system("clear")
    print('''\033[1;31m
 __ __ __ __ __ __ __ __ __ /__\  
|__|__|__|__|__|__|__|__|__| \/ | 
| | | |                     \__/  
| | | |                           
|_| |_| 

\033[1;36m[\033[1;35m01\033[1;36m] \033[1;35mBase64
\033[1;36m[\033[1;35m02\033[1;36m] \033[1;35mMD5
\033[1;36m[\033[1;35m03\033[1;36m] \033[1;35mMD4
\033[1;36m[\033[1;35m04\033[1;36m] \033[1;35mBase16
\033[1;36m[\033[1;35m05\033[1;36m] \033[1;35mBack/Credits
''')

    op = input("\033[1;93m>\033[1;92m>\033[1;36m>\033[1;34m ")
    
    if op == '01' or op == '1':
        os.system("clear")
        print('''\033[1;93m
██████╗  █████╗ ███████╗███████╗     ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██║  ██║
██████╔╝███████║███████╗█████╗      ███████╗ ███████║
██╔══██╗██╔══██║╚════██║██╔══╝      ██╔═══██╗╚════██║
██████╔╝██║  ██║███████║███████╗    ╚██████╔╝     ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝      ╚═╝
''')
        message = input("\033[1;36mEnter the text you want to encode:\033[1;93m ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(f'\n\033[1;92mEncoded text: {base64_message}\n')

        back = input("\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ")
        if back == 'Y' or back == 'y':
            main()
        
        else:
            os.system("clear")
            exit()

    elif op == '02' or op == '2':
        os.system("clear")
        print('''\033[1;93m
███╗   ███╗██████╗ ███████╗
████╗ ████║██╔══██╗██╔════╝
██╔████╔██║██║  ██║███████╗
██║╚██╔╝██║██║  ██║╚════██║
██║ ╚═╝ ██║██████╔╝███████║
╚═╝     ╚═╝╚═════╝ ╚══════╝
''')
        md5 = input("\033[1;36mEnter the text to generate a hash:\033[1;93m ")
        request = requests.get('https://api.hashify.net/hash/md5/hex?value={}'.format(md5))
        address_data = request.json()

        if 'erro' not in address_data:
            print('\n\033[1;92mHash: {}\n'.format(address_data['Digest']))

        back = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')
        if back == 'Y' or back == 'y':
            main()

        else:
            os.system("clear")
            exit()

    elif op == '03' or op == '3':
        os.system("clear")
        print('''\033[1;93m
███╗   ███╗██████╗ ██╗  ██╗
████╗ ████║██╔══██╗██║  ██║
██╔████╔██║██║  ██║███████║
██║╚██╔╝██║██║  ██║╚════██║
██║ ╚═╝ ██║██████╔╝     ██║
╚═╝     ╚═╝╚═════╝      ╚═╝
''')

        md4 = input("\033[1;36mEnter the text to generate a hash:\033[1;93m ")
        request = requests.get('https://api.hashify.net/hash/md4/hex?value={}'.format(md4))
        address_data = request.json()

        if 'erro' not in address_data:
            print('\n\033[1;92mHash: {}\n'.format(address_data['Digest']))

        back = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')
        if back == 'Y' or back == 'y':
            main()

        else:
            os.system("clear")
            exit()

    elif op == '04' or op == '4':
        os.system("clear")
        print('''\033[1;93m
██████╗  █████╗ ███████╗███████╗     ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ███║██╔════╝ 
██████╔╝███████║███████╗█████╗      ╚██║███████╗ 
██╔══██╗██╔══██║╚════██║██╔══╝       ██║██╔═══██╗
██████╔╝██║  ██║███████║███████╗     ██║╚██████╔╝
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═╝ ╚═════╝
''')
        data = input("\033[1;36mEnter the text you want to encode:\033[1;93m ")
        encoded = data.encode("utf-8")
        b16 = base64.b16encode(encoded)
        print(f"\n\033[1;92mEncoded text: {b16}\n")

        back = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')
        if back == 'y' or back == 'Y':
            main()

        else:
            os.system("clear")
            exit()
    elif op == '05' or op == '5':
        os.system("clear")
        print('''\033[1;31m
____  _            _      _   _      _ _   _____                    
| __ )| | __ _  ___| | __ | | | | ___| | | |_   _|__  __ _ _ __ ___  
|  _ \| |/ _` |/ __| |/ / | |_| |/ _ \ | |   | |/ _ \/ _` | '_ ` _ \ 
| |_) | | (_| | (__|   <  |  _  |  __/ | |   | |  __/ (_| | | | | | |
|____/|_|\__,_|\___|_|\_\ |_| |_|\___|_|_|   |_|\___|\__,_|_| |_| |_|\n

\033[1;36mTeam:\033[1;32m Black Hell Team
\033[1;36mCoded by:\033[1;32m Near Shelby (Leader)
\033[1;36mTeam YT channel:\033[1;32m https://www.youtube.com/channel/UCFdCJf8YKHvOuWu2UxRI1fg
\033[1;36mGithub ORG:\033[1;32m https://github.com/Black-Hell-Team
\033[1;36mCountry:\033[1;32m Brazil
''')
    
    else:
        os.system("clear")
        print('\033[1;31mInvalid option')
        time.sleep(1.0)
        main()

main()
