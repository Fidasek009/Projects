import keyboard
import time

line=[]
lcount=0

while True:
    line.append(input())
    lcount+=1
    if line[lcount-1] == '':
        break

keyboard.wait("Enter")

for i in range(lcount):
    keyboard.write(line[i])
    time.sleep(0.1)
    keyboard.press_and_release("Enter")
    time.sleep(0.1)
