# HotelReservation_Django
By Imtiyaz Shaikh (A00456832)

## Steps:
1. One can clone the repository.
2. Create an environment and install the required libraries mentioned in the requirements.txt file

## API:
The hotel reservation app provides one get, one post api to getch and insert the hotel details in the database.
During implementation, developer has used the development MYSQL server, the connection is established using ssh tunnel.

## Complexity:
1. The model calculates the 'finalCost' and then inserts into the database. Formula: finalCost = price * noDaysBooked
2. The 'id' column in auto-incrmented in the MySQL table.
3. Exception handling is done for error 404 and 500.

**_Screencapture are provided in the 'screenshots' directory._**

## GET:
**1. To fetch the details of all the hotels**
http://127.0.0.1:8000/app/hotel_list/


**2. To fetch the details of specific hotel**
API CALL: http://127.0.0.1:8000/app/hotel_list/101

OUTPUT:
```json
{
    "name": "A4 Hotel",
    "price": 234,
    "city": "Pune",
    "starRating": 3,
    "amenities": "AC",
    "noDaysBooked": 0,
    "finalCost": 0
}
```
**3. Exception Handling: Returns the 404 status code when requested hotel does not exist**
API CALL: http://127.0.0.1:8000/app/hotel_list/94233

OUTPUT:
```json
{
    "detail": "hotel id - 94233 does not exist."
}
```

## POST
1.http://127.0.0.1:8000/app/hotel_list/

BODY: 
```json
{
    "name": "My Hotel",
    "price": 555,
    "city": "Mumbai",
    "starRating": 9,
    "amenities": "Non-AC",
    "noDaysBooked": 2
}
```
