import requests


url = 'http://localhost:9696/predict'

person = {
    "age":40,
    "height(cm)":165,
    "weight(kg)":65,
    "waist(cm)":83,
    "eyesight(left)":1,
    "eyesight(right)":1,
    "hearing(left)":1,
    "hearing(right)":1,
    "systolic":121,
    "relaxation":78,
    "fasting blood sugar":96,
    "Cholesterol":196,
    "triglyceride":115,
    "HDL":54,
    "LDL":114,
    "hemoglobin":15,
    "Urine protein":1,
    "serum creatinine":0.9,
    "AST":24,
    "ALT":22,
    "Gtp":27,
    "dental caries":0
}


response = requests.post(url, json=person, timeout=10).json()
print(response)

if response['smoker'] == True:
    print("Is a smoker.")
else:
    print("Is not a smoker.")