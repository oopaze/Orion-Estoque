import json


def get_detail_instance(instance, ignore_fields=[], last_fields=[]):
    attrs = []
    last_attrs = []

    for field in instance._meta.fields:
        value = getattr(instance, field.name) if not field.choices else getattr(instance, f"get_{field.name}_display")()

        if field.name in ignore_fields:
            pass

        elif field.name in last_fields:
            last_attrs.append({
                "value": value if value is not None else "",
                "label": field.verbose_name,
                "name": field.name,
            })

        else:
            attrs.append({
                "value": value if is not None else "",
                "label": field.verbose_name,
                "name": field.name,
            })

    attrs.extend(last_attrs)

    return attrs


def get_bairros_choice(cidade=None):
    try:
        if cidade:
            with open(f"static/bairros_{cidade}.json", 'r') as f:
                return [(bairro.replace(" ", "_"), f"{bairro} ({cidade})") for bairro in json.loads(f.read())]

        else:
            with open("static/bairros_Crato.json", 'r') as f:
                bairros_crato = [
                    (bairro.replace(" ", "_"), f"{bairro} (Crato)") for bairro in json.loads(f.read())
                ]

            with open("static/bairros_Juazeiro do Norte.json", 'r') as f:
                bairros_jn = [
                    (bairro.replace(" ", "_"), f"{bairro} (Juazeiro do Norte)") for bairro in json.loads(f.read())
                ]

        return bairros_crato + bairros_jn

    except FileNotFoundError:
        return (("", "-------"),)
