import random
min = 1; max = 100
target = random.randint(min, max)
count = 0

print("=====猜數字遊戲======\n")
while True:
    key = int(input(f"猜數字的範圍{min}~{max}: "))
    count += 1
    if key >= min and key <= max:
        if (key == target):
            print(f"答對!!, 答案是{key}")
            print(f"你總共猜了{count}次")
            break
        elif(key > target):
            print("再小一點")
            max = key - 1

        elif(key < target):
            print("再大一點")
            min = key + 1

        print(f"你總共猜了{count}次")
    else:
        print("超出範圍")
print("GAME END")