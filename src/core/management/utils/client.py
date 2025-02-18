import json
import src.core.models as models


def install_client(self):
    with open('src/resources/client.json', 'r') as f:
        data = json.load(f)

        for i in data:
            if not models.BusinessPartner.objects.filter(full_name=i.get("full_name")):
                models.BusinessPartner.objects.create(**i)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Business Partner id: {i.get('id')}, full name: {i.get('name')} created"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Business Partner id: {i.get('id')}, full name: {i.get('full_name')} already exists"
                    )
                )
