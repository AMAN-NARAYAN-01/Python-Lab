students = [

while True:
        print("\n1. insert")
        print("2.Delete")
        print("3. Searc")
         print("4. Display")
         print(" Exit")
         
         
         ch = int(input("Enter choice:")
         
         if ch ==1:
         roll=input("Enter roll no:")
         name=input("Enter Name:")
         marks=input("Enter Marks:")
         
         ))'
         
         students.append({"Roll":roll,"Name":name,"Marks",marks})
         
         elif ch == 2:
         roll = input("Enter Roll No to delete:")
         found = false
         for s in students 
         if s["Roll"] == roll:
         students.remove(s)
         found = True
         print("Recrod Not Delete")
         Break
         if not found
         print("Record Not Found")
         
        elif ch == 3:
         roll = input("Enter Roll No to search:")
         found = False
         for s in students:
         if s["Roll']== roll:
         print(s)
         found = True 
         break
         if not found:
         print("records Not Found")
         
