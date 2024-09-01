import os
import socket


bind = "0.0.0.0:8080"
workers = int(os.getenv("GUNICORN_WORKER_COUNT", str((2 * os.cpu_count() + 1))))
accesslog = "-"
capture_output = True
enable_stdio_inheritance = True
level=os.getenv('LOG_LEVEL', 'ERROR').upper()
hostname = socket.gethostname()

print(f"Workers: {workers}")
print(f"Log Level: {level}")

# Define syslog format
access_logformat = f'%(asctime)s {hostname} %(name)s[%(process)d]: %(message)s'

logconfig_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': access_logformat
        },
        'access': {
            'format': access_logformat
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    },
    'loggers': {
        'gunicorn.access': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'gunicorn.error': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        }
    }
}
