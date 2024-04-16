output "web_ip" {
  value = aws_instance.app-server-1.public_ip 
}

output "alb_dns_name" {
  value = aws_lb.lb-1
  description = "The domain name of the load balancer"
}