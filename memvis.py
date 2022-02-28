import sys
import re
from os import system


def visualize(res: list, db: list):
    with open("ram.txt", "r") as ram:
        ram = ram.read()
        orig = ram

    curCell = 1

    for value in res:
        for i in range(int(value)):
            ram = ram.replace(f"(VALUE{curCell})", "RESERVED")
            curCell += 1

            if curCell == 7: 
                for i in range(8): 
                    ram = ram.replace(f"(VALUE{curCell})", "..      ")
                    curCell += 1

                print(ram)
                _ = input("RAM DIAGRAM FULL, PRESS ENTER TO CLEAR SCREEN AND CONTINUE. ")
                system("clear")
                ram = orig
                curCell = 0

    for db in db:
        ram = ram.replace(f"(VALUE{curCell})", str(db) + "           |")
        curCell += 1

        if curCell == 7: 
            for i in range(8): 
                ram = ram.replace(f"(VALUE{curCell})", "..      ")
                curCell += 1

            print(ram)
            _ = input("RAM DIAGRAM FULL, PRESS ENTER TO CLEAR SCREEN AND CONTINUE. ")
            system("clear")
            ram = orig
            curCell = 0


    for i in range(8): 
        ram = ram.replace(f"(VALUE{curCell})", "..      ")
        curCell += 1


    print(ram)



if len(sys.argv) < 2:
    print("Too little args!\n")


with open(sys.argv[1], "r") as src:
    content = src.read()


reserved = []
_bytes = []

resb = re.findall(r"resb \d+", content)
db = re.findall(r"db \d+", content)

for res in resb:
    reserved.append(re.findall(r"\d+", res)[0])

for byte in db:
    _bytes.append(re.findall(r"\d+", byte)[0])


if __name__ == "__main__":
    visualize(reserved, _bytes)
