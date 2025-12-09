print("Sinh vien: Nguyen Hoang Huy")
print("MSSV: 245752021610060")
print("######################")

class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
# Tạo đối tượng
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
