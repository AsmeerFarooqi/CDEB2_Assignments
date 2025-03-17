# Python Assignments

This repository contains Python assignments that demonstrate fundamental programming concepts. Below is a detailed explanation of each file.

---

## 🚀 Assignment 1: Basic Python Programs
**Filename:** `assignment1.py` , `assignment2.py`
**Description:** This file contains multiple Python programs that cover basic control structures such as conditional statements (`if-else`) and (`Variables`).

### 📌 Included Programs:
1. **Work Location Eligibility Based on Age and Gender**  
   - This program takes the user's age, gender, and marital status as input and determines their possible work location based on specified conditions..

```python
 age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
marital_status = input("Enter marital status (Y/N): ").upper()
if gender == 'F':  
    print("She will work only in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 <= age <= 60:
        print("He will work only in urban areas.")
    else:
        print("ERROR")
else:
    print("ERROR")

