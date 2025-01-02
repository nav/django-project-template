resource "aws_s3_bucket" "{{ project_name|slugify }}_bucket" {
  bucket = var.s3_bucket

  tags = {
    Name        = "{{ project_name }}"
    Environment = "Production"
  }
}

resource "aws_s3_bucket_ownership_controls" "{{ project_name|slugify }}_bucket_ownership_controls" {
  bucket = aws_s3_bucket.{{ project_name|slugify }}_bucket.id

  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "{{ project_name|slugify }}_bucket_acl" {
  depends_on = [aws_s3_bucket_ownership_controls.{{ project_name|slugify }}_bucket_ownership_controls]

  bucket = aws_s3_bucket.{{ project_name|slugify }}_bucket.id
  acl    = "private"
}
