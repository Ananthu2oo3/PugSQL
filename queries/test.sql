-- :name create :insert
CREATE TABLE Entry_logs (
	name TEXT NOT NULL,
    enter TEXT NOT NULL,
    exit TEXT NOT NULL
);

-- :name insert :insert
INSERT INTO Entry_logs (name, enter, exit) VALUES(:name, :enter, :exit);


-- :name printall :many
SELECT * FROM Entry_logs ;


-- :name print_name :one
select * from Entry_logs where name = :name