from django.utils.translation import ugettext_lazy as _


class CompraChoices:

    @staticmethod
    def itens():
        """
        Define you own acesses here.
        :return: Tuple's list with acesses keys and values.
        """
        return (
            ('comida', _('Comida')),
        )
