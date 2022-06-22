from django.shortcuts import render
from django.apps import apps
import json
import random
import time


devices_file = apps.get_app_config(
    'system_app').path + '/json-data/devices.json'
numbers_file = apps.get_app_config(
    'system_app').path + '/json-data/telephon_numbers.json'


def alarm_status(request):
    while(True):
        time.sleep(3)
        with open(devices_file) as devices_data:
            devices = json.load(devices_data)
        with open(numbers_file) as numbers_data:
            phone_numbers = json.load(numbers_data)
        rand_num = random.randrange(0, 6)
        dataJson = json.dumps(devices)
        return render(request, 'systemalerts.html', {'devices': devices, 'number': phone_numbers[rand_num], 'data': dataJson})
