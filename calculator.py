def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

if __name__ == "__main__":
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))

---

### 🚀 Steps to Upload:
1. Create a new GitHub repo (e.g., `simple-python-calculator`).
2. On your computer:
```bash
mkdir simple-python-calculator
cd simple-python-calculator
touch calculator.py README.md
