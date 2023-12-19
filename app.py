from mongo import Mongo
import time
import random

brands=["A Brand","B Brand","C Brand","D Brand","E Brand"]

color=["Red","Blue","Black","White","Orange","Green","Gray"]
categories=[]
subcategories=[]
products=[]
colors=[]
pAdd=[1,9,2,8,3,7,4,6,5,5]


def main():
    addAll()
    relate()
    
db = Mongo("dxdx")
def addCollection(content):
    val = db.insertCollection(content)
    if val != None:
       print(content["collectionName"]+"---"+val)
       content["_id"]=val
       return content
    else:
        return None
    
def addCategory():
    for i in range(0, 5): 
        data={
            "collectionName":"category",
            "content":{
                "createdDate": round(time.time()*1000) ,
                "categoryName":"category"+str(i)
            }
        }
        categories.append(addCollection(data))
def addSubCategory():
    for i in range(0, 10): 
        data={
            "collectionName":"subCategory",
            "content":{
                "createdDate": round(time.time()*1000) ,
                "subCategoryName":"subCategory"+str(i)
            }
        }
        subcategories.append(addCollection(data))
def addProduct():
    for i in range(0, 50): 
        data={
            "collectionName":"product",
            "content": {
                "createdDate":round(time.time()*1000) ,
                "productName": "Product "+str(i),
                "productBrand": brands[random.randint(0,len(brands)-1)],
                "productPrice": str(random.randint(0,200)),
                "productCurrency":"$",
                "productSaleCount":0,
                "isActive": True
            }
        }
        products.append(addCollection(data))
def addColor():
    for i in range(0,len(color)): 
        data={
            "collectionName":"color",
            "content": {
                "createdDate": round(time.time()*1000) ,
                "colorName": color[i],
                "isActive": True
            }
        }
        colors.append(addCollection(data))
def addAll():
    addCategory()
    addSubCategory()
    addProduct()
    addColor()

def relate():
    sub=0
    
    for i in range(0,len(categories)):
        data={}
        data["collectionId"]=str(categories[i]["_id"])
        data["relationName"]="categoryRelations"
        data["collectionName"]=categories[i]["collectionName"]
        data["content"]=categories[i]["content"]
        data["related"]={
            "subCategory":[]
        }
        s=0
        for c in range(sub,sub+2):
            data["related"]["subCategory"].append(subcategories[c])
            pList=random.sample(products,pAdd[0])
            data["related"]["subCategory"][s]["related"]={
                "product":pList
            }
            for d in range(0,len(data["related"]["subCategory"][s]["related"]["product"])):
                data["related"]["subCategory"][s]["related"]["product"][d]["related"]={"color":random.sample(colors,2)}
            pAdd.pop(0)
            removeProducts(pList)

            s+=1
        sub+=2
        print(sub)
        db.insertRelation(data)
def removeProducts(pList):
    for i in range(len(products))[::-1]:
        if(products[i] in pList):
            del products[i]
    return True
main()
