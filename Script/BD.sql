CREATE SCHEMA Bank_Ud;
use Bank_Ud;
/*Tables*/
CREATE TABLE IF NOT EXISTS users(
	id_number binary(16) DEFAULT (UUID_TO_BIN(UUID())),
	name varchar(70) NOT NULL,
    last_name VARCHAR(70) NOT NULL,  
    pasword VARCHAR(8) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(40) UNIQUE NOT NULL    
);
ALTER TABLE users ADD primary key(id_number);
CREATE INDEX Index_user ON users(id_number);

CREATE TABLE IF NOT EXISTS financial_product_status(
	id_status INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(200)
);
CREATE INDEX Index_fp_status ON financial_product_status(id_status);

CREATE TABLE IF NOT EXISTS financial_product_type(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(200)
);
CREATE INDEX Index_fp_type ON financial_product_type(id);

CREATE TABLE IF NOT EXISTS transaction_status(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(200)
);
CREATE INDEX Index_trans_status ON transaction_status(id);

CREATE TABLE IF NOT EXISTS transaction_type(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(200)
);
CREATE INDEX Index_trans_type ON transaction_type(id);

CREATE TABLE IF NOT EXISTS financial_product(
	id INT AUTO_INCREMENT PRIMARY KEY,
    user_fk BINARY(16),
    type_fk INT,
    status_fk INT,
    date DATETIME,
    amount DECIMAL (12, 2) NOT NULL,
    has_card TINYINT(0) NOT NULL,     
    FOREIGN KEY (user_fk) REFERENCES users(id_number),
    FOREIGN KEY (type_fk) REFERENCES financial_product_type(id),
    FOREIGN KEY (status_fk) REFERENCES financial_product_status(id_status)    
);
CREATE INDEX Index_financial_product ON financial_product(id);

CREATE TABLE IF NOT EXISTS banking_card(
	id INT AUTO_INCREMENT PRIMARY KEY,
    card_number INT UNIQUE,
    financial_product_fk INT,
    password VARCHAR(50) NOT NULL,
    creation_date datetime NOT NULL,
    expiry_date datetime NOT NULL,
    FOREIGN KEY (financial_product_fk) REFERENCES financial_product(id)
);
ALTER TABLE banking_card MODIFY card_number VARCHAR(20);
CREATE INDEX Index_banking_card ON banking_card(id);

CREATE TABLE IF NOT EXISTS movement_history(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    description VARCHAR(120),
    date datetime,
	amount DECIMAL(12, 2) NOT NULL,
    financial_product_fk INT,
    FOREIGN KEY (financial_product_fk) REFERENCES financial_product(id)
);
CREATE INDEX Index_history ON movement_history(id);

CREATE TABLE IF NOT EXISTS transaction(
	id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type_fk INT,
    date datetime,
    status_fk INT,
    amount DECIMAL(12, 2) NOT NULL,
    origin_fk INT,
    destination_fk INT,
	FOREIGN KEY (transaction_type_fk) REFERENCES transaction_type(id),
	FOREIGN KEY (status_fk) REFERENCES transaction_status(id),
	FOREIGN KEY (origin_fk) REFERENCES financial_product(id),
	FOREIGN KEY (destination_fk) REFERENCES financial_product(id)
);
CREATE INDEX Index_transaction ON transaction(id);

CREATE TABLE IF NOT EXISTS transaction_code(
	id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_fk INT,
    creatrion_date datetime NOT NULL,
    expiry_date datetime NOT NULL,
    status TINYINT(1) NOT NULL,
    FOREIGN KEY (transaction_fk) REFERENCES transaction(id)    
);
CREATE INDEX Index_trans_code ON transaction_code(id);

/*Data insertion*/


INSERT INTO users (id_number, name, last_name, pasword, phone_number, email) VALUES
(UUID_TO_BIN(UUID()), 'Juan', 'Pérez', 'abc12345', '3001234567', 'juan.perez@gmail.com'),
(UUID_TO_BIN(UUID()), 'María', 'Gómez', 'def67890', '3002345678', 'maria.gomez@gmail.com'),
(UUID_TO_BIN(UUID()), 'Carlos', 'Rodríguez', 'ghi12345', '3003456789', 'carlos.rodriguez@gmail.com'),
(UUID_TO_BIN(UUID()), 'Ana', 'Martínez', 'jkl67890', '3004567890', 'ana.martinez@gmail.com'),
(UUID_TO_BIN(UUID()), 'Luisa', 'Fernández', 'mno12345', '3005678901', 'luisa.fernandez@gmail.com'),
(UUID_TO_BIN(UUID()), 'Pedro', 'Ramírez', 'pwd12345', '3006789012', 'pedro.ramirez@gmail.com');

INSERT INTO financial_product_status (name, description) VALUES
('Active', 'Financial product active'),
('Inactive', 'Financial product inactive'),
('Pending', 'Financial product pending for activation'),
('Blocked', '');

INSERT INTO financial_product_type (name, description) VALUES
('Savings account', 'Standart savings account'),
('Debit account', 'Standart debit account'),
('Credit card', 'Banking credit card');

INSERT INTO transaction_status (name, description) VALUES
('Completed', 'Transaction completed succesfully'),
('Pending', 'Transantion pending for approval'),
('Failed', 'Transaction failed');

INSERT INTO transaction_type (name, description) VALUES
('Transfer', 'Transfer of money between accounts'),
('Payment', 'Payment for a product or service'),
('Deposit', 'Deposit of money into an account');

INSERT INTO financial_product (user_fk, type_fk, status_fk, date, amount, has_card) VALUES
((SELECT id_number FROM users WHERE email = 'juan.perez@gmail.com'), 1, 1, NOW(), 1500000, 1),
((SELECT id_number FROM users WHERE email = 'maria.gomez@gmail.com'), 2, 1, NOW(), 3000000, 0),
((SELECT id_number FROM users WHERE email = 'carlos.rodriguez@gmail.com'), 3, 1, NOW(), 500000, 1),
((SELECT id_number FROM users WHERE email = 'ana.martinez@gmail.com'), 1, 1, NOW(), 2000000, 1),
((SELECT id_number FROM users WHERE email = 'luisa.fernandez@gmail.com'), 2, 2, NOW(), 1000000, 0);

INSERT INTO financial_product (user_fk, type_fk, status_fk, date, amount, has_card) VALUES
((SELECT id_number FROM users WHERE email = 'pedro.ramirez@gmail.com'), 3, 2, NOW(), 13000000, 1);

INSERT INTO banking_card (card_number, financial_product_fk, password, creation_date, expiry_date) VALUES
(1234567890123456, 1, '1234', NOW(), DATE_ADD(NOW(), INTERVAL 4 YEAR)),
(2345678901234567, 3, '5678', NOW(), DATE_ADD(NOW(), INTERVAL 4 YEAR)),
(3456789012345678, 4, '9101', NOW(), DATE_ADD(NOW(), INTERVAL 4 YEAR));

INSERT INTO movement_history (name, description, date, amount, financial_product_fk) VALUES
('Deposit', 'Deposit in a savings account', NOW(), 500000, 1),
('Withdrawal', 'Withdrawal from ATM', NOW(), -200000, 1),
('Transfer', 'Transfer to a different account', NOW(), 1000000, 2),
('Payment', 'Public services payment', NOW(), -150000, 3),
('Purchase', 'Purchase in store', NOW(), -300000, 4);

INSERT INTO transaction (transaction_type_fk, date, status_fk, amount, origin_fk, destination_fk) VALUES
(1, NOW(), 1, 500000, 1, 2),
(2, NOW(), 1, 300000, 2, 3),
(3, NOW(), 1, 200000, 3, 4),
(1, NOW(), 2, 150000, 4, 5),
(2, NOW(), 3, 100000, 5, 1);

INSERT INTO transaction_code (transaction_fk, creatrion_date, expiry_date, status) VALUES
(1, NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 1),
(2, NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 1),
(3, NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 1),
(4, NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 0),
(5, NOW(), DATE_ADD(NOW(), INTERVAL 1 DAY), 0);

/*Selects*/

SELECT tCode.*
FROM transaction_code tCode
INNER JOIN transaction tranc ON tCode.transaction_fk = tranc.id
INNER JOIN transaction_status tStatus ON tranc.status_fk = tStatus.id
INNER JOIN financial_product fProduct ON fProduct.id = tranc.destination_fk
INNER JOIN users usr ON usr.id_number = fProduct.user_fk
WHERE tStatus.name = 'COMPLETED'
AND usr.name = 'Carlos';

SELECT CONCAT(usr.name,' ', usr.last_name) AS 'Full name', fProduct.*
FROM financial_product fProduct
INNER JOIN financial_product_type fpType ON fProduct.type_fk = fpType.id
INNER JOIN users usr ON usr.id_number = fProduct.user_fk
WHERE fpType.name = 'debit account'
AND fProduct.has_card = 0;

SELECT usr.email, card.card_number
FROM users usr 
INNER JOIN financial_product fProduct ON usr.id_number = fProduct.user_fk
INNER JOIN financial_product_type fpType ON fpType.id = fProduct.type_fk
INNER JOIN banking_card card ON card.financial_product_fk = fProduct.id
INNER JOIN financial_product_status fpStatus ON fpStatus.id_status = fProduct.status_fk
WHERE fpType.name = 'Credit card'
AND fpStatus.name = 'Blocked';

SELECT usr.email, usr.phone_number, fpType.name
FROM users usr 
INNER JOIN financial_product fProduct ON usr.id_number = fProduct.user_fk
INNER JOIN financial_product_type fpType ON fpType.id = fProduct.type_fk
INNER JOIN financial_product_status fpStatus ON fpStatus.id_status = fProduct.status_fk
WHERE fpType.name IN  ('Credit card','Debit account')
AND fProduct.amount < -100000;

SELECT fpStatus.*
FROM financial_product_status fpStatus
WHERE fpStatus.Description = '';

SELECT CONCAT(usr.name,' ', usr.last_name) AS 'Full name', COUNT(fProduct.id)
FROM users usr
INNER JOIN financial_product fProduct ON fProduct.user_fk = usr.id_number
GROUP BY CONCAT(usr.name,' ', usr.last_name);

SELECT fpType.*
FROM financial_product_type fpType;

SELECT trans.id, trans.amount
FROM transaction trans
INNER JOIN transaction_status tStatus ON tStatus.id = trans.transaction_type_fk
WHERE tStatus.name = 'Failed';

SELECT usr.*
FROM users usr
WHERE usr.email LIKE '%@%';

SELECT BIN_TO_UUID(id_number) From users;

/*View*/

CREATE VIEW productos_Luisa AS
SELECT fProduct.id, fpType.name AS 'Type name', mHistory.name AS 'History name', mHistory.date
FROM financial_product fProduct 
INNER JOIN users usr ON usr.id_number = fProduct.user_fk
INNER JOIN financial_product_type fpType ON fpType.id = fProduct.status_fk
INNER JOIN movement_history mHistory ON mHistory.financial_product_fk
WHERE usr.name = 'Luisa'
GROUP BY fProduct.id, fpType.name, mHistory.name, mHistory.date;

SELECT * FROM productos_Luisa;

/*Trigger*/

CREATE TRIGGER insert_card
AFTER INSERT ON banking_card
FOR EACH ROW
UPDATE financial_product SET financial_product.has_card = 1 WHERE financial_product.id = NEW.financial_product_fk;

/*Procedure*/
DELIMITER //
CREATE PROCEDURE no_card()
BEGIN
	SELECT CONCAT(usr.name,' ', usr.last_name) AS 'Full name', fProduct.*
	FROM financial_product fProduct
	INNER JOIN financial_product_type fpType ON fProduct.type_fk = fpType.id
	INNER JOIN users usr ON usr.id_number = fProduct.user_fk
	WHERE fpType.name = 'debit account'
	AND fProduct.has_card = 0;
END //

DELIMITER ;

CALL no_card();
