# Django Project Template
Template repository for Django based projects

# Usage
Use django-admin's startproject command to create the project.

Here's an example

uv run django-admin startproject \
    --template=https://github.com/nav/django-project-template/archive/refs/heads/main.zip \
    --extension=py \
    --extension=html \
    --extension=hcl \
    --extension=json \
    --extension=yaml \
    --extension=toml \
    --extension=sh \
    --extension=tf \
    --extension=tfvars \
    {name of the project}

# Notes
- .env can be found in password manager

