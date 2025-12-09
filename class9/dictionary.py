student = {
    "name":"Aditya",
    "age":"21",
    "Hobby": " chess"
}
print(student)
print(student["name"])
print(student.get("age"))
student["game"] = "Football"
print(student)
student.pop("game")
print(student)
del student["age"]

student.clear() 
print(student)                 