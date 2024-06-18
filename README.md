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
**HTTP Method**: GET <br>
**Description**: Retrieve a list of all inventory items available in the system.<br>
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
**HTTP Method**: POST <br>
**Description**: This creates a new inventory item. <br>
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
/api/inventory/{id}/
```
**HTTP Method**: GET <br>
**Description**: Retrieve a specific inventory item. <br>
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
/api/inventory/{id}/
```
**HTTP Method**: PATCH <br>
**Description**:  This updates a specific inventory item. <br>
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
/api/inventory/{id}/
```
**HTTP Method**: DEL <br>
**Description**:  This deletes a specific inventory item. <br>
**Response**: the API will respond with a sucess message. An example response will have the following schema:
```
"detail": "Inventory item has been deleted successfully."
```
### List all suppliers
**Endpoint**: 
```
/api/suppliers/
```
**HTTP Method**: GET <br>
**Description**: Retrieve a list of all suppliers available in the system. <br>
**Response**: JSON array of suppliers objects with their details, including id, name and contact info. An example is as shown:

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
**HTTP Method**: POST <br>
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
**HTTP Method**: GET <br>
**Description**: This retrieves a specific Supplier. <br>
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
**HTTP Method**: PATCH <br>
**Description**:  This updates a specific supplier. <br>
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
**HTTP Method**: DEL <br>
**Description**:  This deletes a supplier. <br>
**Response**: the API will respond with a success message. An example response will have the following schema:
```
"detail": "Supplier has been deleted successfully."
```
### List all suppliers associated with an Inventory Item
**Endpoint**: 
```
/api/inventory/<int:item_id>/suppliers/
```
**HTTP Method**: GET <br>
**Description**: Retrieve a list of all suppliers available associated with a particular item whose item id is specified in the URL. <br>
**Response**: JSON array of supplier objects with their details, including id, name and contact info. An example is as shown:

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

### List all Inventory items provided by a supplier
**Endpoint**: 
```
/api/suppliers/<int:supplier_id>/items/
```
**HTTP Method**: GET <br>
**Description**: Retrieve a list of all inventory items provided  by a supplier whose item id is specified in the URL. <br>
**Response**: JSON array of inventory objects with their details. An example is as shown:

```
[
    {
        "id": 3,
        "suppliers": [
            1
        ],
        "name": "Nanny",
        "description": "This is a woman for infants.",
        "price": "40000.00",
        "date_added": "2024-06-17"
    },
    {
        "id": 4,
        "suppliers": [
            1,
            3
        ],
        "name": "Nanny",
        "description": "This is a woman for infants.",
        "price": "40000.00",
        "date_added": "2024-06-17"
    }
]
```
### Error Handling

The API may return error messages with appropriate HTTP status codes in case of invalid requests or data issues. Here are some common examples:

* **400 Bad Request:** This indicates a malformed request, such as missing required fields or invalid data formats.
* **404 Not Found:** This occurs when trying to access a resource (inventory item or supplier) that doesn't exist.
* **500 Internal Server Error:** This is a generic error for unexpected server-side issues.

The specific error message will provide more details about the problem encountered.
### Known Limitations

This API does not include authentication or authorization mechanisms. It assumes open access.

### Conclusion

