'''linear_search_product'''

def LinearSearchProduct(productlist,targetProduct):
  indices = []

  for index, product in enumerate(productlist):
    if product == targetProduct:
      indices.append(index)

  return indices

#Example usage:
products = [" shoes","boot","Loafer","shoes","sandle","shoes"]
target = "shoes"  
target2 = 'apple'
result = LinearSearchProduct(products,target)
print(result)