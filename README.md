# F.A.R.M.I.S (Farming, Agriculture Research Management Information System)

F.A.R.M.I.S is an agricultural management system designed to empower farmers, agricultural researchers, stakeholders, investors, and government and non-government agencies. It provides a platform to upload, access, and manage agricultural data, helping users make informed decisions regarding best practices, identifying gaps, areas of high-value investment, policy-making, and future predictions.

## Features

- **User Management and Authentication**: Role-based user management system with authentication via phone numbers and SMS validation.
- **Data Upload and Management**: Securely upload, validate, and manage various agricultural data types (e.g., research documents, images, sensor data).
- **Data Storage and Organization**: Efficient storage of both structured and unstructured data, with support for large file uploads using streaming.
- **Data Access and Visualization**: Role-based access control and data visualization tools for analyzing and interpreting agricultural data.
- **Reports and Documentation**: Generate detailed reports and documentation based on uploaded data for policy-making and decision support.
- **Communication and Collaboration**: Real-time communication between users (farmers, researchers, investors) using Django Channels.
- **Notifications and Alerts**: Customizable notifications and alerts via SMS or in-app messaging.
- **Administrative and Monitoring Tools**: Tools for system administrators to monitor system health, manage users, track background tasks, and audit logs.

## Technologies Used

- **Backend**: Django, Django Rest Framework
- **Database**: PostgreSQL
- **Frontend**: (Optional, depending on your setup)
- **Real-Time Communication**: Django Channels
- **File Management**: S3-compatible storage (or similar services)
- **Deployment**: Docker Compose for local development, AWS EC2 for production

## System Architecture

- **User Management and Authentication**: Role-based authentication using Django’s built-in user model, extended to support phone number-based login and SMS verification.
- **Data Upload and Management**: Modular file handling system with validation and file metadata storage in PostgreSQL.
- **Data Access and Visualization**: Data access control and visualization capabilities restricted based on user roles (e.g., farmers, researchers, stakeholders).
- **Reports and Documentation**: Automated generation of reports based on aggregated data.
- **Administrative and Monitoring Tools**: Includes real-time system monitoring and auditing.

## Project Setup

### Prerequisites

- Docker and Docker Compose installed
- Python 3.8+
- PostgreSQL

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/FARMIS.git
   cd FARMIS
