from sql import Sql
sql = Sql

class Auth:
    def auth(header):
        error = {
            'error': 'Authority error',
            'error_code': '401'
        }
        accept = {
            'error': None,
            'error_code': None
        }
        if header is None and header == '':
            return error
        elif sql.authority(header=header) == 0:
            return error
        else:
            return accept
