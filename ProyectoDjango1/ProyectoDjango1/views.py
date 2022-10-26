"""Creamos ProyectoCuello"""
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader


def saludo(request: bool) -> HttpResponse:
    """_summary_

    Args:
        request (bool): _description_

    Returns:
        HttpResponse: _description_
    """
    return HttpResponse("Hola mundo")


def hoy(request: bool) -> HttpResponse:
    """_summary_

    Args:
        request (bool): _description_

    Returns:
        HttpResponse: _description_
    """
    return HttpResponse(f"Hoy es : {datetime.now()}")


def saludo_nombre(request: bool, nombre: str) -> HttpResponse:
    """_summary_

    Args:
        request (bool): _description_

    Returns:
        HttpResponse: _description_
    """
    return HttpResponse(f"mi nombre es : {nombre}")


def saludo_template(request: bool, nombre) -> HttpResponse:
    """_summary_

    Args:
        request (bool): _description_

    Returns:
        HttpResponse: _description_
    """
    # with open("C:/Users/GUSTAVO/OneDrive/GOOGLE DRIVE/Gustavo/Curso programacion/Coder House/proyectoCuello/proyectoCuello-cywIjlS6/ProyectoDjango1/ProyectoDjango1/templates/template1.html") as miHtml:
    #    plantilla = Template(miHtml.read())
    # mi_contexto = Context()
    # documento = plantilla.render(mi_contexto)
    # plantilla = loader.get_template("template1.html")
    # return HttpResponse(plantilla.render(Context({'my_name': nombre, 'notas': [8, 5, 9, 10]})))
    documento = (loader.get_template("template1.html")).render(
        {"my_name": nombre, "notas": [8, 5, 4, 10]}
    )
    return HttpResponse(documento)
