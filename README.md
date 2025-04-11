# Vulnerable Login Web Application 🔐

This project is developed as part of the **Software Security (SWE 481)** course.  
It demonstrates how common vulnerabilities (like SQL Injection) can be tested and discovered using security tools such as **OWASP ZAP**.


---

## ⚙️ Technologies Used
- Python 3.11
- Flask Web Framework
- SQLite3 Database
- OWASP ZAP for automated vulnerability testing

---

##  Project Features
- A deliberately vulnerable login system built with Flask
- SQL Injection demo (no input validation)
- Manual and automated testing with OWASP ZAP
- Vulnerabilities logged and documented

---
## ▶️ How to Run the Application

1. Run the database creation script:
   ```bash
   python create_db.py
2. Start the Flask server:
   ```bash
   python main.py
3. Open your browser and go to:
   http://localhost:3000
4. Login with:
   Username: admin
   Password: 1234

   
##🚨 Known Vulnerabilities
    SQL Injection
    No CSRF protection
    Missing security headers
