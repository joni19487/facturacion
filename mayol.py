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

df = pd.read_csv("nuevo.csv", encoding="latin-1")

for row, datos in df.iterrows():
    
    cuitreal=str(datos['CUIT'])    
    descripcion=str(datos['DESCRIPCION'])
    cuit_receptor=str(datos['CUIT RECEPTOR'])
    importe=str(datos['IMPORTE'])
         
         
    

#    print("-"+cuit+"-","-"+clave+"-")
    time.sleep(1)
    driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
    driver.maximize_window()
    # INGRESAR CUIT
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(cuitreal)
    
    # SIGUIENTE
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
    # CLAVE FISCAL
   
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(claves_fiscales.clave_fiscal(cuitreal))

    #INGRESAR
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]').click()
    time.sleep(1)
    #MIS SERVICIOS
    driver.find_element("xpath", '/html/body/div/div/main/section[1]/div/ul/li[3]/a/span').click()
    #SLEEP
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div/main/div[2]/section[1]/div/div[1]/div/div/div/div[1]/input').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div/main/div[2]/section[1]/div/div[1]/div/div/div/div[1]/input').send_keys("Comprobantes en Linea")
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div/main/div[2]/section[1]/div/div[1]/div/div/div/ul/li[1]/a/div/div[1]/span[1]').click()
    time.sleep(1)
    driver.get('https://fe.afip.gob.ar/rcel/jsp/index_bis.jsp;jsessionid=8EC17D8A6C0B9E5A5799E72585A54007')
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.close()
    driver.switch_to.window(window_after)
    time.sleep(1)
    #SECCION DE LOS PAZ              
    if cuitreal!='23263370899' and cuitreal!='23220992659' and cuitreal !='20266200952' and cuitreal !='20305266591' and cuitreal !='20240284643' and cuitreal !='20232501856' and cuitreal !='23311768999':
        driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]').click() #primera opcion   
    elif cuitreal=='23220992659':
        driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[5]').click()
    elif cuitreal=='20266200952':
        driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[4]').click()
    else :
        driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[3]').click()
            
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/table/tbody/tr[1]/td/a/span[2]').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select').click()
    #time.sleep(1)
    #SECCION VIONNET DONDE ELIJE PUNTO DE VENTA 2 SI CONCUERDA CUIT
    if cuitreal=='20253862425':
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[3]').click()
    else:
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]').click()
    time.sleep(1)
    driver.find_element("xpath", ' /html/body/div[2]/form/input[2]').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').clear()
    time.sleep(1)
    if cuitreal!= '20259816565':
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys("30/09/2022")
    else:
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys("29/09/2022")
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select').click()
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[3]').click()
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').clear()
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').send_keys("01/09/2022")
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').clear()
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').send_keys("30/09/2022")
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
    #time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
    #time.sleep(1)
    #SECCION DE SERJAN  DONDE ELIJE IVA EXCENTO
    if cuit_receptor=='20177088065':
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click() # exento      
    elif cuitreal == '20220812600' or cuitreal == '27296751214':
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[4]').click() # consumidor final
    else:
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[2]').click() # responsable inscripto
    if cuitreal == '20220812600' or cuitreal == '27296751214':
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys('')
    else:
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(cuit_receptor)
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
    



