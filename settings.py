TEST = True

if TEST:
    DB_SETTINGS = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'LOGIN': '',
        'PASSWORD': ''
    }
    DB_CONNECTION_STRING = 'sqlite+aiosqlite:///data.db'
else:
    DB_SETTINGS = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'LOGIN': '',
        'PASSWORD': ''
    }
    DB_CONNECTION_STRING = ''
