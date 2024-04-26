resource "aws_security_group" "worker_node_sg" {
  name = "terraform-worker-node-sg"  
  ingress{
    from_port = 30000
    to_port   = 32767
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress{
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress{
    from_port = 6783
    to_port   = 6784
    protocol  = "udp"
    cidr_blocks = [var.vpc_cidr]
  }
  ingress{
    from_port = 6783
    to_port   = 6783
    protocol  = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }
  egress = {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "control_plane_sg" {
  name = "terraform-control-plane-sg"
  ingress{ 
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }  
  ingress{ 
    from_port = 6443
    to_port   = 6443
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress{ 
    from_port = 2379
    to_port   = 2380
    protocol  = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }   
  ingress{ 
    from_port = 10250
    to_port   = 10259
    protocol  = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }  
  ingress{ 
    from_port = 6783
    to_port   = 6783
    protocol  = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }
  egress = {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "alb" {
  name = "terraform-example-alb"
  ingress = [
    {
      description      = "Allow HTTP inbound traffic"
      from_port        = 80
      to_port          = 80
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  ]

  egress = [
    {
      description      = "Allow all outbound traffic"
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  ]
}
