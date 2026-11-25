\# Database Tier – Amazon RDS MySQL



\## 1. Overview



The Database Tier stores feedback submitted by users through the application.



Amazon RDS MySQL is used as the relational database service. It is deployed in the private Database Subnets and accepts connections from the App Tier.



\## 2. RDS Instance Configuration



| Property | Configuration |

|---|---|

| DB Identifier | project01-mysql-db |

| Database Engine | MySQL Community |

| Engine Version | MySQL 8.4.11 |

| Instance Class | db.t4g.micro |

| AWS Region | ap-south-1 (Mumbai) |

| Database Name | feedbackdb |

| Port | 3306 |

| Master Username | admin |



\*\*Note:\*\* The database endpoint and password are not included in this documentation for security reasons.



\## 3. Database Network Configuration



The RDS instance is deployed in the Database Subnets of Project01-VPC.



Security group configuration:



\- Inbound Type: MySQL/Aurora

\- Protocol: TCP

\- Port: 3306

\- Source: Project01-App-SG



This allows the private App Server to connect to the database without exposing MySQL directly to the internet.



\## 4. Database Connectivity



The App EC2 instance connects to Amazon RDS using the MySQL client.



The connection uses:

\- RDS endpoint

\- Port 3306

\- Database username

\- Database password



Database credentials are kept private and must not be committed to GitHub.



\## 5. Database Creation



The database `feedbackdb` was created in the MySQL instance.



The following SQL command was used to create the feedback table:



```sql

CREATE TABLE feedback (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   name VARCHAR(100),

&#x20;   email VARCHAR(100),

&#x20;   feedback TEXT

);

```



\## 6. Application Integration



The Flask application connects to Amazon RDS MySQL using the PyMySQL Python library.



When a user submits feedback:

1\. The Web Tier receives the request.

2\. Nginx forwards the request to the Flask backend.

3\. Flask processes the submitted data.

4\. PyMySQL connects to Amazon RDS.

5\. The feedback record is inserted into the `feedback` table.



\## 7. Database Verification



A test feedback record was submitted successfully through the Web Server.



Test data:



| Field | Value |

|---|---|

| Name | Test User |

| Email | test@example.com |

| Feedback | Testing three tier architecture |



The database record was verified successfully using a SELECT query.



The application returned:



```json

{

&#x20; "message": "Feedback submitted successfully!"

}

```



This confirmed successful communication between the Web Tier, App Tier, and Database Tier.



\## 8. Outcome



The Amazon RDS MySQL database was successfully deployed and integrated with the Flask application.



The database is accessible through the private App Tier, and feedback submissions are stored successfully.



The Database Tier completes the three-tier application architecture.

