def calc (a,b,op):
     if op == '+':
        return a+b
     elif op  =='-':
        return a-b
     elif op == '*':
        return a*b
     elif op == '/':
        if b != 0 :
            return a/b
        else:
            return "cannot divie by zero"
     else:
        return "invalid operator"
def main():
        a= int(input("Enter First number :"))
        b= int(input("Enter second number :"))
        op = (input("Enter operator(+,-,*,/) :"))
        result = calc(a,b,op)
        print ("Result:", result) 
main()
        