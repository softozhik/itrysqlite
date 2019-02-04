 
CREATE TABLE IF NOT EXISTS `computers` (
	`Inventory`	INTEGER NOT NULL UNIQUE,
	`User`	TEXT,
	`OS`	TEXT,
	`CompName`	TEXT
);
