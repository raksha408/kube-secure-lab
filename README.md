#  Kube-Secure: Enterprise Netflix Fault-Injection & Log Diagnostics Lab

##  Project Overview
**Kube-Secure** is a simulated microservices troubleshooting environment. I engineered this project to practically apply **networking fundamentals (TCP/IP, DNS, Layer 2/3)**, **endpoint-to-server connectivity troubleshooting**, and **log analysis across distributed, multi-component systems**.

Using Python, I built a mock Netflix Video Streaming API that strictly processes `POST` requests. To simulate a realistic enterprise outage, the code utilizes a synthetic **Fault-Injection Mechanism** to randomly drop internal system connections and simulate authentication attacks, allowing me to **proactively identify and resolve potential problems** in a sandbox environment.

### Core competencies applied in this project:
- **Windows application support:** Executing client load-generation on Windows and reviewing local Event Viewer diagnostics.
- **Linux command-line fundamentals:** Navigating the backend host to tail, parse, and analyze raw container outputs.
- **Kubernetes fundamentals:** Building and analyzing pod-based microservice deployments and cluster-managed architectures.
- **Troubleshooting process:** Gathering logs and configuration details to attempt to reproduce reported issues and authoring professional incident resolution documentation.

---

##  Core Features & Technologies
- **Fault-Injection Engine:** The environment synthetically forces `HTTP 504 (Gateway Timeout)` and `HTTP 401 (Unauthorized)` errors into a stream of healthy API traffic based on a randomized probability model.
- **Log Generation:** Generates real-time, unstructured application logs `[INFO]`, `[ERROR]`, and `[CRITICAL]` to standard output for cross-component **log analysis**.
- **Client Automation:** Uses PowerShell's `Invoke-RestMethod` to emulate high-volume customer streaming traffic hitting the backend API.
- **Cloud/K8s Architecture:** Fully containerized with a written Dockerfile and [app-deployment.yaml](cci:7://file:///F:/Cybersecurity/kube-secure-lab/kubernetes/app-deployment.yaml:0:0-0:0) load-balancer manifests.

---

##  Architecture & Simulation Logic
When the PowerShell client scripts ping the `/api/load_movie` endpoint, the server reacts dynamically:
1. **Normal Traffic (60%):** successfully loads the movie and assigns a `stream_id` (Returns HTTP 200).
2. **Database Crash (30%):** The server simulates losing connection with the backend Netflix database. (Returns HTTP 504 Server Unreachable).
3. **Security Event (10%):** The server simulates detecting an expired or spoofed subscription token. (Returns HTTP 401 Unauthorized).

---

##  Installation & Usage Guide

### 1. Requirements
- Python 3.9+
- Windows PowerShell

### 2. Turn on the Server
Open a terminal, navigate to the project directory, and start the simulation:
```bash
pip install flask
python app.py
