import sys 

def suma(a,b):
    return a+b

if __name__=='__main__':
    if (sys.argv[1])=="suma":
        print(f"\nLa suma de {sys.argv[2]} y {sys.argv[3]} es ",suma(int(sys.argv[2]),int(sys.argv[3])))
    else: print("\nAlgo ha fallado")