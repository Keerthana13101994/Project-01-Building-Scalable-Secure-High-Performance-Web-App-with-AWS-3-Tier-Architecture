
# AWS Project 01 - Implementation Documentation

## Task 1: VPC and Network Infrastructure

### Objective
To create a custom VPC and configure public and private subnets across two Availability Zones.

### Step 1: Create VPC

- VPC Name: Project01-VPC
- CIDR Block: 10.0.0.0/16
- Region: Mumbai (ap-south-1)

Purpose:
A VPC provides an isolated virtual network to host AWS resources.

### Step 2: Create Subnets

Six subnets were planned across two Availability Zones.

Each subnet uses a /23 CIDR block to provide 507 usable IPv4 addresses in AWS.

Purpose:
Subnets separate web, application and database resources.

### Step 3: Create Internet Gateway

Name: Project01-IGW

Purpose:
Provides internet connectivity to resources in public subnets when correctly configured with routes.

### Step 4: Allocate Elastic IP

Purpose:
Provides a static public IPv4 address for the NAT Gateway.

### Step 5: Create NAT Gateway

Name: Project01-NAT
Subnet: Public-Web-A
Connectivity: Public

Purpose:
Allows private application servers to initiate outbound internet connections.

### Step 6: Create Route Tables

1. Project01-Public-RT
2. Project01-Private-App-RT
3. Project01-Private-DB-RT

Purpose:
Route tables control network traffic between subnets and other destinations.

### Step 7: Configure Routes

Public Route Table:
0.0.0.0/0 -> Internet Gateway

Private Application Route Table:
0.0.0.0/0 -> NAT Gateway

Private Database Route Table:
Local VPC route only

### Step 8: Associate Subnets

Public RT:
Public-Web-A and Public-Web-B

Private App RT:
Private-App-A and Private-App-B

Private DB RT:
Private-DB-A and Private-DB-B

### Verification

To be updated after completing all configurations.

### Outcome

Final output has been added in the screenshot file
