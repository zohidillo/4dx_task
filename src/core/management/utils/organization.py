import json
import src.core.models as models


def install_organization(self):
    with open('src/resources/organization.json', 'r') as f:
        data = json.load(f)

        for i in data:
            if not models.Organization.objects.filter(name=i.get("name")):
                models.Organization.objects.create(**i)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Organization id: {i.get('id')}, name: {i.get('name')} created"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Organization id: {i.get('id')}, name: {i.get('name')} already exists"
                    )
                )
