import requests

URL = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'

def get_jurisprudences(payload):
    '''Metodo para obtener las jurisprudencias'''
    r = requests.post(URL, json=payload)
    data = r.json()['jurisprudencias']
    if data == []:
        return []
    return data
