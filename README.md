# Python Assignments

This repository contains Python assignments that demonstrate fundamental programming concepts. Below is a detailed explanation of each file.

---

## 🚀 Assignment 1: Basic Python Programs
**Filename:** `assignment1.py` 
Filename: 'assignment2.py'
**Description:** This file contains multiple Python programs that cover basic control structures such as conditional statements (`if-else`) and loops.

### 📌 Included Programs:
1. **Check Even or Odd**  
   - Takes a number as input and checks whether it is even or odd using the modulus operator (`%`).

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

