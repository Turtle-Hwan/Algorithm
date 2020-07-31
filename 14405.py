#14405번 피카츄

S = input()

def pikachu():
    if(S[0:2] == 'pi'):
        if(len(S) == 2):
            print('YES')
            return
        else:
            S.lstrip('pi')
            pikachu()
            
    elif(S[0:2] == 'ka'):
        if(len(S) == 2):
            print('YES')
            return
        else:
            S.lstrip('ka')
            pikachu()
            
    elif(S[0:3] == 'chu'):
        if(len(S) == 3):
            print('YES')
            return
        else:
            S.lstrip('chu')
            pikachu()
    else:
        print('NO')
        return

pikachu()
