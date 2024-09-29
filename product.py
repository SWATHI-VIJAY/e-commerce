products=[
    {'id':1,'name':'laptop','price':1200.00},
    {'id':2,'name':'smartphone','price':800.00},
    {'id':3,'name':'headphones','price':150.00}
]
cart=[]
order_history=[]

def search_products(keyword):
    result=[product for product in products if keyword.lower() in product['name'].lower()]
    return result
def add_to_cart(product_id,quality):
    product=next((p for p in products if p['id']==product_id),None)
    if product:
        cart.append({'product':product,'quality':quality})
        return True
    return False
def view_cart():
    return cart
def checkout():
    if not cart:
        return "cart is empty.add items to the cart before checking out."
    total_amount=sum(item['product'][price]*item['quality']for item in cart)
    order_id=len(order_history)+1
    order={
        'order_id':order_id,
        'items':cart,
        'total_amount':total_amount
    }
    order_history.append(order)
    cart.clear()
    return order
def view_order_history():
    return order_history
def test_ecommerce_system():
    defects=[]

    search_result=search_product("laptop1")
    if len(search_result)!=1 or search_result[0]['name']!='laptop':
        defects.append({'test case':'product search(valid keyword)','error message':'product search did not return correct results for "laptop" '})
        search_result=search_product("nonexistent")
        if len(search_result)!=0:
            defects.append({'Test Case': 'Product Search (Invalid Keyword)', 'Error Message': 'Search returned results for an invalid keyword "nonexistent" '}) 
        if not add_to_cart(1,1):
            defects.append({'test case':'add to cart','error message':'failed to add product ith id 1 to the cart'})
        if not add_to_cart(2,2):
            defects.append({'test case':'add to cart','error message':'failed to add product ith id 1 to the cart'})
            cart_contents=view_cart()
            if len(cart_contents)!=2 or cart_content[0]['product']['name']!='laptop' or cart_contents[1]['product']['name']!='smartphone':
                defects.append({'test case':'checkout','error message':'cart does not contain expected items'})
                order=checkout()
                if not order or order['tota_amount']!=(1200.00+2*800.00):
                    defects.append({'test case':'checkout','error message':'checkout process failed or order total is incorrect'})
                    order_history_content=view_order_history()
                    if len(order_history_content)!=1 or order_history_content[0]['total_amount']!=(1200.00+2*800.00):
                         defects.append({'Test Case': 'Order History', 'Error Message': 'Order history does not contain expected orders or total amount is incorrect'})
                         return defects
                    if __name__ == "__main__":
                          
                          

                          defects=test_ecommerce_system()
                          if defects:
                        
                             print("defects reported:")
                             for defect in defects:
                                 print(f"Test Case: {defect['Test Case']}") 
                                 print(f"Error Message: {defect['Error Message']}") 
                                 print() 
                          else: 
                               print("All tests passed successfully.")

 






        