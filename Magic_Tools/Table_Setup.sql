DROP TABLE IF EXISTS Card_Types;
DROP TABLE IF EXISTS Card_Subtypes;
DROP TABLE IF EXISTS Legalities;
DROP TABLE IF EXISTS LegalTypes;
DROP TABLE IF EXISTS DeckList;
DROP TABLE IF EXISTS Decks;
DROP TABLE IF EXISTS Colors;
DROP TABLE IF EXISTS Types;
DROP TABLE IF EXISTS Subtypes;
DROP TABLE IF EXISTS Cards;
DROP TABLE IF EXISTS Sets;
DROP TABLE IF EXISTS Formats;
DROP TABLE IF EXISTS ColorIdentity;
DROP TABLE IF EXISTS Supertypes;

CREATE TABLE Formats (
	 FormatID INT AUTO_INCREMENT
	,FormatName VARCHAR(20)
	,PRIMARY KEY(FormatID)
);

CREATE TABLE Colors (
	 ColorID INT AUTO_INCREMENT
	,Color VARCHAR(10)
	,ColorSymbol VARCHAR(10)
	,PRIMARY KEY (ColorID)
);

CREATE TABLE ColorIdentity (
	 CIdentityID INT AUTO_INCREMENT
	,CIdentityName VARCHAR(50)
	,CIdentitySymbol VARCHAR(10)
	,PRIMARY KEY (CIdentityID)
);

CREATE TABLE Supertypes (
	 SupertypeID INT AUTO_INCREMENT
	,SupertypeDesc VARCHAR(20)
	,PRIMARY KEY (SupertypeID)
);

CREATE TABLE Types (
	 TypeID INT AUTO_INCREMENT
	,TypeDesc VARCHAR(50)
	,PRIMARY KEY (TypeID)
);

CREATE TABLE Subtypes (
	 SubtypeID INT AUTO_INCREMENT
	,SubtypeDesc VARCHAR(50)
	,PRIMARY KEY (SubtypeID)
);

CREATE TABLE Sets (
	 SetCode VARCHAR(10)
	,SetName VARCHAR(100)
	,PRIMARY KEY (SetCode)
);

CREATE TABLE Cards (
	 CardID INT AUTO_INCREMENT
	,CMC DOUBLE
	,ImageURL VARCHAR(4000)
	,ManaCost VARCHAR(50)
	,NAME VARCHAR(100)
	,Number VARCHAR(10)
	,Power VARCHAR(10)
	,Rarity VARCHAR(20)
	,SetCode VARCHAR(10)
	,Text VARCHAR(4000)
	,Toughness VARCHAR(10)
	,PRIMARY KEY (CardID)
	,FOREIGN KEY (SetCode) REFERENCES Sets(SetCode)
);

CREATE TABLE Card_Types (
	 CTypeID INT AUTO_INCREMENT
	,CardID INT
	,TypeID INT
	,PRIMARY KEY (CTypeID)
	,FOREIGN KEY (CardID) REFERENCES Cards(CardID)
	,FOREIGN KEY (TypeID) REFERENCES Types(TypeID)
);

CREATE TABLE Card_Subtypes (
	 CSubtypeID INT AUTO_INCREMENT
	,CardID INT
	,SubtypeID INT
	,PRIMARY KEY (CSubtypeID)
	,FOREIGN KEY (CardID) REFERENCES Cards(CardID)
	,FOREIGN KEY (SubtypeID) REFERENCES Subtypes(SubtypeID)
);

CREATE TABLE Decks (
	 DeckID INT AUTO_INCREMENT
	,DeckName VARCHAR(25)
	,FormatID INT
	,PRIMARY KEY (DeckID)
	,FOREIGN KEY (FormatID) REFERENCES Formats(FormatID)
);

CREATE TABLE DeckList (
	 DListID INT AUTO_INCREMENT
	,CardID INT
	,NumberCopies INT
	,PRIMARY KEY (DListID)
	,FOREIGN KEY (CardID) REFERENCES Cards(CardID)
);

CREATE TABLE LegalTypes (
	 LTypeID INT AUTO_INCREMENT
	,LTypeDesc VARCHAR(10)
	,PRIMARY KEY (LTypeID)
);

CREATE TABLE Legalities (
	 LegalID INT AUTO_INCREMENT
	,FormatID INT
	,CardID INT
	,LTypeID INT
	,PRIMARY KEY (LegalID)
	,FOREIGN KEY (FormatID) REFERENCES Formats(FormatID)
	,FOREIGN KEY (CardId) REFERENCES Cards(CardID)
	,FOREIGN KEY (LTypeID) REFERENCES LegalTypes(LTypeID)
);

INSERT INTO Colors(
	 Color
	,ColorSymbol
) VALUES
	 ('Black','B')
	,('Blue','U')
	,('Green','G')
	,('Red','R')
	,('White','W');

INSERT INTO ColorIdentity(
	CIdentityName
	,CIdentitySymbol
) VALUES
	-- Mono Colors
	 ('Mono Black','B')
	,('Mono Blue','U')
	,('Mono Green','G')
	,('Mono Red','R')
	,('Mono White','W')

	-- Dual Colors
	,('Aorious','WU')
	,('Boros','RW')
	,('Dimir','UB')
	,('Golgari','BG')
	,('Gruul','RG')
	,('Izzet','UR')
	,('Orzhov','WB')
	,('Rakdos','BR')
	,('Selesnya','GW')
	,('Simic','GU')

	-- Tri Colors
	,('Abzan','BWG')
	,('Bant','WGU')
	,('Esper','UWB')
	,('Grixis','BRU')
	,('Jeskai','URW')
	,('Jund','RGB')
	,('Mardu','RWB')
	,('Naya','GWR')
	,('Sultai','BGU')
	,('Temur','GRU')

	-- Quad Colors
	,('Non-White','UBRG')
	,('Non-Blue','BRGW')
	,('Non-Black','RGWB')
	,('Non-Red','GWUB')
	,('Non-Green','WUBR')

	-- Other
	,('Rainbow','WUBRG')
	,('Diamond','D');

INSERT INTO LegalTypes (
	LTypeDesc
) VALUES
	 ('Legal')
	,('Banned')
	,('Restricted');

INSERT INTO Formats (
	 FormatName
) VALUES
	 ('Standard')
	,('Commander')
	,('Duel')
	,('Legacy')
	,('Modern')
	,('Pioneer')
	,('Vintage')
	,('Pauper')
	,('Brawl')
	,('Future')
	,('Historic');
