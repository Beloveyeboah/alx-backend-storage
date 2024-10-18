-- task 13
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Declare a cursor to iterate through all users
    DECLARE user_cursor CURSOR FOR 
    SELECT id FROM users;

    -- Declare a handler for when the cursor is done
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the weighted sum of scores for the current user
        SELECT COALESCE(SUM(score * weight), 0) INTO weighted_sum
        FROM scores
        WHERE scores.user_id = user_id;

        -- Calculate the total weight for the current user
        SELECT COALESCE(SUM(weight), 1) INTO total_weight
        FROM scores
        WHERE scores.user_id = user_id;

        -- Calculate the average weighted score for the current user
        SET avg_weighted_score = weighted_sum / total_weight;

        -- Store the average weighted score in the users table
        UPDATE users
        SET average_weighted_score = avg_weighted_score
        WHERE id = user_id;

    END LOOP user_loop;

    -- Close the cursor
    CLOSE user_cursor;
END;
//

DELIMITER ;

