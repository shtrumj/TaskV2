create table employees
(
    id        INTEGER not null
        primary key,
    firstName TEXT,
    lastName  TEXT,
    email     VARCHAR(25)
        unique,
    phone     TEXT
);

INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (1, 'יהונתן', 'שטרום', 'yonatan@trot.co.il', '054-8018016');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (2, 'אורטל', 'לוי', 'ortal@trot.co.il', '054-4929329');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (3, 'ניצן', 'בר', 'nitzan@trot.co.il', '054-4328832');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (4, 'ירון', 'כלימיאן', 'yaron@trot.co.il', '054-4819030');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (5, 'אליאל', 'כרמי', 'eliel@trot.co.il', '053-8243355');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (6, 'שי', 'כרמלי', 'shay@trot.co.il', '052-8833989');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (7, 'רועי', 'ארביב', 'roy@trot.co.il', '050-4882345');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (8, 'אופק', 'אלבז', 'ofek@trot.co.il', '050-9511301');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (9, 'עידן', 'בר סבר', 'idan@trot.co.il', '052-3911746');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (10, 'אלכס', 'אבזלמן', 'alex@trot.co.il', '050-6928029');
INSERT INTO employees (id, firstName, lastName, email, phone) VALUES (11, 'חן', 'גפנר', 'chen@trot.co.il', '054-6395044');
