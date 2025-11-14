from django.utils.text import slugify
from faker import Faker

from ..models import Address, Author, Book, Country

faker = Faker()
def seed_data(authors_count:int = 10 , books_per_author:int =10 , countries_count:int = 10 , countries_per_book :int= 3):
    Author.objects.all().delete()
    Address.objects.all().delete()
    Book.objects.all().delete()
    Country.objects.all().delete()
    for _ in range(countries_count) :
        Country.objects.create(
            name=faker.country() ,
            code=faker.country_code()
        )
    countries = Country.objects.all()
    for _ in range(authors_count):
        address = Address.objects.create(
            street=faker.street_address() ,
            postal_code= faker.random_int(min=1000 , max=9999).__str__() ,
            city= faker.city()
        )
        author = Author.objects.create(
            first_name=faker.first_name() ,
            last_name = faker.last_name() ,
            address=address
        )
        for _ in range(books_per_author):
            title = faker.sentence(nb_words=4).rstrip('.')
            book = Book.objects.create(
                title=title ,
                description= faker.paragraph(nb_sentences=4) ,
                author=author  ,
                rating=faker.random_int(min=0,max=5) ,
                is_bestselling=faker.boolean(chance_of_getting_true=50) ,
                slug=slugify(title)
            )
            book.published_countries.set(faker.random_choices(countries , countries_per_book))

    print(f"{authors_count} authors created and each author have {books_per_author} books created")
