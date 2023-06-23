from selenium import webdriver
import keyboard
import time
import pandas as pd


driver= r'webdriver//chromedriver.exe'
#RUTA DE DESCARGA DEL EXCEL MIS COMPROBANTES
ruta_descarga=r'C:\Users\SOLO OUTLOOK\Documents\facturacion' #ACA SE PUEDE CAMBIAR CON UN INPUT
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" :  ruta_descarga}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=driver, options=chromeOptions)
CUIT='20084647706'
CLAVE_FISCAL='Juancarlos2022'
FECHA = "29/05/2023"

df = pd.read_csv("BAGNAT.csv", encoding="latin-1")

for row,datos in df.iterrows():
    tipo=str(datos['TIPO'])
    descripcion=str(datos['DESCRIPCION'])
    cuit_receptor=str(datos['CUIT RECEPTOR'])
    fecha=str(datos['FECHA'])
    importe=str(datos['IMPORTE'])
    condicion=str(datos['CONDICION'])
    

#    print("-"+cuit+"-","-"+clave+"-")
    time.sleep(1)
    driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')
    driver.maximize_window()
    # INGRESAR CUIT
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').clear()
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input').send_keys(CUIT)
    
    # SIGUIENTE
    driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/input[2]').click()
    # CLAVE FISCAL
    try: 
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[2]').send_keys(CLAVE_FISCAL)

        #INGRESAR
        driver.find_element("xpath", '/html/body/main/div/div/div/div/div[1]/div/form/div/input[3]').click()
        #MIS SERVICIOS
        #SLEEP
        time.sleep(1)
        try:
            driver.find_element("xpath", '/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]').click()
        except:
            pass
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').click()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[1]/input').send_keys("Comprobantes en Linea")
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/ul/li[1]/a/div/div/div[1]/div/p').click()
        time.sleep(1)
        driver.get('https://fe.afip.gob.ar/rcel/jsp/index_bis.jsp;jsessionid=8EC17D8A6C0B9E5A5799E72585A54007')
        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.close()
        driver.switch_to.window(window_after)
        time.sleep(2)
        #SECCION DE LOS PAZ              
        #if cuitreal!='23220992659' and cuitreal !='20266200952':
        #    driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]').click()
        #elif cuitreal=='23220992659':
        #    driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[5]').click()
        #elif cuitreal=='20266200952':
        #    driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[4]').click()
        #else :
        #    driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[3]').click()
                
        #time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/table/tbody/tr[4]/td/input[2]').click()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/table/tbody/tr[1]/td/a/span[2]').click() 
        
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select').click()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]').click()
        time.sleep(1)
        if tipo=='FACTURA B':
            driver.find_element("xpath",'/html/body/div[2]/form/div/div/table/tbody/tr[3]/td/div/select/option[5]').click()
        else:
            driver.find_element("xpath",'/html/body/div[2]/form/div/div/table/tbody/tr[3]/td/div/select/option[1]').click()
        #SECCION VIONNET DONDE ELIJE PUNTO DE VENTA 2 SI CONCUERDA CUIT
        #if cuitreal=='20253862425':
        #    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[3]').click()
        #else:
        #    driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/select/option[2]').click()
        time.sleep(1)
        driver.find_element("xpath", ' /html/body/div[2]/form/input[2]').click()
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').clear()
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]').send_keys(FECHA)
            
        time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[2]/td/select/option[3]').click()
        time.sleep(1)
        
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').clear()
        time.sleep(1)

        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td/input[1]').send_keys(str(fecha))
        time.sleep(1)
        
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').clear()
        time.sleep(1)

        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/input[1]').send_keys(str(fecha))
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
        #time.sleep(1)
        #SECCION DE SERJAN  DONDE ELIJE IVA EXCENTO
        if condicion=='CONSUMIDOR FINAL':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
        elif condicion=='MONOTRIBUTO': 
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
            time.sleep(1)      
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[3]').click()
        elif condicion=='RESPONSABLE INSCRIPTO':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select').click()
            time.sleep(1) 
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[1]/td/select/option[2]').click()
        
        if condicion=='MONOTRIBUTO'or condicion=='RESPONSABLE INSCRIPTO':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input[2]').send_keys(str(cuit_receptor))
        elif condicion=='CONSUMIDOR FINAL':
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[2]/td/input').send_keys(str(cuit_receptor))
        time.sleep(1)  
        driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[2]/tbody/tr[8]/th/input').click()
        time.sleep(1)
        try:
            driver.find_element("xpath", '/html/body/div[2]/form/div/div/table[1]/tbody/tr[4]/td/div/input').send_keys(".")
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        except:
            time.sleep(1)
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        
        
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[5]/input').send_keys(importe)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[2]/textarea').send_keys(descripcion)
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[1]/div/table/tbody/tr[2]/td[9]/select/option[8]').click()
        time.sleep(1)
        if condicion=='MONOTRIBUTO'or condicion=='RESPONSABLE INSCRIPTO':
            driver.find_element("xpath", '/html/body/div[2]/form/input[2]').click()
        else:
            driver.find_element("xpath", '/html/body/div[2]/form/input[8]').click()
        #time.sleep(1)
        driver.find_element("xpath", '/html/body/div[2]/form/div[4]/input[2]').click()
        #time.sleep(1)
        keyboard.press_and_release("enter")
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div[2]/form/div[6]/input').click()
        
    except:
        ERROR=open("ERRONEOS BAGNAT.csv","a")
        ERROR.write(cuit_receptor + "  CLAVE FISCAL ERRONEA O ERROR" + "\n")

