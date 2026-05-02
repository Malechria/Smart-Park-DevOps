# 1. Se define el proveedor
provider "aws" {
  region = var.region_aws
}

# 2. Se crea la VPC
resource "aws_vpc" "smartpark_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = { Name = "SmartPark-VPC" }
}

# 3. Se crea la Subred Pública en Ohio
resource "aws_subnet" "smartpark_subnet_publica" {
  vpc_id                  = aws_vpc.smartpark_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "${var.region_aws}a"
  tags = { Name = "SmartPark-Subred-Publica" }
}

# 4. Se busca la imagen oficial de Ubuntu
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# 5. Aprovisionar el servidor para Ansible/Vault
resource "aws_instance" "servidor_gestion" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.tipo_instancia
  subnet_id     = aws_subnet.smartpark_subnet_publica.id
  tags = { Name = "SmartPark-Servidor-Ansible-Vault" }
}
