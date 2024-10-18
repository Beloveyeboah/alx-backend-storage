-- Add the generated column
ALTER TABLE names ADD COLUMN name_first_char CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

-- Create the index on the generated column and the score column
CREATE INDEX idx_name_first_score ON names (name_first_char, score);
