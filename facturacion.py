from selenium import webdriver
import keyboard
import time
import pandas as pd
import claves_fiscales
import os
driver= r'webdriver//chromedriver.exe'
#RUTA DE DESCARGA DEL EXCEL MIS COMPROBANTES
ruta_descarga=r'C:\Users\SOLO OUTLOOK\Documents\facturacion\descargas' #ACA SE PUEDE CAMBIAR CON UN INPUT
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" :  ruta_descarga}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=driver, options=chromeOptions)
FECHA= "29/05/2023"
DESDE= "01/05/2023"
HASTA= "31/05/2023"

df = pd.read_csv("nuevo.csv", encoding="latin-1")

for row, datos in df.iterrows():
    
    cuitreal=str(datos['CUIT'])
    descripcion=str(datos['DESCRIPCION'])
    cuit_receptor=str(datos['CUIT RECEPTOR'])
    importe=str(datos['IMPORTE'])    
            
    time.sleep(1)
    driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
    driver.maximize_window()
    # INGRESAR CUIT
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(cuitreal)
    
    # SIGUIENTE
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
    # CLAVE FISCAL
    try:
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(claves_fiscales.clave_fiscal(cuitreal))

        #INGRESAR
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
        #SECCION DE LOS PAZ              
        if cuitreal!='23263370899' and cuitreal!='23220992659' and cuitreal !='20266200952' and cuitreal !='20305266591' and cuitreal !='20240284643' and cuitreal !='20232501856' and cuitreal !='23311768999':
            driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]').click() #primera opcion   
        elif cuitreal=='23220992659':
            driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[5]').click()
        elif cuitreal=='20266200952':
            driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[4]').click()
        else :
            driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[3]').click()
                
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/table/tbody/tr[1]/td/a/span[2]').click()
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select').click()
        #time.sleep(1)
        #SECCION VIONNET DONDE ELIJE PUNTO DE VENTA 2 SI CONCUERDA CUIT
        if cuitreal=='20253862425':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[3]').click()
        else:
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]').click()
        time.sleep(1)
        driver.find_element("xpath", ' /html/body/div[2]/form/input[2]').click()
        time.sleep(3)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').clear()
        time.sleep(1)
        if cuitreal!= '20259816565':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys(FECHA)
        else:
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys(FECHA)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[3]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').clear()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').send_keys(DESDE)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').clear()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').send_keys(HASTA)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
        #time.sleep(1)
        #SECCION DE SERJAN  DONDE ELIJE IVA EXCENTO
        if cuit_receptor=='20177088065':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
        elif cuit_receptor=='CONSUMIDOR FINAL':
            driver.find_element("xpath", '//html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[4]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys('')
        elif cuit_receptor=='30529710204':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)            
        else:
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[2]').click()
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
        #time.sleep(1)       
        
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[2]/tbody/tr[8]/th/input').click()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[5]/input').send_keys(importe)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[2]/textarea').send_keys(descripcion)
        
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/input[8]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[4]/input[2]').click()
        #time.sleep(1)
        keyboard.press_and_release("enter")
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/div[6]/input').click()
    except:
         ERROR=open("ERRONEOS.csv","a")
         ERROR.write("DE " + ";" + cuitreal + ";" + " CLAVE FISCAL ERRONEA O ERROR A " +";" + cuit_receptor + "\n")

