resource "aws_instance" "Control_plane" {
  ami           = "ami-0d3d9b94632ba1e57"
  instance_type = "t2.medium"
  vpc_security_group_ids = [aws_security_group.control_plane_sg.id]
  # aws_security_group 사용
  user_data = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo hostnamectl set-hostname control-plane
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
EOF
  tags = {
    Name = "control"
  }
}

/*
Change the hostname
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
*/

resource "aws_instace" "Worker_node" {
  ami           = "ami-00554e6d90019a269"
  instance_type = "t2.small"
  count         =  2
  vpc_security_gorup_ids = [aws_security_group.worker_node_sg.id]
  tags = "worker"
}



# resource "aws_db_instance" "default" {
#   instance_class = "db.t2.micro"
#   engine         = "mysql"
#   allocated_storage = 20
# }