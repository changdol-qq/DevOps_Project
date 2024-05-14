terraform {
  backend "s3" {
    bucket = "mark-cicd-terraform-eks" 
    key    = "jenkins/terraform.tfstate"
    region = "ap-northeast-2"
  }
}