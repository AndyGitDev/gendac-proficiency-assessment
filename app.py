from flask import Flask, render_template, url_for, request, redirect
from src.utils import *

app = Flask(__name__)
gendacPath = "https://gendacproficiencytest.azurewebsites.net/API/ProductsAPI/"
data = getProductData(gendacPath)

@app.route("/", methods=['POST', 'GET'])
def index():
	"""
	Index home page of application which displays the full list of products as well as having the ability
	add new products
	"""
	global data
	data = getProductData(gendacPath)

	if request.method == 'POST':
		name = f"Product {request.form['Name']}"
		price = request.form['Price']
		category = request.form['Category']
		id = max([product["Id"] for product in data]) + 1

		newProduct = {"Id": id, "Name": name, "Category": category, "Price": price}
		addNewProduct(newProduct, gendacPath)
		
		return redirect("/")

	else:
		return render_template("index.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
	"""
	Simply deletes the selected product

	@param id: id of product
	"""
	deleteExistingProduct(id, gendacPath)

	return redirect('/')

@app.route("/Product/<int:id>")
def product(id):
	"""
	Simply shows all the details of the selected product

	@param id: id of product
	"""
	singleEntry = getProductData(f"{gendacPath}get?id={id}")

	return render_template("product.html", data=singleEntry)

@app.route("/Update/<int:id>", methods=['GET','POST'])
def update(id):
	"""
	Shows the details of the selected product with the ability
	to update the chosen products details

	@param id: id of product
	"""
	singleEntry = getProductData(f"{gendacPath}get?id={id}")

	if request.method == 'POST':
		name = f"Product {request.form['Name']}"
		price = request.form['Price']
		category = request.form['Category']
		id = id

		updatedProduct = {"Id": id, "Name": name, "Category": category, "Price": price}

		updateExistingProduct(id, gendacPath, updatedProduct)

		return redirect("/")
	
	else:

		return render_template("productUpdate.html", data=singleEntry)

if __name__ == "__main__":
	app.run(debug=True)
