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

@app.get("/transaction-codes/query{username}")
def get_nombre_transaction_codes(username: str) -> List[dict]:
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT tCode.*
        FROM transaction_code tCode
        INNER JOIN transaction tranc ON tCode.transaction_fk = tranc.id
        INNER JOIN transaction_status tStatus ON tranc.status_fk = tStatus.id
        INNER JOIN financial_product fProduct ON fProduct.id = tranc.destination_fk
        INNER JOIN users usr ON usr.id_number = fProduct.user_fk
        WHERE tStatus.name = 'COMPLETED'
        AND usr.name = %s
    """
    cursor.execute(query, (username,))
    transaction_codes = cursor.fetchall()
    cursor.close()
    return transaction_codes    

@app.get("/blocked-credit-cards")
def get_blocked_credit_cards() -> List[dict]:
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT usr.email, card.card_number
        FROM users usr 
        INNER JOIN financial_product fProduct ON usr.id_number = fProduct.user_fk
        INNER JOIN financial_product_type fpType ON fpType.id = fProduct.type_fk
        INNER JOIN banking_card card ON card.financial_product_fk = fProduct.id
        INNER JOIN financial_product_status fpStatus ON fpStatus.id_status = fProduct.status_fk
        WHERE fpType.name = 'Credit card'
        AND fpStatus.name = 'Blocked'
    """
    cursor.execute(query)

    blocked_credit_cards = cursor.fetchall()
    cursor.close()
    return blocked_credit_cards



@app.get("/query")#read usuario
def get_productos_luisa():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM productos_Luisa")
    result = cursor.fetchall()

 # convierte a utf8
    column_names = [i[0] for i in cursor.description]
    productos_Luisas = []
    for row in result:
        productos_Luisa = {}
        for idx, value in enumerate(row):
            if isinstance(value, bytes):
                productos_Luisa[column_names[idx]] = safe_decode(value)
            else:
                productos_Luisa[column_names[idx]] = value
        productos_Luisas.append(productos_Luisa)
    
    return {"productos_luisa": productos_Luisas}

@app.get("/financial-products/debit-no-card")
def get_debit_accounts_no_card() -> List[dict]:
    cursor = mydb.cursor(dictionary=True)
    query = """
    SELECT CONCAT(usr.name, ' ', usr.last_name) AS 'Full name', fProduct.*
    FROM financial_product fProduct
    INNER JOIN financial_product_type fpType ON fProduct.type_fk = fpType.id
    INNER JOIN users usr ON usr.id_number = fProduct.user_fk
    WHERE fpType.name = 'debit account'
    AND fProduct.has_card = 0;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results  

@app.get("/financial-products-overdue", response_model=List[Dict[str, str]])
def get_financial_products_overdue():
    cursor = mydb.cursor(dictionary=True)
    query = """
    SELECT usr.email, usr.phone_number, fpType.name
    FROM users usr 
    INNER JOIN financial_product fProduct ON usr.id_number = fProduct.user_fk
    INNER JOIN financial_product_type fpType ON fpType.id = fProduct.type_fk
    INNER JOIN financial_product_status fpStatus ON fpStatus.id_status = fProduct.status_fk
    WHERE fpType.name IN ('Credit card','Debit account')
    AND fProduct.amount < -100000;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

@app.get("/financial-product-status", response_model=List[Dict[str, str]])
def get_financial_product_status_empty_description():
    cursor = mydb.cursor(dictionary=True)
    query = """
    SELECT fpStatus.*
    FROM financial_product_status fpStatus
    WHERE fpStatus.Description = '';
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

@app.get("/full-name-count")
def get_full_name_count():
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT CONCAT(usr.name, ' ', usr.last_name) AS 'Full name', COUNT(fProduct.id) AS 'Count'
        FROM users usr
        INNER JOIN financial_product fProduct ON fProduct.user_fk = usr.id_number
        GROUP BY CONCAT(usr.name, ' ', usr.last_name)
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

@app.get("/financial-product-types")
def get_financial_product_types():
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT *
        FROM financial_product_type
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

@app.get("/failed-transactions")
def get_failed_transactions():
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT trans.id, trans.amount
        FROM transaction trans
        INNER JOIN transaction_status tStatus ON tStatus.id = trans.transaction_type_fk
        WHERE tStatus.name = 'Failed'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

@app.get("/users-with-email")
def get_users_with_email():
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT *
        FROM users
        WHERE email LIKE '%@%'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
