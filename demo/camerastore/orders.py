@app.route("/checkout")
@login_required
def checkout():
    order = Order()
    order.customer = Customer.find_by_id(session['customer_id'])
    order.billingAddress = create_address()
    order.shippingAddress = create_address()
    form = CheckoutForm(obj=order)
    return render_template("orders/checkout.html", form=form)

@app.route("/orders/create", methods=['POST'])
@login_required
def place_order():
    form = CheckoutForm(request.form)
    if form.validate():
        order = Order(**form.data)
        order.customer.id = session['customer_id']
        paymentSource = request.form['token']
        transaction = Order.checkout(order, paymentSource)
    return redirect("/orders/{id}".format(id=transaction.order.id))

@app.route("/orders")
@login_required
def index():
    orders = Order.find_all_by_customer(customer=session['customer_id'])
    return render_template("orders/index.html", orders=orders)

@app.route("/orders/<order_id>")
@login_required
def show(order_id):
    try:
        order = Order.find_by_id(order_id)
        return render_template("orders/show.html", order=order)
    except EntityNotFoundException as e:
        abort(404)

@app.route("/orders/refund/<order_id>", methods=['POST'])
def refund(order_id):
    transaction = Order.refund(order_id)
    return redirect("/orders/{id}".format(id=transaction.order.id))
