db = {}
with open("user.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        ret = i.strip().split("|")


        db[ret[0]] = ret[1]


print("请选择功能：登录 ，注册")
act = input()
if act == "登录":
    with open("user.txt", "r", encoding="utf-8") as f:

     false=0
    while True:
        false+=1
        username = input("请输入用户名：")
        if false <= 3:
         if username in db:
            password = input("请输入密码：")
            if password == db[username]:
                print("登录成功")
            else:
                print("密码错误登录失败")

         else:
            print("用户名不存在")
        else :
            print("登录失败次数过多")
            break
elif act == "注册":
    with open("user.txt", "w", encoding="utf-8") as f:
        username = input("请输入用户名：")
        password = input("请输入密码：")
        f.write(username + "|" + password + "\n")
    print("注册成功")




