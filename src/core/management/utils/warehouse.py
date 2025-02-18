import json
import src.core.models as models


def install_warehouse(self):
    with open('src/resources/warehouse.json', 'r') as f:
        data = json.load(f)

        for i in data:
            if not models.Warehouse.objects.filter(name=i.get("name")):
                models.Warehouse.objects.create(**i)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Warehouse id: {i.get('id')}, name: {i.get('name')} created"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Warehouse id: {i.get('id')}, name: {i.get('name')} already exists"
                    )
                )
