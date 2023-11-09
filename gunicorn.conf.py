bind = '0.0.0.0:8000'
workers = 4
static_root = 'static/'
static_files = True
forwarded_allow_ips = '*'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')