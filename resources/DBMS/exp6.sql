-- Given the tables t1 and t2 created and populated as shown below:

CREATE TABLE t1 (cid INT PRIMARY KEY, Name VARCHAR(20));
INSERT INTO t1 VALUES (1, 'Rahul'), (2, 'Yash'), (3, 'Henry'), (4, 'Smith');

CREATE TABLE t2 (ID INT PRIMARY KEY, cid INT, date INT);
INSERT INTO t2 VALUES (1, 1, 2017), (2, 2, 2017), (3, 2, 2017), (4, 1, 2018), (5, 3, 2018);

SELECT * FROM t1;
SELECT * FROM t2;
SELECT cid FROM t1 WHERE cid <> ALL (SELECT cid FROM t2);
SELECT cid FROM t1 WHERE cid <> ANY (SELECT cid FROM t2);
SELECT cid FROM t1 WHERE cid = ANY (SELECT cid FROM t2);
SELECT cid FROM t1 WHERE cid = SOME (SELECT cid FROM t2);
SELECT cid FROM t1 WHERE EXISTS (SELECT * FROM t2 WHERE t1.cid =t2.cid);
SELECT cid FROM t1 WHERE NOT EXISTS (SELECT * FROM t2 WHERE t1.cid = t2.cid);



-- 6B
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50)
);
INSERT INTO Students (ID, Name)
VALUES
    (1, 'John'),
    (2, 'Alice'),
    (3, 'Bob'),
    (4, 'Emily');
CREATE TABLE Grades (
    GID INT PRIMARY KEY,
    ID INT,
    Subject VARCHAR(50),
    Score INT,
    FOREIGN KEY (ID) REFERENCES Students(ID)
);
INSERT INTO Grades (GID, ID, Subject, Score)
VALUES
    (101, 1, 'Math', 85),
    (102, 2, 'Math', 95),
    (103, 3, 'Math', 88),
    (104, 4, 'Math', 92);
SELECT Name
FROM Students
WHERE ID IN (
    SELECT ID
    FROM Grades
    WHERE Subject = 'Math' AND Score > 90
);



SELECT Name, ID
FROM Students s
WHERE ID IN (
    SELECT ID
    FROM Grades g
    WHERE g.Subject = 'Math'
);

UPDATE Grades G
SET Score = Score + 5
WHERE  (
    SELECT 1
    FROM Students S
    WHERE S.ID = G.ID
);
SELECT * FROM Grades;

DELETE FROM Grades g
WHERE Score < (
    SELECT 93
    FROM Students s
    WHERE g.ID = s.ID
);
SELECT * FROM Grades;



UPDATE Grades G
SET Score = Score + 5
WHERE Subject = 'Math'
  AND Score < 90
  AND EXISTS (
    SELECT 1
    FROM Students S
    WHERE S.ID = G.ID
);
SELECT * FROM Grades;

DELETE FROM Grades
WHERE NOT EXISTS (
    SELECT 1
    FROM Students S
    WHERE S.ID = Grades.ID
);
SELECT * FROM Grades;