from django.shortcuts import render
from django.apps import apps
import json
import random
import time

# Aqui guardo la data de los json en variables
devices_file = apps.get_app_config(
    'system_app').path + '/json-data/devices.json'
numbers_file = apps.get_app_config(
    'system_app').path + '/json-data/telephon_numbers.json'

# funcion para activar el render de la página


def alarm_status(request):
    with open(devices_file) as devices_data:
        devices = json.load(devices_data)
    with open(numbers_file) as numbers_data:
        phone_numbers = json.load(numbers_data)
    rand_num = random.randrange(0, 6)
    dataJson = json.dumps(devices)
    return render(request, 'systemalerts.html', {'devices': devices, 'number': phone_numbers[rand_num], 'data': dataJson})
