# Clinical Notes GraphQL API (FastAPI + Strawberry)

This project is a simplified GraphQL API for managing patients and their symptoms — built using **FastAPI** and **Strawberry GraphQL**. 

---

## Features

* Add new patient records
* Add one or more symptoms to a patient
* Fetch patient details along with their symptoms
* Delete symptoms from a patient (bonus)
* Uses in-memory storage (no database)
* Input validation using Strawberry's input types

---

##  Tech Stack

* **FastAPI** – Web framework
* **Strawberry GraphQL** – GraphQL support
* **Uvicorn** – ASGI server

---

## Project Structure

```bash
.
├── main.py              # FastAPI entrypoint
├── schema.py            # GraphQL schema (Query and Mutation)
├── data.py              # In-memory patient data
└── README.md            
```

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/nazha55/clinical-notes-api.git
   cd clinical-notes-api
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate   
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt   
   ```

4. **Run the API**

   ```bash
   uvicorn main:app --reload
   ```

5. **Access GraphQL UI**

   * Open your browser and visit: [http://localhost:8000/graphql](http://localhost:8000/graphql)

---

## Sample GraphQL Queries

### Add Patient

```graphql
mutation {
  addPatient(input: {
    id: 1,
    name: "Hima",
    age: 32,
    gender: "Female",
    height: "163cm",
    weight: "55kg"
  }) {
    id
    name
    age
    gender
    height
    weight
    symptoms {
      name
    }
  }
}
```

---

### Add Multiple Symptoms

```graphql
mutation {
  addSymptoms(
    patientId: 1,
    symptoms: [
      { name: "Cough" },
      { name: "Fever" }
    ]
  ) {
    id
    name
    symptoms {
      name
    }
  }
}
```

---

### Get Patient

```graphql
query {
  getPatient(id: 1) {
    id
    name
    age
    gender
    height
    weight
    symptoms {
      name
    }
  }
}
```

---

### Delete a Symptom

```graphql
mutation {
  deleteSymptom(patientId: 1, symptomName: "Fever") {
    id
    symptoms {
      name
    }
  }
}
```

---

## Notes

* The API uses in-memory Python lists; no database is required.
* This project focuses only on the **Patient** and **Symptom** sections shown in the Figma UI.
* Other fields like medications or history are **not part of the required task**, as confirmed via email.

---

