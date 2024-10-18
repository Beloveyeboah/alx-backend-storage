-- task 12
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Calculate the weighted sum of scores for the user
    SELECT SUM(score * weight) INTO weighted_sum
    FROM scores
    WHERE user_id = user_id;

    -- Calculate the total weight for the user
    SELECT SUM(weight) INTO total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Calculate the average weighted score
    SET avg_weighted_score = weighted_sum / total_weight;

    -- Store the average weighted score in the users table
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;
END;
//

DELIMITER ;
