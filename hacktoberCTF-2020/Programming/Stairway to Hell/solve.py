
from pwn import *
context.log_level='DEBUG'
conn = remote('env2.hacktober.io',5001)
conn.recvuntil('deal.\n\n')

counter=666
lines=[]
linecounter=1
line=""
for i in range(30):
    
    for j in range(linecounter):
        line+=str(counter)+" "
        counter+=1
    lines.append(line)
    linecounter+=1

conn.sendline(line)
print(conn.recv())