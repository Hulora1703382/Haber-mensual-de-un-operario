#      CALCULO DEL HABER MENSUAL DE UN OPERARIO 
#  PRIMERAS DEFINICIONES Y VARIABLES 
#HABER MENSUAL ES hbm,  DATOS : SMV (smv)  , HIJOS MENORES DE EDAD ( hm)   ,  DÍAS TRABAJADOS ( data2 )  ,  TIPO DE CAMBIO SUNAT ( cambsu)  ,   DESC. ONP ( onp) , HABER BRUTO MENSUAL =HBM  Y  ,  HABER  NETO MENSUAL ES   hb "
    from turtle import onkeypress


hm=1
#  TIPO DE CAMBIO SUNAT = cambsu
    cambsu = 3.726
    data2=>30
    smv = 1050      
#SIENDO  SUELDO MÍNIMO VITAL  = smv 
     dtrab >=1
# SIENDO     DÍAS TRABAJADOS POR EL OPERADOR = dtrab 
#  CÁLCULO DE LA GRATIFICACIÓN
    grati = ( smv/ 180) * dtrab, 
    print (" GRATIFICACIÓN  = ", grati) 
# CÁLCULO   DE LAS   VACACIONES
#  PAGO DE VACACIONES = vac
    vac = (smv/360)* dtrab, 
    print ("  VACACIONES = " ,vac)
#  PAGO   CTS
#  SIENDO  CTS = cts
    cts = (( smv+1/6*smv)/180)*data2, 
    print (" CTS 0 ",cts):
# ASIGNACIÓN FAMILIAR ( af), ESTÁ REFERIDA A LOS HIJOS MENORES DE 18 AÑOS (hm) 
    hm=1
    af=(hm * 0.1*smv),
    print (" ASIGNACIÓN FAMILIAR = ", af) :
# SEGURO DE VIDA  LEY ( sv), PAGO OBLIGATORIO DE US $ 15 MENSUALE
# tipo de cambi sunat a la fecha = 3.726   Mar. 22"
    sv = (15*cambsu),
    print ( "seguro de vida = ",sv):
# EL HABER MENSUAL BRUTO DEL OPERARIO ES   (hbm)
    hbm = ( smv+grati+cts+af+sv),
    print (" HABER MENSUAL BRUTO A PAGAR ES = , hbm) : 
#  SOBRE LOS   DESCUENTOS   DE   LEY  A   EFECTUAR  
#    DESCUENTOS :  AFP/ ONP  ES DE 13%
    onp = 0.13*smv
    "   EL   HABER  NETO MENSUAL  , es  hb  
    hb = hbm - onp, 
    print ("HABER NETO ES = ",  hb):
        
