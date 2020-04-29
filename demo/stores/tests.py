from django.test import TestCase

from .models import Store, Book, Category


# Create your tests here.

# Functions init DB Category,Book,Store
def create_store(name, address, phone, email):
    return Store.objects.create(name=name, address=address, phone=phone, email=email)


def create_category(name, store_id):
    return Category.objects.create(name=name, store_id=store_id)


def create_book(name, author, category_id, cost, page_number):
    return Book.objects.create(
        name=name, author=author, category_id=category_id, cost=cost, page_number=page_number)


# Test of store model
class StoreModelTests(TestCase):

    # Test create stores in database
    def test_create_store(self):
        # Get all stores in database
        stores = Store.objects.all()
        self.assertEquals(stores.count(), 0)
        # Create store in database
        store = create_store('Store Test', 'USA', '12345678', 'store@gmail.com')
        self.assertEqual(store, Store.objects.get(pk=store.id))
        # Get all store in DB after create store
        stores = Store.objects.all()
        self.assertEquals(stores.count(), 1)

    # Test get category of store in DB
    def test_category_of_store(self):
        # Init 2 store in DB
        store = create_store('Store', 'USA', '12345678', 'store@gmail.com')
        store2 = create_store('Store 2', 'USA', '12345678', 'stores2@gmail.com')
        # Init 5 category in 2 store : store1, store2
        for i in range(3):
            create_category('Category' + str(i), store.id)
        for i in range(3, 5, 1):
            create_category('Category' + str(i), store2.id)

        # Get list category in object
        categories_store1 = Category.objects.filter(store_id=store.id)
        categories_store2 = Category.objects.filter(store_id=store2.id)
        categories = Category.objects.all()
        # Check count list category each store
        self.assertEqual(categories_store1.count(), 3)
        self.assertEqual(categories_store2.count(), 2)
        self.assertEqual(categories.count(), 5)
        # Print list category each store
        print(f'Store1:{categories_store1}')
        print(f'Store2:{categories_store2}')

    # Test books in stores
    def test_books_of_store(self):
        # Init store DB
        store = create_store('Store', 'USA', '12345678', 'store@gmail.com')
        # Init category, book in store
        category_pks = []
        for i in range(3):
            category = create_category('Category' + str(i), store.id)
            # Add pk of category in list category pk
            category_pks.append(category.id)
            # create book
            create_book('Book Category' + str(i), 'Author', category.id, 50.2, 500)
        # Get books of stores with category
        books_store = Book.objects.filter(category_id__in=category_pks)
        # Get books of method of Store
        books_store2 = store.books_of_store()
        # Check by assert
        self.assertEqual(books_store.count(), len(category_pks))
        self.assertEqual(books_store2.count(), books_store.count())
        self.assertEqual(len(books_store2), len(books_store))
