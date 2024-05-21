#!/bin/bash

# Update package list
sudo apt-get update

# Install Jenkins
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y
sudo apt update
sudo apt install fontconfig openjdk-17-jre -y
sudo systemctl enable jenkins
sudo systemctl start jenkins




#install git
sudo apt-get install git -y

#install terraform
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt-get install terraform

#install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

#install aws-cli 
sudo apt-get install unzip -y
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo unzip awscliv2.zip
sudo ./aws/install
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
#install eksctl 
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

#install helm
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm


#Install docker engine
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y



# #!/bin/bash

# set -e

# log() {
#     echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')] $1"
# }

# install_jenkins() {
#     log "Installing Jenkins..."
#     sudo apt-get update
#     sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
#     echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
#     sudo apt-get update
#     sudo apt-get install -y jenkins fontconfig openjdk-17-jre
#     sudo systemctl enable jenkins
#     sudo systemctl start jenkins
#     log "Jenkins installation completed."
# }

# install_git() {
#     log "Installing Git..."
#     sudo apt-get install -y git
#     log "Git installation completed."
# }

# install_terraform() {
#     log "Installing Terraform..."
#     sudo apt-get update
#     sudo apt-get install -y gnupg software-properties-common
#     wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
#     gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint
#     echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
#     sudo apt-get update
#     sudo apt-get install -y terraform
#     log "Terraform installation completed."
# }

# install_kubectl() {
#     log "Installing kubectl..."
#     curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
#     sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
#     log "kubectl installation completed."
# }

# install_aws_cli() {
#     log "Installing AWS CLI..."
#     sudo apt-get install -y unzip
#     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
#     unzip awscliv2.zip
#     sudo ./aws/install
#     sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
#     log "AWS CLI installation completed."
# }

# install_eksctl() {
#     log "Installing eksctl..."
#     curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
#     sudo mv /tmp/eksctl /usr/local/bin
#     log "eksctl installation completed."
# }

# install_helm() {
#     log "Installing Helm..."
#     curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
#     sudo apt-get install -y apt-transport-https
#     echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
#     sudo apt-get update
#     sudo apt-get install -y helm
#     log "Helm installation completed."
# }

# install_docker() {
#     log "Installing Docker..."
#     sudo apt-get update
#     sudo apt-get install -y ca-certificates curl
#     sudo install -m 0755 -d /etc/apt/keyrings
#     sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
#     sudo chmod a+r /etc/apt/keyrings/docker.asc
#     echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#     sudo apt-get update
#     sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#     log "Docker installation completed."
# }

# main() {
#     install_jenkins
#     install_git
#     install_terraform
#     install_kubectl
#     install_aws_cli
#     install_eksctl
#     install_helm
#     install_docker
#     log "All installations completed successfully."
# }

# main "$@"