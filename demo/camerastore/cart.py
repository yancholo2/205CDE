@app.route("/cart/add", methods=['POST'])
def add_to_cart():
    cart = ShoppingCart.add(product=request.form['product'], quantity=int(request.form['quantity']))
    return jsonify(cart)

@app.route("/cart")
def view_cart():
    cart = ShoppingCart.get()
    return render_template("cart.html", cart=cart)

@app.route("/cart/remove/<item_id>", methods=['POST'])
def remove_from_cart(item_id):
    cart = ShoppingCart.remove(item_id)
    return jsonify(cart)

