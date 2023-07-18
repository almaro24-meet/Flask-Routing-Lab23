from flask import Flask, redirect, request, render_template, url_for


app = Flask(  
    __name__,
    template_folder='templates',  
    static_folder='static'  
)

@app.route('/')
def main1():
    return render_template("home.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/product')
def product():
    return render_template("product.html")

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
