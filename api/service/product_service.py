from api.model.product import Product
from api.dto.product_dto import ProductDTO


class ProductService:
    def __init__(self):
        pass

    def get_product_by_product_id(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
            category_name = product.category.name if product.category else ""
            return ProductDTO(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                discount_rate=product.discount_rate,
                coupon_applicable=product.coupon_applicable,
                category_name=category_name
            )
        except:
            return None

    def list_all_products(self, category: str):
        filters = {}
        if category:
            filters["category__name"] = category
        products = Product.objects.filter(**filters)
        product_dtos = []
        for product in products:
            category_name = product.category.name if product.category else None
            product_dto = ProductDTO(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                discount_rate=product.discount_rate,
                coupon_applicable=product.coupon_applicable,
                category_name=category_name
            )
            product_dtos.append(product_dto)
        return product_dtos
