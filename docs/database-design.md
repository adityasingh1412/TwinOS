# TwinOS Database Design

## Database

Development:
- SQLite

Production:
- PostgreSQL

ORM:
- SQLAlchemy

---

# Tables

## users

Stores user information.

Columns

- id
- username
- email
- password_hash
- created_at

---

## system_snapshots

Stores historical system telemetry.

Columns

- id
- user_id
- timestamp
- cpu_percent
- ram_percent
- disk_percent
- disk_used_gb
- disk_free_gb
- network_sent_mb
- network_received_mb

---

## alerts

Stores generated alerts.

Columns

- id
- user_id
- timestamp
- severity
- title
- description

---

## predictions

Stores AI predictions.

Columns

- id
- user_id
- timestamp
- cpu_prediction
- ram_prediction
- disk_prediction

---

## recommendations

Stores AI recommendations.

Columns

- id
- user_id
- timestamp
- recommendation
- status

---

## settings

Stores user preferences.

Columns

- id
- user_id
- refresh_interval
- dark_mode
- notifications