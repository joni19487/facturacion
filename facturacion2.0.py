import csv
import time
import pandas as pd
from selenium import webdriver
import keyboard
import claves_fiscales

class Persona:
    def __init__(self, cuit, descripcion, cuit_receptor, importe):
        self.cuit = cuit
        self.descripcion = descripcion
        self.cuit_receptor = cuit_receptor
        self.importe = importe

def cargar_personas(desde_archivo):
    personas = []
    df = pd.read_csv(desde_archivo, encoding="latin-1")
    for _, datos in df.iterrows():
        cuit = str(datos['CUIT'])
        descripcion = str(datos['DESCRIPCION'])
        cuit_receptor = str(datos['CUIT RECEPTOR'])
        importe = str(datos['IMPORTE'])
        persona = Persona(cuit, descripcion, cuit_receptor, importe)
        personas.append(persona)
    return personas

ruta_descarga = r'C:\Users\SOLO OUTLOOK\Documents\facturacion\descargas'
driver_path = r'webdriver//chromedriver.exe'
FECHA = "29/05/2023"
DESDE = "01/05/2023"
HASTA = "31/05/2023"

def procesar_personas(personas):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": ruta_descarga}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    for persona in personas:
        cuit = persona.cuit
        descripcion = persona.descripcion
        cuit_receptor = persona.cuit_receptor
        importe = persona.importe

        time.sleep(1)
        driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
        driver.maximize_window()
        # INGRESAR CUIT
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(cuit)

        # SIGUIENTE
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
        # CLAVE FISCAL
        try:
            driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(claves_fiscales.clave_fiscal(cuit))

            # INGRESAR
            driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]').click()
            time.sleep(1)
            try:
                driver.find_element("xpath", '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]').click()
            except:
                pass
            time.sleep(1)
            driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').click()
            time.sleep(1)
            driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').send_keys("Comprobantes en Linea")
            time.sleep(2)
            driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/ul/li[1]/a/div/div/div[1]/div/p').click()
            time.sleep(1)
            driver.get('https://fe.afip.gob.ar/rcel/jsp/index_bis.jsp;jsessionid=8EC17D8A6C0B9E5A5799E72585A54007')
            window_before = driver.window_handles[0]
            window_after = driver.window_handles[1]
            driver.close()
            driver.switch_to.window(window_after)
            time.sleep(2)
            # SECCION DE LOS PAZ
            if cuit != '23263370899' and cuit != '23220992659' and cuit != '20266200952' and cuit != '20305266591' and cuit != '20240284643' and cuit != '20232501856' and cuit != '23311768999':
                driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]').click() # primera opcion
            elif cuit == '23220992659':
                driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[5]').click()
            elif cuit == '20266200952':
                driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[4]').click()
            else:
                driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[3]').click()

            time.sleep(2)
            driver.find_element("xpath", '/html/body/div[2]/table/tbody/tr[1]/td/a/span[2]').click()
            time.sleep(2)
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select').click()
            # SECCION VIONNET DONDE ELIJE PUNTO DE VENTA 2 SI CONCUERDA CUIT
            if cuit == '20253862425':
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[3]').click()
            else:
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]').click()
            time.sleep(1)
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
            time.sleep(3)
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').clear()
            time.sleep(1)
            if cuit != '20259816565':
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys(FECHA)
            else:
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys(FECHA)
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[3]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').clear()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').send_keys(DESDE)
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').clear()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').send_keys(HASTA)
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
            # SECCION DE SERJAN  DONDE ELIJE IVA EXCENTO
            if cuit_receptor == '20177088065':
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
            elif cuit_receptor == 'CONSUMIDOR FINAL':
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[4]').click()
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys('')
            elif cuit_receptor == '30529710204':
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
            else:
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[2]').click()
                driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[2]/tbody/tr[8]/th/input').click()
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[5]/input').send_keys(importe)
            driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[2]/textarea').send_keys(descripcion)
            driver.find_element("xpath", '/html/body/div[2]/form/input[8]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div[4]/input[2]').click()
            keyboard.press_and_release("enter")
            time.sleep(2)
            driver.find_element("xpath", '/html/body/div[2]/form/div[6]/input').click()
        except:
            ERROR = open("ERRONEOS.csv", "a")
            salida = cuit, descripcion, cuit_receptor, importe
            ERROR.write(salida)
            ERROR.write("\n")
            ERROR.close()
        driver.quit()

personas = cargar_personas("nuevo.csv")
procesar_personas(personas)
