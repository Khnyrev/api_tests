""" Methods for check our requests"""
import json

from requests import Response


class Checking():

    """Method for status-code check"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Successful! STATUS_CODE = " + str(result.status_code))

    """ Method fot mandatory fields check"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("all fields are OK!")


    """ Method fot fields values check"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, print("Get operation failed, looks like place_id  doesn't exists")
        print(field_name + ' Верен')
