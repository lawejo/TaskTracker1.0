SELECT * FROM users;
DELETE FROM users WHERE user_firstname = 'Angela';

UPDATE users SET user_verified_at = 1 WHERE user_firstname = 'Anna';
UPDATE users SET user_role = 1 WHERE user_firstname = 'Nadja';

SELECT * FROM users WHERE NOT user_role = 0;