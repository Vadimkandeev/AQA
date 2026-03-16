class CurrencyConverter:

    @staticmethod
    def usd_to_eur(amount):
        eur = amount * 0.85
        return eur

    @staticmethod
    def eur_to_usd(amount):
        usd = 1.18 * amount
        return usd