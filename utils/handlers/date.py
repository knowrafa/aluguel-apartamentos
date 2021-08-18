from datetime import datetime

from dateutil.parser import parse


def parse_date_to_iso(date: str) -> datetime:
    """
    Recebe uma data e devolve uma data no padrão iso
    """
    if date.count("/") == 1:
        return datetime.strptime(date, "%m/%Y")
    elif date.count("-") == 1:
        return datetime.strptime(date, "%Y-%m")
    elif date.count("/") == 2:
        return datetime.strptime(date, "%d/%m/%Y")
    elif date.count("-") == 2:
        return datetime.strptime(date, "%Y-%m-%d")
    return parse(date)
