
# AWS Three-Tier Web Application Architecture

## 1. Project Overview

This project demonstrates the design of a scalable, secure and high-performance web application using AWS three-tier architecture.

The architecture separates the application into three layers:

- Web Tier: Handles incoming user requests.
- Application Tier: Processes business logic.
- Database Tier: Stores application data.

## 2. AWS Region

Mumbai - ap-south-1

## 3. VPC Configuration

- VPC Name: Project01-VPC
- IPv4 CIDR: 10.0.0.0/16

## 4. Subnet Architecture

| Tier | Subnet | CIDR |
|---|---|---|
| Public Web | Public-Web-A | 10.0.0.0/23 |
| Public Web | Public-Web-B | 10.0.2.0/23 |
| Private App | Private-App-A | 10.0.4.0/23 |
| Private App | Private-App-B | 10.0.6.0/23 |
| Private DB | Private-DB-A | 10.0.8.0/23 |
| Private DB | Private-DB-B | 10.0.10.0/23 |

The six subnets are distributed across two Availability Zones.

## 5. Network Components

- VPC
- Public and Private Subnets
- Internet Gateway
- Elastic IP
- NAT Gateway
- Public Route Table
- Private Application Route Table
- Private Database Route Table

## 6. Network Traffic Flow

1. Internet users access the public web tier.
2. The web tier communicates with the private application tier.
3. The application tier communicates with the private database tier.
4. Private application servers use NAT Gateway for outbound internet access.
5. Database resources do not have a direct internet route.

## 7. Architecture Diagram

Final output has been added in the screenshot file
