import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def get_scraping_data():
    '''Funcion que obtiene la data del scraping'''
    # Conexión al webdriver usando el driver para chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Ingresar al sitio
    driver.get("https://www.concesionesmaritimas.cl/")
    # Esperar unos 10 ms hasta carge el sitio y los datos necesarios
    driver.implicitly_wait(0.10)
    # Entrar al frame que contiene el iframe necesario
    driver.switch_to.frame('centro_sigmar')
    # Encontrar el iframe que contiene la tabla necesaria
    iframe = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/iframe')
    # Ya que el iframe no tiene ID, name o class, ingreso pasando el webelement
    driver.switch_to.frame(iframe)
    # Constante con la ruta base hacia los select
    BASE_SELECT = "/html/body/font/form/center/table[1]/tbody"
    # Obtener del select la region a usar, por defecto II
    select_region = driver.find_element(By.XPATH, f"{BASE_SELECT}/tr[2]/td[1]/select")
    region = Select(select_region)
    region.select_by_value("2")
    # Obtener del select la gobernacion a usar, por defecto Antofagasta
    select_gober = driver.find_element(By.XPATH, f"{BASE_SELECT}/tr[4]/td[1]/select")
    gobernacion = Select(select_gober)
    gobernacion.select_by_value("12")
    # Obtener del select la capitanía a usar, por defecto Antofagasta
    select_capuerto = driver.find_element(By.XPATH, f"{BASE_SELECT}/tr[6]/td/select")
    capuerto = Select(select_capuerto)
    capuerto.select_by_value("13")
    # Obtener la tabla a usar
    listado = driver.find_element(By.NAME, "verlistado")
    listado.click()
    # Lista donde se almacenaran los datos obtenidos como diccionarios
    data = []
    # Pag. de la primera tabla
    pag = 1
    # Constante del xpath base para acceder a las filas
    BASE_ROW = "/html/body/font/form/div/center/table/tbody"
    # Obtener datos de todas las páginas
    while True:
        # Obtener todas las filas de la tabla
        rows = driver.find_elements(By.XPATH, f"{BASE_ROW}/tr")
        # Recorrer las filas
        for row in rows[1:]:
            # Obtener todas las columnas de la fila
            columns = row.find_elements(By.TAG_NAME, "td")
            # Diccionario donde se almacenarán las columnas
            dict_rows = {}
            # Recorrer las columnas
            for i, c in enumerate(columns):
                # Convierto los indices en nombres de columnas
                if i == 0: i = "n"
                if i == 1: i = "n_concesion"
                if i == 2: i = "tipo_concesion"
                if i == 3: i = "comuna"
                if i == 4: i = "lugar"
                if i == 5: i = "n_rs_ds"
                if i == 6: i = "tipo_tramite"
                if i == 7: i = "concesionario"
                if i == 8: i = "tipo_vigencia"
                # Obtener el texto de la columna
                txt_columna = c.text
                # Agregar el texto de la columna al diccionario con
                # clave de nombre de columna
                dict_rows[i] = txt_columna
            # Agregar el diccionario la lista de datos de la tabla
            data.append(dict_rows)
        # Incrementar el número de pág. a la sgte.
        pag += 1
        # Romper el ciclo si el numero de pag. es 7
        if pag == 7:
            break
        # Constante con el xpath para acceder a los botones de sgte. tabla
        BASE_SGTE = "/html/body/font/form/p[4]/font/table/tbody/tr"
        # Buscar el elemento que contiene el numero de la sgte. tabla
        # y acceder con el método click
        driver.find_element(By.XPATH, f"{BASE_SGTE}/td[{pag}]/font/a").click()
    # Se cierra la ventana
    driver.quit()
    # retornamos el listado
    return data


def add_json_to_file(data):
    '''Funcion que crea y almacena el json en un archivo'''
    with open ('concesiones.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
