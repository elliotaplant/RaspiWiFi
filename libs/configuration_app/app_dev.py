from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    wifi_ap_array = scan_wifi_networks()
    config_hash = config_file_hash()

    return render_template('app.html', wifi_ap_array=wifi_ap_array, config_hash=config_hash)


@app.route('/manual_ssid_entry')
def manual_ssid_entry():
    return render_template('manual_ssid_entry.html')


@app.route('/wpa_settings')
def wpa_settings():
    return render_template('wpa_settings.html', wpa_enabled=False, wpa_key=None)


@app.route('/save_credentials', methods=['GET', 'POST'])
def save_credentials():
    ssid = request.form['ssid']
    wifi_key = request.form['wifi_key']
    config_hash = config_file_hash()

    print('save_credentials', ssid, wifi_key)

    return render_template('save_credentials.html', ssid=ssid, config_hash=config_hash)


@app.route('/save_wpa_credentials', methods=['GET', 'POST'])
def save_wpa_credentials():
    wpa_enabled = request.form.get('wpa_enabled')
    wpa_key = request.form['wpa_key']
    print('save_wpa_credentials', wpa_enabled, wpa_key)
    return render_template('save_wpa_credentials.html',
                           wpa_enabled=wpa_enabled,
                           wpa_key=wpa_key)


def scan_wifi_networks():
    return ['network 1', 'network 2']


def create_wpa_supplicant(ssid, wifi_key):
    print('create_wpa_supplicant', ssid, wifi_key)


def set_ap_client_mode():
    print('set_ap_client_mode')


def config_file_hash():
    return {
        'ssl_enabled': '0',
        'server_port': '8080',
        'auto_config_delay': '300'
    }


if __name__ == '__main__':
    config_hash = config_file_hash()

    if config_hash['ssl_enabled'] == "1":
        app.run(host='0.0.0.0', port=int(config_hash['server_port']), ssl_context='adhoc')
    else:
        app.run(host='0.0.0.0', port=int(config_hash['server_port']))
