CREATE TABLE student (
    Sid INT PRIMARY KEY,
    Sname VARCHAR(50),
    Branch VARCHAR(50),
    Marks INT
);
INSERT INTO student (Sid, Sname, Branch, Marks) VALUES
(1, 'Lenin', 'IT', 75),
(2, 'Sam', 'CSE', 92),
(3, 'Shivam', 'ECE', 56),
(4, 'Peter', 'IT', 82),
(5, 'John', NULL, 89);

CREATE TABLE faculty (
    Fid INT PRIMARY KEY,
    Fname VARCHAR(50),
    Qualification VARCHAR(50),
    Deptid INT
);
INSERT INTO faculty (Fid, Fname, Qualification, Deptid) VALUES
(1, 'Adam', 'B.Tech', 1),
(2, 'Milan', 'M.Tech', 1),
(3, 'Victor', 'M.Tech', 1),
(4, 'Peter', 'Phd', 2),
(5, 'Ricky', 'Phd', 3),
(6, 'Alice', 'M.Tech', 2);

CREATE TABLE department (
    Deptid INT PRIMARY KEY,
    Dname VARCHAR(50)
);
INSERT INTO department (Deptid, Dname) VALUES
(1, 'IT'),
(2, 'CSE'),
(3, 'ECE'),
(4, 'EEE');

CREATE VIEW view1 AS
SELECT * FROM student
WHERE branch IN ('IT', 'CSE');

CREATE VIEW view2 AS
SELECT * FROM student
WHERE marks > (SELECT AVG(marks) FROM student);

CREATE VIEW view3 AS
SELECT * FROM faculty
WHERE deptid IN (1, 2);

INSERT INTO view3 VALUES (7, 'Henry', 'Phd', 2);