from fastapi import FastAPI,Depends, HTTPException
from datetime import datetime
"""from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from models.modelos import User,UserResponse,financial_product_status,financial_product_type,transaction_status,transaction_type,financial_product,banking_card,transaction,transaction_code"""
import mysql.connector
import base64
from typing import List

#inicio de la aplicación
app = FastAPI(title="BankUD", description="this is the BankUD DB API")

#conección a db
mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="mysql",
        database="Bank_UD"
)

#función para utf8
def safe_decode(data):
    """Attempt to decode data as UTF-8, if it fails, return base64 encoded string."""
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return base64.b64encode(data).decode('utf-8')

@app.get("/")
def healthcheck():
    """This is a service to validate web API is up and running."""
    return {"status": "ok"}

#request users

@app.get("/user")#read usuario
def get_usuario():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    users = []
    for row in result:
        user = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                user[column_names[idx]] = safe_decode(value)
            else:
                user[column_names[idx]] = value
        users.append(user)
    
    return {"usuarios": users}

@app.post("/user")#create usuario    
def add_usuario(name: str,last_name:str,pasword: str,phone_number:str,email:str):
    cursor = mydb.cursor()
    sql = "INSERT INTO users (name,last_name,pasword,phone_number,email) VALUES (%s, %s, %s,%s, %s)"
    val = (name,last_name,pasword,phone_number,email)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "usuario añadido"}

# update contraseña de usuario con el  email
@app.put("/user/{email}")
def update_usuario_password(email: str, pasword: str):
    cursor = mydb.cursor()
    cursor.execute("UPDATE users SET pasword = %s WHERE email = %s", (pasword, email))
    mydb.commit()
    return {"message": "Password updated successfully"}

# Delete un usuario con el email
@app.delete("/employees/{email}")
def delete_usuario(email: str):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM users WHERE email = {email}")
    mydb.commit()
    return {"mensaje": "usuario eliminado"}

#request financial_product_status

@app.get("/financial_product_status")#read  financial_product_status
def get_financial_product_status():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM financial_product_status")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    financial_product_statuss = []
    for row in result:
        financial_product_status = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                financial_product_status[column_names[idx]] = safe_decode(value)
            else:
                financial_product_status[column_names[idx]] = value
        financial_product_statuss.append(financial_product_status)
    
    return {"financial_product_status": financial_product_statuss}

@app.post("/financial_product_status")#create usuario    
def add_financial_product_status(name: str,description :str):
    cursor = mydb.cursor()
    sql = "INSERT INTO financial_product_status (name,description) VALUES (%s, %s)"
    val = (name,description)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "add_financial_product_status añadido"}

# Delete un financial_product_status con el nombre
@app.delete("/financial_product_status/{nombre}")
def delete_financial_product_status(nombre: str):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM financial_product_status WHERE nombre = {nombre}")
    mydb.commit()
    return {"mensaje": "financial_product_status eliminado"}

# request financial_product_type

@app.get("/financial_product_type")#read  financial_product_type
def get_financial_product_type():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM financial_product_type")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    financial_product_types = []
    for row in result:
        financial_product_type = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                financial_product_type[column_names[idx]] = safe_decode(value)
            else:
                financial_product_type[column_names[idx]] = value
        financial_product_types.append(financial_product_type)
    
    return {"financial_product_status": financial_product_types}

@app.post("/financial_product_type")#create financial_product_type    
def add_financial_product_type(name: str,description :str):
    cursor = mydb.cursor()
    sql = "INSERT INTO financial_product_type (name,description) VALUES (%s, %s)"
    val = (name,description)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "add_financial_product_type añadido"}

# Delete un financial_product_type con el nombre
@app.delete("/financial_product_type/{nombre}")
def delete_financial_product_type(nombre: str):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM financial_product_type WHERE nombre = {nombre}")
    mydb.commit()
    return {"mensaje": "financial_product_type eliminado"}

# request transaction_status

@app.get("/transaction_status")#read  transaction_status
def get_transaction_status():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM transaction_status")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    transaction_statuss = []
    for row in result:
        transaction_status = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                transaction_status[column_names[idx]] = safe_decode(value)
            else:
                transaction_status[column_names[idx]] = value
        transaction_statuss.append(transaction_status)
    
    return {"transaction_status": transaction_statuss}

@app.post("/transaction_status")#create transaction_status    
def add_transaction_status(name: str,description :str):
    cursor = mydb.cursor()
    sql = "INSERT INTO transaction_status (name,description) VALUES (%s, %s)"
    val = (name,description)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "transaction_status añadido"}

# Delete un transaction_status con el nombre
@app.delete("/transaction_status/{nombre}")
def delete_transaction_status(nombre: str):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM transaction_status WHERE nombre = {nombre}")
    mydb.commit()
    return {"mensaje": "transaction_status eliminado"}

#request transaction_type

@app.get("/transaction_type")#read  transaction_type
def get_transaction_type():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM transaction_type")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    transaction_types = []
    for row in result:
        transaction_type = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                transaction_type[column_names[idx]] = safe_decode(value)
            else:
                transaction_type[column_names[idx]] = value
        transaction_types.append(transaction_type)
    
    return {"transaction_types": transaction_types}

@app.post("/transaction_type")#create transaction_type    
def add_transaction_type(name: str,description :str):
    cursor = mydb.cursor()
    sql = "INSERT INTO transaction_type (name,description) VALUES (%s, %s)"
    val = (name,description)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "transaction_type añadido"}

# Delete un transaction_type con el nombre
@app.delete("/transaction_type/{nombre}")
def transaction_type(nombre: str):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM transaction_type WHERE nombre = {nombre}")
    mydb.commit()
    return {"mensaje": "transaction_type eliminado"}

# request financial_product

@app.get("/financial_product")#read financial_product
def get_financial_product():

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM financial_product")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    financial_products = []
    for row in result:
        financial_product = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                financial_product[column_names[idx]] = safe_decode(value)
            else:
                financial_product[column_names[idx]] = value
        financial_products.append(financial_product)
    
    return {"transaction_types": financial_products}  

@app.post("/financial_product")#create financial_product  terminarrr   
def add_financial_product(user_fk: str,type_fk :str,status_fk:str,date: datetime,
    amount: float,has_card: int):
    cursor = mydb.cursor()
    sql = "INSERT INTO financial_product (user_fk,type_fk ,status_fk,date,amount,has_card) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (user_fk,type_fk ,status_fk,date,amount,has_card)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "financial_product añadido"}

# Delete un financial_product con el id
@app.delete("/financial_product/{id}")
def delete_financial_product(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM financial_product WHERE id = {id}")
    mydb.commit()
    return {"mensaje": "financial_product eliminado"}


# request banking_card

@app.get("/banking_card")#read banking_card
def get_banking_card():

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM banking_card")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    banking_cards = []
    for row in result:
        banking_card = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                banking_card[column_names[idx]] = safe_decode(value)
            else:
                banking_card[column_names[idx]] = value
        banking_cards.append(banking_card)
    
    return {"banking_cards": banking_cards}  

@app.post("/banking_card")#create banking_card     
def add_banking_card(card_number: str,
    financial_product_fk: str,
    password: str,
    creation_date: datetime,
    expiry_date: datetime ):
    cursor = mydb.cursor()
    sql = "INSERT INTO banking_card (card_number,financial_product_fk,password, creation_date,  expiry_date ) VALUES (%s, %s,%s, %s,%s)"
    val = (card_number,financial_product_fk,password, creation_date,  expiry_date)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "banking_card añadido"}

# Delete un banking_card con el id
@app.delete("/banking_card/{id}")
def delete_banking_card(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM banking_card WHERE id = {id}")
    mydb.commit()
    return {"mensaje": "banking_card eliminado"}

# request movement_history

@app.get("/movement_history")#read movement_history
def get_movement_history():

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM movement_history")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    movement_historys = []
    for row in result:
        movement_history = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                movement_history[column_names[idx]] = safe_decode(value)
            else:
                movement_history[column_names[idx]] = value
        movement_historys.append(movement_history)
    
    return {"movement_historys": movement_historys}  

@app.post("/movement_history")#create movement_history     
def add_movement_history(
    name: str,
    description:str,
    date: datetime,
    amount: float,
    financial_product_fk: str,
     ):
    cursor = mydb.cursor()
    sql = "INSERT INTO movement_history ( name,description,date,amount,financial_product_fk) VALUES (%s, %s,%s, %s,%s)"
    val = (name,description,date,amount,financial_product_fk)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "movement_history añadido"}

# Delete un banking_card con el id
@app.delete("/movement_history/{id}")
def delete_movement_history(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM movement_history WHERE id = {id}")
    mydb.commit()
    return {"mensaje": "movement_history eliminado"}

# request transaction

@app.get("/transaction")#read transaction
def get_transaction():

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM transaction")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    transactions = []
    for row in result:
        transaction = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                transaction[column_names[idx]] = safe_decode(value)
            else:
                transaction[column_names[idx]] = value
        transactions.append(transaction)
    
    return {"transaction_types": transactions}  

@app.post("/transaction")#create transaction     
def add_transaction(
    transaction_type_fk: str, date: datetime,status_fk: str,
    amount: float, origin_fk: str,destination_fk: str   ):
    cursor = mydb.cursor()
    sql = "INSERT INTO transaction ( transaction_type_fk, date , status_fk , amount, origin_fk,destination_fk) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (transaction_type_fk, date,status_fk,amount, origin_fk,destination_fk)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "transaction añadido"}

# Delete un banking_card con el id
@app.delete("/transaction/{id}")
def delete_transaction(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM transaction WHERE id = {id}")
    mydb.commit()
    return {"mensaje": "transaction eliminado"}

# request transaction_code

@app.get("/transaction_code")#read transaction_code
def get_transaction_code():

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM transaction_code")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    transaction_codes = []
    for row in result:
        transaction_code = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                transaction_code[column_names[idx]] = safe_decode(value)
            else:
                transaction_code[column_names[idx]] = value
        transaction_codes.append(transaction_code)
    
    return {"transaction_codes": transaction_codes}  

@app.post("/transaction_code")#create transaction_code     
def add_transaction_code(
    transaction_fk: str, creation_date: datetime,
      expiry_date: datetime,status: int     ):
    cursor = mydb.cursor()
    sql = "INSERT INTO transaction_code ( transaction_fk, creation_date, expiry_date,status) VALUES (%s, %s,%s, %s)"
    val = (transaction_fk, creation_date, expiry_date,status)
    cursor.execute(sql, val)
    mydb.commit()
    return {"mensaje": "transaction_code añadido"}

# Delete un transaction_code con el id
@app.delete("/transaction_code/{id}")
def delete_transaction_code(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM transaction_code WHERE id = {id}")
    mydb.commit()
    return {"mensaje": "transaction_code eliminado"}

