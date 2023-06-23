def corrector():
    nuevo=open('corregidos.csv','w')
    g=open("nuevo.csv","r")
    for dato in g.readlines():    
        if ';' in dato:
            dato= dato.replace(';',',')        
            nuevo.write(str(dato))

