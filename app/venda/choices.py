from core.utils import get_bairros_choice


METODOS_PAGAMENTO = (
    ('dinheiro', "Dinheiro"),
    ('cartão', "Cartão"),
)

CIDADES = (
    ("juazeiro_do_norte", "Juazeiro do Norte"),
    ("crato", "Crato")
)

BAIRROS = get_bairros_choice()

TIPO_CONTATO = (
    ("redes_sociais", "Redes Sociais"),
    ("indicacao", "Indicação"),
    ("wpp", "WhatsApp")
)