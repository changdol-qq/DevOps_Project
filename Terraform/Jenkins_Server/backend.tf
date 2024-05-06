terraform {
  backend "s3" {
    bucket = "mark-cicd-terraform-eks" #이미 생성 되어있는 버켓 사용??
    key    = "jenkins/terraform.tfstate"
    region = "ap-northeast-2"
  }
}