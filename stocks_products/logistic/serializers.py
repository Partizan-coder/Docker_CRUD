from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
       model = Product
       fields = ['id', 'title', 'description']
       # настройте сериализатор для продукта
    pass


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
       model = StockProduct
       fields = ['id', 'product', 'quantity', 'price']
    # настройте сериализатор для позиции продукта на складе
    pass


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)


        # positionItems = {}
        # for position in positions:
        #     for key, value in position.items():
        #         positionItems.setdefault(key, value)
        #
        # stockProduct, created = StockProduct.objects.update_or_create(
        #     stock=stock.id,
        #     product=positionItems.get('product'),
        #     quantity=positionItems.get('quantity'),
        #     price=positionItems.get('price')
        # )
        # class StockProductSerializer(serializers.ModelSerializer):
        #     model = StockProduct
        #     fields = ['id', 'stock', 'product', 'quantity', 'price']
        #
        #     def create(self, positions):
        #         # достаем связанные данные для других таблиц
        #
        #         stockProduct = super().create(positions)



        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
