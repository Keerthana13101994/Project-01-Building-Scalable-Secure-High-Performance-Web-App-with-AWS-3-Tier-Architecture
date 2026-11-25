\# App Tier – Flask Application



\## 1. Overview



The App Tier is the backend layer of the three-tier architecture. It uses Python Flask to process feedback submitted by users through the Web Tier.



The application runs on a private EC2 instance and communicates with the RDS MySQL database.



\## 2. EC2 Instance Configuration



| Property | Configuration |

|---|---|

| Instance Name | Project01-App-Server-A |

| Operating System | Ubuntu 24.04 |

| Private IP | 10.0.4.211 |

| Public IP | Not assigned |

| Application | Python Flask |

| Application Port | 5000 |

| Application Directory | \~/three-tier-app |



\## 3. Security Configuration



The App Server is deployed in a private subnet.



Inbound security group rules:



\- SSH (Port 22): Allowed from the Bastion Host security group.

\- Custom TCP (Port 5000): Allowed from the Web Server security group.



This configuration restricts direct public access to the backend application.



\## 4. Application Setup



The Flask application was deployed on the Ubuntu EC2 instance.



Application directory:



`\~/three-tier-app`



A Python virtual environment was created and activated.



Commands used:



```bash

python3 -m venv venv

source venv/bin/activate

```



Required Python packages were installed:



```bash

pip install flask pymysql gunicorn

```



\## 5. Flask Application Details



The backend application is maintained in `app.py`.



It provides two endpoints:



\- `/` – Health-check endpoint to verify that Flask is running.

\- `/submit` – POST endpoint to receive feedback details and insert them into the MySQL database.



The Flask application listens on port 5000.



\## 6. Web Tier to App Tier Communication



Nginx on the Web Server acts as a reverse proxy.



Request flow:



```text

User Browser

&#x20;    |

&#x20;    v

Web Server (Nginx)

&#x20;    |

&#x20;    | HTTP request to /submit

&#x20;    v

App Server (Flask)

Private IP: 10.0.4.211

Port: 5000

```



The Web Server forwards feedback requests to the private IP of the App Server.



\## 7. Database Connectivity



The Flask application connects to Amazon RDS MySQL using the PyMySQL library.



Database details:



\- Database Identifier: project01-mysql-db

\- Database Name: feedbackdb

\- Database Engine: MySQL

\- Port: 3306



Database credentials are configured securely using environment variables. Passwords must not be committed to GitHub.



\## 8. Application Testing and Verification



The Flask application was started successfully on the App Server.



A test feedback submission was sent through the Web Server using the `/submit` endpoint.



Successful response:



```json

{

&#x20; "message": "Feedback submitted successfully!"

}

```



The submitted record was also verified in the MySQL database.



This confirmed communication between the Web Tier, App Tier, and Database Tier.



\## 9. Outcome



The App Tier was successfully deployed on a private EC2 instance.



The Flask backend receives requests from the Web Tier, processes feedback, and stores the information in Amazon RDS MySQL.

