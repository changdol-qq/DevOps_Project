terraform {
  backend "s3" {
    bucket = "mark-cicd-terraform-eks"
    key    = "eks/terraform.tfstate"
    region = "ap-northeast-2"
  }
}