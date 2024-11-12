
import json

def test_create_product(test_client):
    response = test_client.post("/products", json={
        "name": "Test Product",
        "description": "A test product",
        "price": 10.99,
        "inventory_count": 100,
        "category": "Test Category"
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["name"] == "Test Product"
    assert data["inventory_count"] == 100

def test_get_products(test_client):
    response = test_client.get("/products")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) >= 1

def test_get_product_by_id(test_client):
    response = test_client.get("/products/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Test Product"

def test_update_product(test_client):
    response = test_client.put("/products/1", json={
        "name": "Updated Product",
        "description": "Updated description",
        "price": 12.99,
        "inventory_count": 150,
        "category": "Updated Category"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "Updated Product"
    assert data["inventory_count"] == 150

def test_delete_product(test_client):
    response = test_client.delete("/products/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "Product deleted"

def test_product_search(test_client):
    response = test_client.get("/products?name=Test")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert any("Test Product" in product["name"] for product in data)

def test_update_inventory(test_client):
    response = test_client.patch("/products/2/inventory", json={
        "inventory_count": 80
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["inventory_count"] == 80

def test_update_popularity(test_client):
    response = test_client.patch("/products/2/popularity", json={
        "popularity_score": 5.0
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["popularity_score"] == 5.0
