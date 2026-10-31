# Digital Guardian — Device Security Dashboard

A personal device management dashboard designed to organize registered devices and display security-related event notifications.

**Built by Swaraj Sonalkar**

## Overview

Digital Guardian is a defensive device-management dashboard that provides a centralized interface for maintaining a list of personal devices and reviewing simulated security events.

The project demonstrates backend API development, database operations, and dashboard-based information visualization.

## Features

- Register personal devices
- Manage registered devices
- Remove devices
- Simulated security event generation
- Event history dashboard
- SQLite database integration
- REST API architecture
- Responsive interface

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| FastAPI | API development |
| SQLite | Data storage |
| HTML5 | Structure |
| CSS3 | Interface design |
| JavaScript | Frontend interaction |

## Project Structure

```text
DIGITAL-GUARDIAN/
├── app.py
├── guardian.db
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/swarajsonalkar-web/Digital-Guardian.git
cd Digital-Guardian
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment**

```bash
source .venv/bin/activate
```

Windows users can run `.venv\Scripts\activate`.

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
uvicorn app:app --reload --port 8002
```

Open: http://127.0.0.1:8002

## Future Improvements

- Real device inventory integrations
- Authentication and authorization
- Security notification integrations
- Device health monitoring
- Advanced event filtering
- Security analytics dashboard

## Security Note

This project currently uses simulated security events. It does not perform network scanning, covert monitoring, or traffic interception.

## Developer

**Swaraj Sonalkar**

GitHub: https://github.com/swarajsonalkar-web

Email: swarajsonalkar99@gmail.com

---

*Building a smarter and more organized digital security workspace.*

Make a separate static in project directory and then paste the html,css and javascript file
