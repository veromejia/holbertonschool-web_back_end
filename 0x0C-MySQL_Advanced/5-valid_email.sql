-- Creates a trigger that resets the attribute valid_email only when the email has been changed.
-- Decrease the quantity of an item when a new order is inserted
DELIMITER $ $ 
CREATE TRIGGER resets BEFORE
UPDATE
    ON users FOR EACH ROW BEGIN IF NEW.email <> OLD.email THEN
SET
    NEW.valid_email = 0;

END IF;

END;

$ $