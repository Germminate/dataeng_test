BEGIN;

CREATE TABLE IF NOT EXISTS Cars (
    CarSerial bigint NOT NULL PRIMARY KEY,
    Manufacturer text NOT NULL,
    Model text NOT NULL,
    Mass  bigint NOT NULL,
    Price bigint NOT NULL
);

CREATE TABLE IF NOT EXISTS SalesPersons (
    SalesID bigint NOT NULL PRIMARY KEY,
    PersonName text NOT NULL
);

CREATE TABLE IF NOT EXISTS Customer (
    CustID bigint NOT NULL PRIMARY KEY,
    CustName text NOT NULL,
    CustPhone bigint NOT NULL
);

CREATE TABLE IF NOT EXISTS Sales (
    SaleDate date NOT NULL PRIMARY KEY,
    CustID bigint NOT NULL references Customer (CustID),
    SalesID bigint NOT NULL references SalesPersons (SalesID),
    CarSerial bigint NOT NULL references Cars (CarSerial)
);

END;