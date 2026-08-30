
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(
    __name__,
    template_folder="flask/templates",
    static_folder="flask/static"
)

app.secret_key = "hospital-management-demo"


departments = [
    {"id": 1, "name": "Cardiology", "patients": 24, "staff": 8},
    {"id": 2, "name": "Emergency", "patients": 31, "staff": 12},
    {"id": 3, "name": "Neurology", "patients": 18, "staff": 6},
    {"id": 4, "name": "Pediatrics", "patients": 22, "staff": 7},
]


patients = [
    {
        "id": 1,
        "name": "Ahmed Hassan",
        "age": 34,
        "department": "Cardiology",
        "record": "Routine cardiac follow-up",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Mariam Ali",
        "age": 27,
        "department": "Neurology",
        "record": "Neurological consultation",
        "status": "Active"
    },
    {
        "id": 3,
        "name": "Omar Mohamed",
        "age": 45,
        "department": "Emergency",
        "record": "Emergency observation",
        "status": "Critical"
    },
    {
        "id": 4,
        "name": "Salma Ahmed",
        "age": 12,
        "department": "Pediatrics",
        "record": "Regular check-up",
        "status": "Active"
    },
]


staff = [
    {
        "id": 1,
        "name": "Dr. Sara Ali",
        "age": 39,
        "position": "Cardiologist",
        "department": "Cardiology"
    },
    {
        "id": 2,
        "name": "Dr. Karim Samir",
        "age": 42,
        "position": "Neurologist",
        "department": "Neurology"
    },
    {
        "id": 3,
        "name": "Nour Hassan",
        "age": 29,
        "position": "Nurse",
        "department": "Emergency"
    },
    {
        "id": 4,
        "name": "Mona Adel",
        "age": 31,
        "position": "Nurse",
        "department": "Pediatrics"
    },
]


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        active="dashboard",
        patients=patients,
        staff=staff,
        departments=departments
    )


@app.route("/patients")
def patients_page():
    return render_template(
        "patients.html",
        active="patients",
        patients=patients,
        departments=departments
    )


@app.route("/patients/add", methods=["POST"])
def add_patient():
    department = request.form.get("department", "").strip()

    patient = {
        "id": len(patients) + 1,
        "name": request.form.get("name", "").strip(),
        "age": request.form.get("age", "").strip(),
        "department": department,
        "record": request.form.get("record", "").strip(),
        "status": request.form.get("status", "Active")
    }

    if patient["name"] and patient["age"] and department:
        patients.append(patient)

        for d in departments:
            if d["name"] == department:
                d["patients"] += 1
                break

        flash("Patient added successfully.", "success")
    else:
        flash("Please fill in all required fields.", "error")

    return redirect(url_for("patients_page"))


@app.route("/staff")
def staff_page():
    return render_template(
        "staff.html",
        active="staff",
        staff=staff,
        departments=departments
    )


@app.route("/staff/add", methods=["POST"])
def add_staff():
    department = request.form.get("department", "").strip()

    member = {
        "id": len(staff) + 1,
        "name": request.form.get("name", "").strip(),
        "age": request.form.get("age", "").strip(),
        "position": request.form.get("position", "").strip(),
        "department": department
    }

    if (
        member["name"]
        and member["age"]
        and member["position"]
        and department
    ):
        staff.append(member)

        for d in departments:
            if d["name"] == department:
                d["staff"] += 1
                break

        flash("Staff member added successfully.", "success")
    else:
        flash("Please fill in all required fields.", "error")

    return redirect(url_for("staff_page"))


@app.route("/departments")
def departments_page():
    return render_template(
        "departments.html",
        active="departments",
        departments=departments
    )


@app.route("/departments/add", methods=["POST"])
def add_department():
    name = request.form.get("name", "").strip()

    if name:
        departments.append({
            "id": len(departments) + 1,
            "name": name,
            "patients": 0,
            "staff": 0
        })

        flash("Department added successfully.", "success")
    else:
        flash("Department name is required.", "error")

    return redirect(url_for("departments_page"))


if __name__ == "__main__":
    app.run(debug=True)

