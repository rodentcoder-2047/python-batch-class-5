subjects = ["maths", "science","english"," history","arts"]
hated_subject = input("enter the subject you hate ")
for sub in subjects:
    if sub == hated_subject:
        print("you hate:",sub)
        break
    print("subject:",sub)