
healthy_patient={ "Sugar level": 15,"Blood pressure": 32,"Heartbeat rate": 71,"weight": 65, "fat percentage": 10}
patient_data = {}
for key in healthy_patient:
    patient_data[key]=int(input(f"Enter {key}: "))
differences={}
for key in healthy_patient:
    differences[key]=healthy_patient[key]-patient_data[key]
print(differences)
for key,diff in differences.items():
    print(f"{key} {diff}")
    if diff < 0:
        print(f"The {key} is {abs(diff)} more than the ideal value")
    elif diff > 0:
        print(f"The {key} is {abs(diff)} less than the ideal value")
