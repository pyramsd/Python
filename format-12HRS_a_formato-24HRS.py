def convertir_horario(hora):
    
    _hora_ = hora.split(":")
    if hora[-2].lower() == "pm":
        if _hora_[0] != "12":
            _hora_[0] = str(int(_hora_[0]) + 12)

    else:
        if _hora_[0] == "12":
            _hora_[0] = "00"

    nueva_hora = ":".join(_hora_)

    return nueva_hora

print(convertir_horario("12:40PM"))