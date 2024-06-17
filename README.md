# Online Store Inventory and Supplier Management API

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```
## API Endpoints

### List all inventory items
**Endpoint**:
```
/api/inventory/
```
**HTTP Method**: GET
**Description**: Retrieve a list of all inventory items available in the system.
**Response**: JSON array of inventory objects with their details, including id, name, description, price, date added and suppliers. An example is as shown:

```
[
    {
        "id": 1,
        "suppliers": [
            1,
            2
        ],
        "name": "Nan one",
        "description": "This is a milk for a day old infants.",
        "price": "4000.00",
        "date_added": "2024-06-17"
    },
    {
        "id": 2,
        "suppliers": [1],
        "name": "Nan two",
        "description": "This is a milk for two day old infants.",
        "price": "4000.00",
        "date_added": "2024-06-17"
    },
  
]
```

### Create a new inventory item
**Endpoint**: 
```
/api/inventory/
```
**HTTP Method**: POST
**Description**: This creates a new inventory item.
**Request**: Example request body includes;
```
{
    "name": "Nanny ",
    "description": "This is a woman for infants.",
    "price": 40000.00,
    "suppliers": [1, 3]
}
```
**Response**: Upon successful creation of the inventory item, the API will respond with a status code of 201 and a JSON object representing the newly created inventory item. An example response will have the following schema:
```
{
    "id": 1,
    "suppliers": [
        1,
        3
    ],
    "name": "Nan One",
    "description": "This is a milk for children",
    "price": "40000.00",
    "date_added": "2024-06-17"
}
```
### Get An Inventory Item
**Endpoint**: 
```
/api/inventory/id/
```
**HTTP Method**: GET
**Description**: Retrieve a specific inventory item
**Response**: The response returned is a JSON object with an example schema as follows:
```
{
    "id": 1,
    "suppliers": [
        1,
        2
    ],
    "name": "Nan one",
    "description": "This is a milk for a day old infants.",
    "price": "4000.00",
    "date_added": "2024-06-17"
}
```
### Edit an inventory item
**Endpoint**: 
```
/api/inventory/1/
```
**HTTP Method**: PATCH
**Description**:  This updates a specific inventory item
**Request**: Example request body includes;
```
{
    "description": "This is a milk for children.",
}
```
**Response**: the API will respond with a status code of 200 and a JSON object representing the updated inventory item. An example response will have the following schema:
```
{
    "id": 1,
    "suppliers": [
        1,
        3
    ],
    "name": "Nan One",
    "description": "This is a milk for children",
    "price": "40000.00",
    "date_added": "2024-06-17"
}
```
### Delete an inventory item
**Endpoint**: 
```
/api/inventory/1/
```
**HTTP Method**: DEL
**Description**:  This deletes a specific inventory item
**Response**: the API will respond with a sucess message. An example response will have the following schema:
```
"detail": "Inventory item has been deleted successfully."
```
### List all suppliers
**Endpoint**: 
```
/api/suppliers/
```
**HTTP Method**: GET
**Description**: Retrieve a list of all suppliers available in the system.
**Response**: JSON array of inventory objects with their details, including id, name and contact info. An example is as shown:

```
[
    {
        "id": 1,
        "name": "Divine Pascal",
        "contact_info": "08147250442"
    },
    {
        "id": 2,
        "name": "Chukwu ekene",
        "contact_info": "08059771695"
    }
]
```

### Create a new supplier
**Endpoint**: 
```
/api/suppliers/
```
**HTTP Method**: POST
**Description**: This creates a new supplier.
**Request**: Example request body includes;
```
{
  "name": "Chukwu ekene",
  "contact_info": "08059771695"
}
```
**Response**: Upon successful creation of the supplier, the API will respond with a status code of 201 and a JSON object representing the newly created inventory item. An example response will have the following schema:
```
{
    "id": 2,
    "name": "Chukwu ekene",
    "contact_info": "08059771695"
}
```
### Get A Specific Supplier
**Endpoint**: 
```
/api/suppliers/{id}/
```
**HTTP Method**: GET
**Description**: This retrieves a specific Supplier
**Response**: The response returned is a JSON object with an example schema as follows:
```
{
    "id": 2,
    "name": "Chukwu ekene",
    "contact_info": "08059771695"
}
```
### Edit an supplier
**Endpoint**: 
```
/api/suppliers/{id}/
```
**HTTP Method**: PATCH
**Description**:  This updates a specific supplier
**Request**: Example request body includes;
```
{
  "name": "Chukwudi Emeka",
  "contact_info": "08059771695"
}
```
**Response**: the API will respond with a status code of 200 and a JSON object representing the updated inventory item. An example response will have the following schema:
```
{
    "id": 2,
    "name": "Chukwudi Emeka",
    "contact_info": "08059771695"
}
}
```
### Delete a specific Supplier
**Endpoint**: 
```
/api/suppliers/{id}/
```
**HTTP Method**: DEL
**Description**:  This deletes a supplier
**Response**: the API will respond with a success message. An example response will have the following schema:
```
"detail": "Supplier has been deleted successfully."
```
### Known Limitations

This API does not include authentication or authorization mechanisms. It assumes open access.

### Conclusion

