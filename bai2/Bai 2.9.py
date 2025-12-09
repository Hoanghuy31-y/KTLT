print("Sinh vien: Nguyen Hoang Huy")
print("MSSV: 245752021610060")
print("######################")

s = input("Enter a string: ")
d = {}

for ch in s:
    d[ch] = s.count(ch)

print(d)    
