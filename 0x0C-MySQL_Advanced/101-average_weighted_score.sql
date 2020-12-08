-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u set average_score = (SELECT 
    SUM((c.score) * p.weight) / (SUM(p.weight)) 'avg'
    FROM corrections as c
    INNER JOIN projects AS p 
    ON p.id = c.project_id 
    where c.user_id = u.id);
END $$
