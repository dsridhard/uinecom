import requests
from concurrent.futures import ThreadPoolExecutor
from celery import shared_task
from uincom.models import Product

@shared_task
def fetch_products_task():
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
                for product in products:
                    product['source'] = source_name
                return products
        except:
            return []
        return []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_from_source, src, url) for src, url in sources.items()]
        for future in futures:
            all_products.extend(future.result())

    # Deduplication by name (case insensitive)
    unique_products = {}
    for product in all_products:
        key = product.get('name', '').strip().lower()
        if key and key not in unique_products:
            unique_products[key] = product

    for product in unique_products.values():
        Product.objects.get_or_create(
            name=product.get('name'),
            defaults={
                'price': product.get('price'),
                'image': product.get('image', ''),
                'source': product.get('source'),
            }
        )
