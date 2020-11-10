from socket import socket, AF_INET, SOCK_STREAM

def calculate():
    if recvCalculate.split(" ")[0] == "Hello":
        str_hello = "HELLO zhao.yuc\n"
        s.send(str_hello.encode())
    elif recvCalculate.split(" ")[0] == "DONE":
        flag = recvCalculate.split(" ")[1]
        print(recvCalculate)
        print('flag = ' + flag)
    elif recvCalculate.split(" ")[0] == "MATH":
        Integer1 = int(recvCalculate.split(" ")[1])
        Integer2 = int(recvCalculate.split(" ")[3])
        Operator = recvCalculate.split(" ")[2]
        if Operator == "+":
            sum = int(Integer1 + Integer2)
        elif Operator == "-":
            sum = int(Integer1 - Integer2)
        elif Operator == "*":
            sum = int(Integer1 * Integer2)
        else:
            sum = int(Integer1 / Integer2)
        answer = 'ANSWER ' + str(sum) + '\n'
        print(recvCalculate)
        print(answer)
        s.send(answer.encode())

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
while True:
    recvCalculate = s.recv(1024).decode()
    if recvCalculate == "":
        break
    else:
        calculate()
s.close()
