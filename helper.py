def date_format(date):
    months = (
      "Enero",
      "Febrero",
      "Marzo",
      "Abril",
      "Mayo",
      "Junio",
      "Julio",
      "Agosto",
      "Septiembre",
      "Octubre",
      "Noviembre",
      "Diciembre"
    )
    month = months[date.month - 1]
    return "{} de {} de {}".format(date.day, month, date.year)