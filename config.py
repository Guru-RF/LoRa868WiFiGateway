hostname = "ctrlr0"

TCPports = {
    0: {
        'name': 'Loop NS',
        'httpReq': 'http://switch0.lan/port/1'
    },
    1: {
        'name': 'Loop EW',
        'httpReq': 'http://switch0.lan/port/2'
    },
    2: {
        'name': 'Loop',
        'httpReq': 'http://switch0.lan/port/4'
    },
    3: {
        'name': 'LOG',
        'httpReq': 'http://switch0.lan/port/3'
    },
}

LORAports = {
    0: {
        'name': 'Loop NS',
        'LoRaReq': 'sw0/1'
    },
    1: {
        'name': 'Loop EW ',
        'LoRaReq': 'sw0/2'
    },
    2: {
        'name': 'Loop',
        'LoRaReq': 'sw0/4'
    },
    3: {
        'name': 'LOG',
        'LoRaReq': 'sw0/3'
    },
}