cleanedcontent =""
count = 0
with open("plain.txt", "r") as file:
    
    for num, line in  enumerate(file, start=1):
            content = [clean.strip() for clean in line.split(",")]

        
            name= content[0]
            age = content[1]
            email = content[2]
            
            try:
                if int(age) < 18:
                    continue
            except ValueError:
                 print("age has incorrect input for user "+name+" in line "+str(num))
                 if ValueError:
                      continue
            count +=1
            cleanedcontent += (f"{name}, {age}, {email}"+'\n')
            with open('cleanedlist.txt', 'w') as output:
                output.write(cleanedcontent)
print(f"{count} details is cleaned and stored in cleaned.txt file")
        
            
        

