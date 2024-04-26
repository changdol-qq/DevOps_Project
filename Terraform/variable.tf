variable "server_port" {
  description = "The port the server will use for HTTP requests"
  type        = number
  default     = 8080
}

variable "ssh" {
  description = "The port the server will use for SSH request"
  type        = number
  default     = 22
}

variable "vpc_cidr" {
  description = "The VPC cidr"
  default = "172.31.0.0/16"
}