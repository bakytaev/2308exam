CREATE FUNCTION get_course_id_by_email() RETURNS id $$
SELECT id FROM user_course
WHERE 
$$ LANGUAGE SQL;