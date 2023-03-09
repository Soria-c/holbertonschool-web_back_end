-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.
-- defining trigger
DELIMITER $$
DROP TRIGGER IF EXISTS reset_valid;
CREATE TRIGGER reset_valid
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN SET NEW.valid_email = 0;
END IF;
END $$
