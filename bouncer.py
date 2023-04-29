age = 19
isBirthday = False

if age >= 21:
    print("You can DRINK!")
    if isBirthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE MARTINI!")
elif age >= 18:
    print("You can come in but no drinking")
    if isBirthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE GATORADE!")
else:
    print("GO HOME JIT")
