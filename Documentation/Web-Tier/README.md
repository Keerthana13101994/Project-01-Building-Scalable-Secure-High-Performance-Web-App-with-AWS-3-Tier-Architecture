# Web Tier – Presentation Layer Deployment

## 1. Overview

The Web Tier represents the Presentation Layer of the AWS Three-Tier Architecture.

It is deployed using an Amazon EC2 instance in a public subnet. Nginx is installed as the web server to host and serve the frontend HTML webpage.

## 2. AWS Resources

| Resource | Configuration |
|---|---|
| EC2 Instance | Project01-Web-Server-A |
| Operating System | Amazon Linux 2023 |
| VPC | Project01-VPC |
| Subnet | Public-Web-A |
| Security Group | Project01-Web-SG |
| Web Server | Nginx |
| HTTP Port | 80 |
| SSH Port | 22 |

## 3. Security Group Configuration

Security Group: Project01-Web-SG

### Inbound Rules

| Type | Port | Source | Purpose |
|---|---|---|---|
| HTTP | 80 | 0.0.0.0/0 | Allow website access |
| SSH | 22 | Administrator IP | SSH access |
| SSH | 22 | EC2 Instance Connect prefix list | Browser-based SSH access |

## 4. Nginx Installation

Updated the Linux packages:

```bash
sudo dnf update -y
```

Installed Nginx:

```bash
sudo dnf install nginx -y
```

Started Nginx:

```bash
sudo systemctl start nginx
```

Enabled automatic startup:

```bash
sudo systemctl enable nginx
```

Verified Nginx:

```bash
sudo systemctl status nginx
```

## 5. Frontend HTML Deployment

Source repository:

https://github.com/Vennilavanguvi/Three-Tier-Architecture

Created a backup of the default Nginx homepage:

```bash
sudo cp /usr/share/nginx/html/index.html /usr/share/nginx/html/index.html.backup
```

Downloaded the frontend HTML file from GitHub:

```bash
sudo curl -fL https://raw.githubusercontent.com/Vennilavanguvi/Three-Tier-Architecture/main/index.html -o /usr/share/nginx/html/index.html
```

Nginx document root:

```text
/usr/share/nginx/html/
```

## 6. Deployment Verification

Verified that the Nginx service was running and the default website was replaced with the GUVI Feedback Form.

Website access:

http://13.232.150.191

Deployment result: Successful.

## 7. Outcome

- EC2 instance successfully deployed in the public subnet.
- Web Security Group configured.
- Nginx installed and running.
- Frontend HTML downloaded from GitHub.
- Custom webpage successfully hosted on Nginx.
- Website verified through the EC2 public IPv4 address.
