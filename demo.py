import sys
from iol import ApiIOL

iol = ApiIOL()

while iol.token_error:
    user = input('Ingrese usuario o \"q\" para salir: ')
    if user == 'q':
        exit(0)
    password = input('Ingrese Password: ')

    body = {
        'username': user,
        'password': password,
        'grant_type': "password",
    }

    iol.req_token(body, True)
    print('código: ', iol.token_error_code)

print('access token:', iol.access_token)

while True:
    try:
        option = input(
            'Ingrese \"1\" para ver estado de cuenta.\n'
            'Ingrese \"2\" para ver su portafolio.\n'
            'Ingrese \"3\" para ver cotización cedear.\n'
            'Ingrese \"q\" para salir.\n'
            'opción:'
        )
        print('option: ', option)
        if option == 'q':
            print('Saliendo.')
            exit()
        elif option == '1':
            resp = iol.get(url='https://api.invertironline.com/api/v2/estadocuenta')
            print(resp)
        elif option == '2':
            resp = iol.get(url='https://api.invertironline.com/api/v2/portafolio/argentina')
            print(resp)
        elif option == '3':
            simbolo = input('símbolo: ')
            url = f'https://api.invertironline.com/api/v2/bCBA/Titulos/{simbolo}/CotizacionDetalle'
            resp = iol.get(url=url)
            print(resp)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
