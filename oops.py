class A:
    def __init__(self,nm,usn,marks):
        self.__Name=nm
        self.__USN=usn
        self.__Marks=marks
        self.percentage=(sum(marks)/len(marks)*100)/100
    def getDetails(self):
        print('Name:',self.__Name)
        print('USN',self.__USN)
        print('Marks',self.__Marks)
    def getPercentage(self):
        print('Percentage is:',self.percentage,'%')
        if(self.percentage < 35):
            print('Failed')
        elif(self.percentage >= 35 and self.percentage <= 84):
            print('Passed')
        else:
            print('Distinction')
        

st1 = A('sumayya','3BR21EC177',[89,86,79,77,92])
st1.getDetails()
st1.getPercentage()
print('\n')
st2 = A('sanu','3BR21EC180',[86,58,96,67,45])
st2.getDetails()
st2.getPercentage()
print('\n')
st3 = A('naffi','3BR21EC184',[99,94,96,97,91])
st3.getDetails()
st3.getPercentage()
print('\n')
st4 = A('juvi','3BR21EC153',[76,75,94,92,35])
st4.getDetails()
st4.getPercentage()
print('\n')
st5 = A('dakshi','3BR21EC148',[75,25,34,94,67])
st5.getDetails()
st5.getPercentage()

