 # create : Adding student records
students = {
    
    "101": "Ali",
    "102": "sara",

}
# read : print all student records
print("Student Records:")
for roll, name in students.items():
    print(f"Rol No :{roll},Name : {name}")
# update : change name of student with roll 101
students["101"]= "Ahmed"
# delete : Remove student with roll 102 
del students["102"]
 # Final records
print("\nAfter update and delete:")
for roll , name in students.items():
  print(f"Roll No:{roll}, Name:{name}")