class symptoms:
    def __init__(self,age,gender,fever,swab,nasal,tracheal,stool):
        self.age1=age
        self.gender1=gender
        self.symptom_fever=fever
        self.symptom_swab=swab
        self.symptom_nasal=nasal
        self.symptom_tracheal=tracheal
        self.symptom_stool=stool

    def __str__(self):
        return f'Age :{self.age1} ,Gender : {self.gender1}, Fever : {self.symptom_fever},Swab:{self.symptom_swab},Nasal : {self.symptom_nasal},Tracheal : {self.symptom_tracheal},Stool : {self.symptom_stool}'

    def __repr__(self):
        return str(self)
