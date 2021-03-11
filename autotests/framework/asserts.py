import json
class Asserts:
    @staticmethod
    def status_code(response, code: int, message: str = ""):
        if response is not None:
            assert response.status_code == code, \
                f'Excepted status_code: {code}, but got: {response.status_code}.{message}'
        else:
            return f'Request is None'

    @staticmethod
    def elapsed_time(response, time: int, message: str = ""):
        if response is not None:
            assert response.elapsed.total_seconds() < time, \
                f'Excepted response time < {time}s, but got {response.elapsed.total_seconds()}.{message}'
        else:
            return f'Request is None'

    @staticmethod
    def check_id(response, message: str = ""):
        if response is not None:
            assert response.json()['id'] != '', \
                f'Empty ID'
            assert type(response.json()['id']) == int and response.json()['id'] is not None, \
                f'Excepted ID, but id -  {response.json()["id"]} not int.{message}'
        else:
            return f'Request is None'

    @staticmethod
    def json_has_key(response, key: int, message: str= ""):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does not have a key "{key}" which is expected. JSON text: "{response.text}"'

