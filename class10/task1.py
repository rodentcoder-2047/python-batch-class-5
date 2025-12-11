student1 = {"physics", "chemistry", "computer", "biology"}
student2 = {"maths", "computer", "hindi", "biology"}
#common subjects
intersection = student1 & student2
#unique subjects
unique_to_1 = student1 - student2
unique_to_2 = student2 - student1
#union 
all_subjects = student1 | student2
print("common subjects" , intersection)
print(" subject unique to student 1 ", unique_to_1)
print("subject unique to student 2 ", unique_to_2)
print("total subjects combined", all_subjects)
