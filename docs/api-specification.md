# TwinOS API Specification

## Base URL

http://localhost:8000

---

# Health

## GET /

Description:
Returns API welcome message.

Authentication:
No

Response

```json
{
    "message": "Welcome to TwinOS API"
}
```

---

## GET /health

Description:
Checks server health.

Authentication:
No

Response

```json
{
    "status": "healthy"
}
```

---

# System

## GET /system/info

Description:
Returns live system information.

Authentication:
No

Returns

- CPU Usage
- RAM Usage
- Disk Usage
- OS
- Hostname

---

## GET /system/history

Description:
Returns historical telemetry.

Authentication:
Yes

---

## GET /system/processes

Description:
Returns running processes.

Authentication:
Yes

---

## GET /system/network

Description:
Returns network statistics.

Authentication:
Yes

---

# Authentication

## POST /auth/register

Creates a new user.

Authentication:
No

---

## POST /auth/login

Logs user in.

Authentication:
No

Returns

JWT Token

---

## GET /auth/profile

Returns current user.

Authentication:
Yes

---

# Alerts

## GET /alerts

Returns all alerts.

Authentication:
Yes

---

## POST /alerts

Creates alert.

Authentication:
Yes

---

# AI

## GET /prediction

Returns AI predictions.

Authentication:
Yes

---

## GET /recommendation

Returns AI recommendations.

Authentication:
Yes

---

# Settings

## GET /settings

Returns user settings.

Authentication:
Yes

---

## PUT /settings

Updates settings.

Authentication:
Yes

---

# WebSocket

## WS /ws/system

Streams live telemetry.

Authentication:
Yes