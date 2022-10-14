def segundo():
      horasSemanales = 48
      precioPorHora = 2000

      salarioBrutoMensual = horasSemanales * 4.2 * precioPorHora
      deduccion1 = salarioBrutoMensual * 0.105
      deduccion2 = (salarioBrutoMensual - deduccion1) * 0.05
      gananciasConCargasSociales = salarioBrutoMensual - deduccion2
      print("El salario bruto mensual es de:", salarioBrutoMensual, " y el salalario neto sería de:",
            gananciasConCargasSociales)

def primero():
      horasSemanales = 48
      precioPorHora = 2000

      salarioBrutoMensual = horasSemanales * 4.2 * precioPorHora
      deduccion = salarioBrutoMensual * 0.105 + salarioBrutoMensual * 0.05
      gananciasConCargasSociales = salarioBrutoMensual - deduccion
      print("El salario bruto mensual es de:", salarioBrutoMensual, " y el salalario neto sería de:",
            gananciasConCargasSociales)

print("Primero")
primero()

print("Segundo")
segundo()