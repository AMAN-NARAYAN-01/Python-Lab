fin = open("marks.txt", "r")
fout = open("result.txt", "w")

for line in fin:
   data = line.split()
   
   
        roll = data[0]
        name = data[1]
        m1 = data[2])
        m2 = data[3])
        m3 = data[4])
        
        total = m1 + m2 + m3 
        avg = total / 3
        
        if avg >= 90:
        grade = "A"
        elif  avg >= 75:
        grade = "B'
        elif  avg>=60:
        grade = "c"
        else:
        grade = "D"
        
        fout.write(f"{roll} {name}
        Total={total} Average={avg:.2f}
        Grade={grade}\n")
        
        fin.close()
        fout.close()
        
        print("Results written to result.txt")
        
        
   
   
