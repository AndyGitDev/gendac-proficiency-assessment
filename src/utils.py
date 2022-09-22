import requests

def getProductData(apiPath):
	try:
		apiResponse = requests.get(apiPath)
		data = apiResponse.json()

		return data

	except requests.exceptions.RequestException as e:
		raise SystemExit(e)

def addNewProduct(product, apiPath):
	try:
		apiResponse = requests.post(apiPath, json=product)

		return apiResponse

	except requests.exceptions.RequestException as e:
		raise SystemExit(e)

def deleteExistingProduct(id, apiPath):
	try:
		apiResponse = requests.delete(f"{apiPath}get?id={id}")

		return apiResponse

	except requests.exceptions.RequestException as e:
		raise SystemExit(e)

def updateExistingProduct(id, apiPath, updatedProduct):
	try:
		apiResponse = requests.put(f"{apiPath}get?id={id}", updatedProduct)

		return apiResponse

	except requests.exceptions.RequestException as e:
		raise SystemExit(e)

if __name__ == "__main__":
	pass