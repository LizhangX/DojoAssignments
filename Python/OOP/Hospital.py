
class Patient(object):
    def __init__(self, ID, Name, Allergies):
        # super(Patient, self).__init__ ID, Name, Allergies, Bed_num))
        self.ID = ID
        self.Name = Name
        self.Allergies = Allergies
        self.Bed_num = None
        

class Hospital(object):
    def __init__(self, Name, Capacity):
        # super(Hospital, self).__init__(*args))
        self.patient = []
        self.Name = Name
        self.Capacity = Capacity
        self.bednumber = 0
    
    def Admit(self,new_patient):
        self.bednumber += 1
        if self.bednumber <= self.Capacity:
            self.patient.append(new_patient)
            new_patient.Bed_num = self.bednumber
            print "Admission confirmed."
        else:
            self.bednumber -= 1
            print "Sorry, the hospital is full."
        return self

    def Discharge(self,dis_name):
        for i in self.patient:
            if i.Name == dis_name:
                self.patient.remove(i)
                i.Bed_num = None
        self.bednumber -= 1
        return self

    def check_patients(self):
        print self.patient
        print self.bednumber
        return self

patient1 = Patient(1,"Mike","qwer")
patient2 = Patient(2,"Jane","asdf")
patient3 = Patient(3,"Kate","asdf")

hospital1 = Hospital("royal", 2)
hospital1.Admit(patient1).check_patients()
# hospital1.Discharge(patient1).check_patients()
hospital1.Admit(patient2).check_patients()
hospital1.Admit(patient3).check_patients()


        
        
