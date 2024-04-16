resource "aws_launch_configuration" "launch_configuration_1" {
  image_id = "ami-0d3d9b94632ba1e57"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.security_group_1.id]
  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    EOF
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "asg-1" {
  launch_configuration = aws_launch_configuration.launch_configuration_1.id
  vpc_zone_identifier = [aws_subnet.my_subnet.id]

  target_group_arns = [aws_lb_target_group.asg.arn]
  health_check_type = "ELB"

  min_size = 2
  max_size = 3

  tag {
     key          = "Name"
     value        = "terraform-asg-example" 
     propagate_at_launch = true
  }     
}

resource "aws_lb" "lb-1" {
  name = "terraform-lb-1"
  load_balancer_type = "application"
  subnets = data.aws_subnet_ids.default.ids
  security_groups = [aws_security_group.alb]
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.lb-1
  port = 80
  protocol = "HTTP"

  default_action {
    type = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      message_body = "404: page not found"
      status_code = 404
    }
  }
}

resource "aws_lb_target_group" "asg" {
  name = "terraform-asg-example"
  port = var.server_port
  protocol = "HTTP"
  vpc_id = aws_vpc.my_vpc
  
  health_check {
    path ="/"
    protocol = "HTTP"
    matcher = "200"
    interval = 15
    timeout = 3
    healthy_threshold = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener_rule" "asg" {
  listener_arn = aws_lb_listener.http.arn
  priority = 100
  
  condition {
    path_pattern{
      values = ["*"]
    }  
  }
  
  action {
    type = "forward"
    target_group_arn = aws_lb_target_group.asg.arn
  }
}
