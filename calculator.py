import math
def calculator():
    print("welcome to scientific calculator")
    print("Available operations:+,-,*,/,sqrt,pow,sin,cos,tan,log")
    print("type 'exit' to stop\n")
    while True:
        op=input("enter operation")
        if op=="exit":
            print("exit program")
            break
        if op in ['+','-','*','/']:
            a=float(input("enter first number"))
            b=float(input("enter second number "))
            if op == '+':
                print("result",a+b)
            elif op == '-':
                print("resuit",a-b)
            elif op == '*':
                print("result",a*b)
            elif op == '/':
                print("result", "error"if b==0 else a/b)
                
        elif op =='sqrt':
            a=float(input("enter number :"))
            print("result",math.sqrt(a))
        elif op == 'pow':
            a=float(input("enter base"))
            b=float(input("enter exponent"))
            print("result", math.pow(a,b))
        elif op in['sin','cos','tan','log']:
            a=float(input("enter value (in radians for sin/cos/tan):"))
            if op =='sin':
                print("result:",math.sin(a))
            elif op == 'cos':
                print("result",math.cos(a))
            elif op == 'tan':
                print("result", math.tan(a))
            elif op == 'log':
                print("result",math.log(a))
            
        else:
            print("Invalid operation")
            
calculator()                                
                               



  
        
    