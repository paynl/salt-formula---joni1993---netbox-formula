{% from tpldir ~ "/map.jinja" import netbox with context %}
command = '{{ netbox.service.homedir }}/app/venv/bin/gunicorn'
pythonpath = '{{ netbox.service.homedir }}/app/venv/bin/'
bind = '{{ netbox.service.gunicorn.bind }}'
workers = {{ netbox.service.gunicorn.workers }}
user = '{{ netbox.service.user }}'
threads = '{{ netbox.service.gunicorn.threads }}'
max_requests = {{ netbox.service.gunicorn.max_requests }}
max_requests_jitter = {{ netbox.service.gunicorn.max_requests_jitter }}