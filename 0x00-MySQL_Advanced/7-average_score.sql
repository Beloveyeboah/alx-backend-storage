-- rite a SQL script that creates a stored procedure ComputeAverageScoreForUs
DELIMITER //

-- Step 1: Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    -- Step 2: Declare a variable to hold the average score
    DECLARE average_score DECIMAL(5, 2);

    -- Step 3: Calculate the average score for the user
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE user_id = user_id;

    -- Step 4: Store the average score in the users table
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END;
//

-- Step 5: Reset the delimiter
DELIMITER ;
