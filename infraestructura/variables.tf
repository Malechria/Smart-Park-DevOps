variable "region_aws" {
  description = "La región de AWS donde se creará la infraestructura"
  type        = string
  default     = "us-east-2" # Región Ohio
}

variable "tipo_instancia" {
  description = "El tamaño de la instancia EC2"
  type        = string
  default     = "t3.micro" 
}