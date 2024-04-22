variable "db_username" {}
variable "db_password" {}


resource "aws_db_instance" "db_1" {

    allocated_storage = 5
    engine = "postgres"
    engine_version = "16.2"
    instance_class = "db.t3.micro"
    identifier = "my-webapp-db"
    username = var.db_username
    password = var.db_password

    #db_subnet_group_name = aws_db_subnet_group.example.name  # DB 서브넷 그룹
    #vpc_security_group_ids = [aws_security_group.example.id]  # VPC 보안 그룹

    backup_retention_period = 7
    skip_final_snapshot = true

    tags = {
        Name = "My PostgreSQL Instance"
    }
}


resource "aws_db_subnet_group" "example" {
  name        = "my-subnet-group"
  subnet_ids  = ["subnet-abcdefgh", "subnet-ijklmnop"]

  tags = {
    Name = "My DB Subnet Group"
  }
}


resource "aws_security_group" "example" {
  name        = "my-rds-sg"
  description = "Allow all inbound traffic to PostgreSQL"
  vpc_id      = "vpc-abcdef0123456789"

  ingress {
    from_port   = 5432  # PostgreSQL 포트
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "my-postgres-sg"
  }
}