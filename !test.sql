SELECT * FROM users;
DELETE FROM users WHERE user_firstname = 'Angela';

UPDATE users SET user_verified_at = 1 WHERE user_firstname = 'Lasse';
UPDATE users SET user_role = 1 WHERE user_firstname = 'Lasse';

SELECT * FROM users WHERE NOT user_role = 0;

SELECT * FROM users WHERE user_id = '35302d9a87374f19891f0271072e5656';