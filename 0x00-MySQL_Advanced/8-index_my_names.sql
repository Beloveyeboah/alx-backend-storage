-- Step 1: Add the generated column to store the first letter of name
ALTER TABLE names ADD COLUMN name_first_char CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

-- Step 2: Create an index on the generated column
CREATE INDEX idx_name_first ON names (name_first_char);
