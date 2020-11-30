import requests

class Venta():

    def realizarVenta(self, producto, cantidad):
        requests.get('http://127.0.0.1:8081/facturas/nueva-factura/Tony_Stark')

        r = requests.get('http://127.0.0.1:8081/facturas/'+producto+'/'+cantidad)
        
        item_object = r.json()

        valor_total = 0

        for key, value in item_object.items():
            if key == 'valor_total':
                valor_total = value

        return valor_total


