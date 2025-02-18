import json
import src.core.models as models


def install_product(self):
    with open('src/resources/product.json', 'r') as f:
        data = json.load(f)
        product_measurements = data.get("product_measurements", [])
        products = data.get("products", [])

        for i in product_measurements:
            if not models.ProductMeasurement.objects.filter(name=i.get("name")):
                models.ProductMeasurement.objects.create(**i)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Product Measurement id: {i.get('id')}, name: {i.get('name')} created"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product Measurement id: {i.get('id')}, name: {i.get('name')} already exists"
                    )
                )

        for i in products:
            if not models.Product.objects.filter(name=i.get("name")):
                models.Product.objects.create(**i)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Products id: {i.get('id')}, name: {i.get('name')} created"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Products id: {i.get('id')}, name: {i.get('name')} already exists"
                    )
                )
