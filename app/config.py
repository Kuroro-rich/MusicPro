# from flask import Flask, request, jsonify
# from transbank import Webpay

# webpay = Webpay("INTEGRATION", "NombreComercio", "CodigoComercio", "ApiKeyComercio", "ApiSecretComercio")


class DevelopmentConfig():
    DEBUG=True
config = {
    'development': DevelopmentConfig
}

# # Lógica para iniciar el pago y generar la URL de pago en Transbank
# @app.route('/pago', methods=['POST'])
# def iniciar_pago():
#     monto = request.args.get('monto')
#     orden_compra = 'ORDEN123'  # Genera un número de orden único
#     response = webpay.transaction.create(
#         amount=monto,
#         buy_order=orden_compra,
#         return_url='http://tudominio.com/callback'
#     )
#     return redirect(response['url'])



# @app.route('/callback', methods=['POST'])
# def callback_pago():
#     token_ws = request.form['token_ws']
#     response = webpay.transaction.commit(token_ws)
#     if response.response_code == 0:
#         # Pago exitoso, guardar en la base de datos, etc.
#         return 'OK'
#     else:
#         # Pago rechazado o fallido, manejar el error adecuadamente
#         return 'Error'