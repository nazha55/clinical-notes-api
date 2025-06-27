import strawberry
from typing import List,Optional
from data import patients

# graphQL types
@strawberry.type
class Symptom:
    name:str

@strawberry.type
class Patient:
    id:int
    name:str
    age:Optional[int]
    gender:Optional[str]
    height:Optional[str]
    weight:Optional[str]
    symptoms:List[Symptom]

# input types
@strawberry.input
class SymptomInputGQL:
    name:str

@strawberry.input
class PatientInputGQL:
    id:int
    name:str
    age:Optional[int]=None
    gender:Optional[str]=None
    height:Optional[str]=None
    weight:Optional[str]=None
    
# get queries
@strawberry.type
class Query:
    @strawberry.field
    def get_patient(self,id:int) -> Patient:
        """
        Returns a patient with the given ID, including their symptoms.
        """
        for patient in patients:
            if patient["id"] == id:
                return Patient(
                    id=patient["id"],
                    name=patient["name"],
                    age=patient.get("age"),
                    gender=patient.get("gender"),
                    height=patient.get("height"),
                    weight=patient.get("weight"),
                    symptoms=[Symptom(name=s["name"]) for s in patient["symptoms"]]
                )
        
        # If patient not found
        raise ValueError(f"Patient with id {id} not found")    
# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_patient(self,input:PatientInputGQL)-> Patient:
        """
        Adds a new patient to the in-memory data.
        """
        # Check if patient ID already exists
        for patient in patients:
            if patient["id"] == input.id:
                raise ValueError(f"Patient with id {input.id} already exists")
        
        new_patient={
            "id":input.id,
            "name":input.name,
            "age":input.age,
            "gender":input.gender,
            "height":input.height,
            "weight":input.weight,
            "symptoms":[]
        }
        patients.append(new_patient)
        return Patient(
            id=input.id,
            name=input.name,
            age=input.age,
            gender=input.gender,
            height=input.height,
            weight=input.weight,
            symptoms=[]            
        )
    
    @strawberry.mutation
    def add_symptoms(self,patient_id:int,symptoms:List[SymptomInputGQL])->Patient:
        """
        Adds one or more symptoms to the specified patient.
        """
        for patient in patients:
            if patient["id"]== patient_id:
                for symptom in symptoms:
                    patient["symptoms"].append({"name":symptom.name})
                return Patient(
                id=patient["id"],
                name=patient["name"],
                age=patient.get("age"),
                gender=patient.get("gender"),
                height=patient.get("height"),
                weight=patient.get("weight"),
                symptoms=[Symptom(name=s["name"]) for s in patient["symptoms"]]
        )
        # If patient not found
        raise ValueError(f"Patient with id {patient_id} not found")

    @strawberry.mutation  
    def delete_symptom(self, patient_id: int, symptom_name: str) -> Patient:
        """
        Deletes a symptom by name for a given patient.
        Throws error if symptom or patient is not found.
        """
        for patient in patients:
            if patient["id"] == patient_id:
            # Check if symptom exists
                symptom_names = [s["name"] for s in patient["symptoms"]]
                if symptom_name not in symptom_names:
                    raise ValueError(f"Symptom '{symptom_name}' not found for patient with id {patient_id}")

                # Remove symptom
                patient["symptoms"] = [s for s in patient["symptoms"] if s["name"] != symptom_name]

                return Patient(
                    id=patient["id"],
                    name=patient["name"],
                    age=patient.get("age"),
                    gender=patient.get("gender"),
                    height=patient.get("height"),
                    weight=patient.get("weight"),
                    symptoms=[Symptom(name=s["name"]) for s in patient["symptoms"]]
                )
    
        # If patient not found
        raise ValueError(f"Patient with id {patient_id} not found")


schema=strawberry.Schema(query=Query,mutation=Mutation)