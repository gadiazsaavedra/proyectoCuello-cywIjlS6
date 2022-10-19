"""Creamos ProyectoCuello"""
from django.http import HttpResponse


def saludo(request: bool) -> HttpResponse:
    """_summary_

    Args:
        request (bool): _description_

    Returns:
        HttpResponse: _description_
    """
    return HttpResponse("Hola mundo")
