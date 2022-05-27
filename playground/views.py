
from django.shortcuts import render
from django.db.models import Value, F,Func
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product, customer
from tags.models import TaggedItem


# views in django is equal to Request response handler
def say_hello(request):
    #query_set = TaggedItem.objects.get_tags_for(Product,1)
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk = 1)
    collection.save()

    #Collection.objects.create(title='Shoes', product_featured_id = 2)
    return render(request,'hello.html',{'name': 'Mushtaq'})#, 'result': list(query_set)})
