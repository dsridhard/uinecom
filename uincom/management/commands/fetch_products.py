import requests
from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from uincom.models import Product
from uincom.tasks import fetch_products_task

class Command(BaseCommand):
    help = 'Fetches products from multiple APIs concurrently and stores them in the unified Product model'

    def handle(self, *args, **kwargs):
        self.stdout.write("📡 Triggering Celery task to fetch product data...")
        fetch_products_task.delay()
        self.stdout.write(self.style.SUCCESS("✅ Product fetch task has been scheduled."))
        sources = {
            'TechMart': 'http://localhost:5000/techMartProducts',
            'StyleShop': 'http://localhost:5000/styleShopProducts'
        }

        all_products = []

        def fetch_from_source(source_name, url):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    products = response.json()
                    self.stdout.write(self.style.SUCCESS(f"✅ Fetched {len(products)} from {source_name}"))
                    for product in products:
                        product['source'] = source_name  # attach source to each product
                    return products
                else:
                    self.stdout.write(self.style.ERROR(f"❌ Failed to fetch from {source_name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"⚠️ Error fetching from {source_name}: {e}"))
            return []

        # Fetch concurrently
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(fetch_from_source, source, url)
                for source, url in sources.items()
            ]
            for future in futures:
                all_products.extend(future.result())

        # Deduplicate based on name (and optionally price)
        unique_products = {}
        for product in all_products:
            key = product.get('name', '').strip().lower()
            if key and key not in unique_products:
                unique_products[key] = product

        total_added = 0
        for key, product in unique_products.items():
            name = product.get('name')
            price = product.get('price')
            image = product.get('image', '')
            source = product.get('source')

            obj, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'price': price,
                    'image': image,
                    'source': source
                }
            )

            if created:
                total_added += 1
                self.stdout.write(f"🆕 Added: {name} ({source})")
            else:
                self.stdout.write(f"↩️ Duplicate skipped: {name}")

        self.stdout.write(self.style.SUCCESS(f"🎉 {total_added} new unique products added!"))
