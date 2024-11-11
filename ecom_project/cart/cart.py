from orbit.models import Product,Customer
class Cart():
    def __init__(self,request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        self.cart =cart

    def add(self,product,quantity):
        product_id=str(product.id)
        product_qty=str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified =True
        
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart=str(carty))

    def db_add(self,product,quantity):
        product_id=str(product)
        product_qty=str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified =True
        
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart=str(carty))


    def total(self):
        quantities=self.cart
        product_id=self.cart.keys()
        product= Product.objects.filter(id__in=product_id)
        
        total=0
        for key, value in quantities.items():
            key=int(key)
            for products in product:
                if products.id == key:
                    total= total + (products.price*value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def getproducts(self):
        product_id=self.cart.keys()
        product= Product.objects.filter(id__in=product_id)
        return product
    
    def getquants(self):
        quantities=self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id=str(product)
        product_qty=int(quantity)

        ourcart = self.cart

        ourcart[product_id]=product_qty

        self.session.modified =True

        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart=str(carty))

        thing = self.cart
        return thing
    
        
    
    def delete(self,product):
        product_id=str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified =True

        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")

            current_user.update(old_cart=str(carty))



