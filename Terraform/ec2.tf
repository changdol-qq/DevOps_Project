resource "aws_instance" "app-server-1" {
  ami           = "ami-0d3d9b94632ba1e57"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.security_group_1]
  # aws_security_group 사용
  user_data = <<-EOF
    #!/bin/bash
    apt-get update
EOF
  tags = {
    Name = "App"
  }
}


resource "aws_db_instance" "default" {
  instance_class = "db.t2.micro"
  engine         = "mysql"
  allocated_storage = 20
}