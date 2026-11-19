class ReglaNegocioError(Exception):
    """Una operación viola una regla de negocio (RN-xx). Se responde con 409."""

    def __init__(self, mensaje: str, regla: str | None = None):
        """Guarda el mensaje y, si aplica, el identificador de la regla de negocio violada."""
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.regla = regla


class NoEncontradoError(Exception):
    """Un registro buscado no existe o ya no es válido. Se responde con 404."""

    def __init__(self, mensaje: str):
        """Guarda el mensaje que se devuelve al cliente de la API."""
        super().__init__(mensaje)
        self.mensaje = mensaje
