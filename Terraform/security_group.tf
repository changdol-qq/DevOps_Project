resource "aws_security_group" "security_group_1" {
  name = "terraform-example-instance"
  ingress{
    from_port = var.sever_port
    to_port   = var.sever_port
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    #CIDR 블록 0.0.0.0/0(anywhere)에서 8080포트로 들어오는 TCP 요청 허용
  }  
}

resource "aws_security_group" "alb" {
  name = "terraform-example-alb"
  ingress = {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress = {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}