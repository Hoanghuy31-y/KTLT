print("Sinh vien: Nguyen Hoang Huy")
print("MSSV: 245752021610060")
print("######################")

number = []

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        number.append(str(i))

print(','.join(number))      
                    
                        
