variable "app_name" {
  type = string
  description = "Name of this application"
}

variable "app_role" {
  type = string
  description = "App role name for this application"
}

variable "aws_account_id" {
  type = string
  description = "AWS Account ID"
}

variable "aws_profile" {
  type = string
  description = "AWS Profile to use for Terraform"
}

variable "aws_region" {
  type = string
  description = "AWS Region to use for Terraform"
}

variable "ecr_repo" {
  type = string
  description = "Docker repository to store private docker images"
}

variable "s3_bucket" {
  type = string
  description = "S3 bucket name for the application."
}
