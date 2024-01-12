import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyBlog.settings')
import django
django.setup()
from Blog.models import ProductDetails
from faker import Faker
fn=Faker()
def populateData(N=5):
    for entry in range(N):
        fake_title=fn.name()
        fake_text=fn.text()

        fake_data=ProductDetails.objects.get_or_create(news_title=fake_title,news_text=fake_text)[0]

if __name__=='__main__':
    print('Building')
    populateData(20)
    print("Completed")

