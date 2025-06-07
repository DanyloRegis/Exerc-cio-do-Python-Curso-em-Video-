def nota(*n, sit=False):
    """
    =>NOTA DO ALUNO
    """
    r = {
        "total": len(n),
        "maior": max(n),
        "menor": min(n),
        "media": sum(n)/len(n),
        "estado": ""
    }
    if sit:
        if r["media"] >= 7:
            r["estado"]="Boa"
        elif r["media"] == 6:
            r["estado"]="Ok"
        else:
            r["estado"]="Recuperacao"
    return r

resultado = nota(6, 8, 9,sit=True)
print(resultado)