import os

def clear():
    os.system("cls")
    
def text(*text):
    print("\n" + "=" * 60 + "\n")
    print(text[0].center(60))
    print(*text[1:])
    
