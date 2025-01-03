# Refer to this for more information:
# https://github.com/hashicorp/envconsul#configuration-file

kill_signal = "SIGINT"
log_level = "info"
pristine = false
reload_signal = "SIGHUP"
upcase = true


secret {
  path      = "secret/data/{{ project_name|slugify }}"
  no_prefix = true
}

secret {
  path      = "aws/creds/{{ project_name|slugify }}-role"
  no_prefix = true
  {% verbatim %}
  format = "aws_{{ key | replaceKey `access_key` `access_key_id` | replaceKey `secret_key` `secret_access_key` }}"
  {% endverbatim %}
}

vault {
  unwrap_token = false
  renew_token = true
  retry {
    enabled = true
    attempts = 12
    backoff = "250ms"
    max_backoff = "1m"
  }
}
