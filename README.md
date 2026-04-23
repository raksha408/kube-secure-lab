# Kube-Secure: Netflix Video Fault-Injection Simulation

### Setup Instructions

### 1. Prerequisites to Install
- **Python 3.9+** (To run the code)

### 2. How to start the server
Open Command Prompt anywhere and type:
`cd F:\Cybersecurity\kube-secure-lab`
`pip install flask`
`python app.py`

### 3. Simulating Traffic
Leave the server running in the first window. Open a new PowerShell window and run this command to simulate user clicks:
```powershell
while($true) { Invoke-RestMethod -Uri http://localhost:5000/api/load_movie; Start-Sleep -Milliseconds 500 }
```
