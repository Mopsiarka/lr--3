god = int(input("Введите год"))
god1 = god%4
god2 = god%100
god3 = god%400

vis = (god1 == 0 and god2 != 0) or (god3 == 0) 
if vis:
    print(god , "является високосным")
else:
    print("год не високосный")