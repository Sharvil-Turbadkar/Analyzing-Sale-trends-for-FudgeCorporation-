/****** Object:  Database UNKNOWN    Script Date: 4/18/2020 12:41:18 PM ******/
/*
Kimball Group, The Microsoft Data Warehouse Toolkit
Generate a database from the datamodel worksheet, version: 4

You can use this Excel workbook as a data modeling tool during the logical design phase of your project.
As discussed in the book, it is in some ways preferable to a real data modeling tool during the inital design.
We expect you to move away from this spreadsheet and into a real modeling tool during the physical design phase.
The authors provide this macro so that the spreadsheet isn't a dead-end. You can 'import' into your
data modeling tool by generating a database using this script, then reverse-engineering that database into
your tool.

Uncomment the next lines if you want to drop and create the database
*/
/*
DROP DATABASE UNKNOWN
GO
CREATE DATABASE UNKNOWN
GO
ALTER DATABASE UNKNOWN
SET RECOVERY SIMPLE
GO
*/

-- Create a schema to hold user views (set schema name on home page of workbook).
-- It would be good to do this only if the schema doesn't exist already.
--GO
--CREATE SCHEMA fudgemartg2
--GO
--use ist722_hhkhan_cc2_stage;

--alter table dbo.stgFudgeMartCustomers
--alter column customer_id nvarchar(6);

--use ist722_hhkhan_cc2_dw;

--alter table fudgemartg2.DimProduct
--alter column ProductName varchar(50);

--alter table fudgemartg2.DimProduct
--drop constraint [DF__DimProduc__Suppl__4FD1D5C8];

--alter table fudgemartg2.DimProduct
--alter column SupplierName nvarchar(50);

--alter table fudgemartg2.DimCustomer
--alter column CustomerCity varchar(50);

--alter table fudgemartg2.DimCustomer
--alter column CustomerState varchar(50);

--alter table fudgemartg2.DimCustomer
--alter column CustomerEmail varchar(200);

--alter table fudgemartg2.DimCustomer
--alter column CustomerZip varchar(20);

--alter table fudgemartg2.DimCustomer
--alter column CustomerName nvarchar(101);

IF (NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'fudgemartg2')) 
BEGIN
    EXEC ('CREATE SCHEMA [fudgemartg2] AUTHORIZATION [dbo]')
	PRINT 'CREATE SCHEMA [fudgemartg2] AUTHORIZATION [dbo]'
END
go 

-- delete all the fact tables in the schema
DECLARE @fact_table_name varchar(100)
DECLARE cursor_loop CURSOR FAST_FORWARD READ_ONLY FOR 
	select TABLE_NAME from INFORMATION_SCHEMA.TABLES 
		where TABLE_SCHEMA='fudgemartg2' and TABLE_NAME like 'Fact%'
OPEN cursor_loop
FETCH NEXT FROM cursor_loop  INTO @fact_table_name
WHILE @@FETCH_STATUS= 0
BEGIN
	EXEC ('DROP TABLE [fudgemartg2].[' + @fact_table_name + ']')
	PRINT 'DROP TABLE [fudgemartg2].[' + @fact_table_name + ']'
	FETCH NEXT FROM cursor_loop  INTO @fact_table_name
END
CLOSE cursor_loop
DEALLOCATE cursor_loop
go
-- delete all the other tables in the schema
DECLARE @table_name varchar(100)
DECLARE cursor_loop CURSOR FAST_FORWARD READ_ONLY FOR 
	select TABLE_NAME from INFORMATION_SCHEMA.TABLES 
		where TABLE_SCHEMA='fudgemartg2' and TABLE_TYPE = 'BASE TABLE'
OPEN cursor_loop
FETCH NEXT FROM cursor_loop INTO @table_name
WHILE @@FETCH_STATUS= 0
BEGIN
	EXEC ('DROP TABLE [fudgemartg2].[' + @table_name + ']')
	PRINT 'DROP TABLE [fudgemartg2].[' + @table_name + ']'
	FETCH NEXT FROM cursor_loop  INTO @table_name
END
CLOSE cursor_loop
DEALLOCATE cursor_loop
go

--use ist722_hhkhan_cc2_dw;
----Alterations made for Loading to be sucessfull
--select * from fudgemartg2.DimCustomer;

--alter table fudgemartg2.DimCustomer
--alter column [CustomerCity] varchar(50);

--alter table fudgemartg2.DimCustomer
--drop constraint DF__DimCustom__Custo__1758727B;

--alter table fudgemartg2.DimCustomer
--alter column [CustomerEmail] varchar(100);

--alter table fudgemartg2.DimCustomer
--alter column [CustomerZip] varchar(20);

--alter table fudgemartg2.DimCustomer
--alter column [CustomerName] nvarchar(101);

--alter table fudgemartg2.DimCustomer
--alter column [CustomerState] varchar(20);

--alter table fudgemartg2.DimCustomer
--alter column [CustomerCity] varchar(50);

--alter table fudgemartg2.DimCustomer
--alter column [SourceType] nvarchar(50);

/* Drop table fudgemartg2.DimCustomer */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudgemartg2.DimCustomer') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudgemartg2.DimCustomer 
;

/* Create table fudgemartg2.DimCustomer */
CREATE TABLE fudgemartg2.DimCustomer (
   [CustomerKey]  int IDENTITY  NOT NULL
,  [CustomerID]  int  NOT NULL
,  [CustomerName]  nvarchar(101)   NOT NULL
,  [CustomerCity]  varchar(50)   NOT NULL
,  [CustomerState] varchar(50)   NOT NULL
,  [CustomerZip]  varchar(20)   NOT NULL
,  [CustomerEmail]  varchar(200)  DEFAULT 'N/A' NOT NULL
,  [SourceType] nvarchar(10) NOT NULL
,  [RowIsCurrent]  bit  DEFAULT 1 NOT NULL
,  [RowStartDate]  datetime  DEFAULT '12/31/1899' NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)   NULL
, CONSTRAINT [PK_fudgemartg2.DimCustomer] PRIMARY KEY CLUSTERED 
( [CustomerKey])
) ON [PRIMARY]
;


SET IDENTITY_INSERT fudgemartg2.DimCustomer ON
;
INSERT INTO fudgemartg2.DimCustomer (CustomerKey, CustomerID, CustomerName, CustomerCity, CustomerState, CustomerZip, CustomerEmail, SourceType, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, -1, 'No Customer', 'None', 'None', 'None', 'None', 'None', 1, '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT fudgemartg2.DimCustomer OFF
;

-- User-oriented view definition
GO
IF EXISTS (select * from sys.views where object_id=OBJECT_ID(N'[fudgemartg2].[Customer]'))
DROP VIEW [fudgemartg2].[Customer]
GO
CREATE VIEW [fudgemartg2].[Customer] AS 
SELECT [CustomerKey] AS [CustomerKey]
, [CustomerID] AS [CustomerID]
, [CustomerName] AS [CustomerName]
, [CustomerCity] AS [CustomerCity]
, [CustomerState] AS [CustomerState]
, [CustomerZip] AS [CustomerZip]
, [CustomerEmail] AS [CustomerEmail]
, [SourceType] AS [SourceType]
, [RowIsCurrent] AS [Row Is Current]
, [RowStartDate] AS [Row Start Date]
, [RowEndDate] AS [Row End Date]
, [RowChangeReason] AS [Row Change Reason]
FROM fudgemartg2.DimCustomer
GO

/* Drop table fudgemartg2.DimDate */
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudgemartg2.DimDate') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudgemartg2.DimDate 
;

/* Create table fudgemartg2.DimDate */
CREATE TABLE fudgemartg2.DimDate (
   [DateKey]  int   NOT NULL
,  [Date]  datetime   NULL
,  [FullDateUSA]  nchar(11)   NOT NULL
,  [DayOfWeek]  tinyint   NOT NULL
,  [DayName]  nchar(10)   NOT NULL
,  [DayOfMonth]  tinyint   NOT NULL
,  [DayOfYear]  int   NOT NULL
,  [WeekOfYear]  tinyint   NOT NULL
,  [MonthName]  nchar(10)   NOT NULL
,  [MonthOfYear]  tinyint   NOT NULL
,  [Quarter]  tinyint   NOT NULL
,  [QuarterName]  nchar(10)   NOT NULL
,  [Year]  int   NOT NULL
,  [IsWeekday]  varchar(1) NOT NULL DEFAULT (('N'))
, CONSTRAINT [PK_fudgemartg2.DimDate] PRIMARY KEY CLUSTERED 
( [DateKey] )
) ON [PRIMARY]
;

INSERT INTO fudgemartg2.DimDate (DateKey, Date, FullDateUSA, DayOfWeek, DayName, DayOfMonth, DayOfYear, WeekOfYear, MonthName, MonthOfYear, Quarter, QuarterName, Year, IsWeekday)
VALUES (-1, '12/31/1899', 'Unk date', 0, 'Unk date', 0, 0, 0, 'Unk month', 0, 0, 'Unk qtr', 0, 0)
;

-- User-oriented view definition
GO
IF EXISTS (select * from sys.views where object_id=OBJECT_ID(N'[fudgemartg2].[Date]'))
DROP VIEW [fudgemartg2].[Date]
GO
CREATE VIEW [fudgemartg2].[Date] AS 
SELECT [DateKey] AS [DateKey]
, [Date] AS [Date]
, [FullDateUSA] AS [FullDateUSA]
, [DayOfWeek] AS [DayOfWeek]
, [DayName] AS [DayName]
, [DayOfMonth] AS [DayOfMonth]
, [DayOfYear] AS [DayOfYear]
, [WeekOfYear] AS [WeekOfYear]
, [MonthName] AS [MonthName]
, [MonthOfYear] AS [MonthOfYear]
, [Quarter] AS [Quarter]
, [QuarterName] AS [QuarterName]
, [Year] AS [Year]
, [IsWeekday] AS [IsWeekday]
FROM fudgemartg2.DimDate
GO

/* Drop table fudgemartg2.DimProduct */------------------------------------------------------------------------------------------------
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudgemartg2.DimProduct') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudgemartg2.DimProduct 
;

/* Create table fudgemartg2.DimProduct */
CREATE TABLE fudgemartg2.DimProduct (
   [ProductKey]  int IDENTITY  NOT NULL
,  [ProductID]  int   NOT NULL
,  [ProductName]  varchar(50)   NOT NULL
,  [IsActive]  nchar(1)  DEFAULT 'N' NOT NULL
,  [SupplierName]  varchar(50)  NOT NULL
,  [CategoryName]  varchar(50)  NOT NULL
,  [SourceType] nvarchar(10) NOT NULL
,  [RowIsCurrent]  bit  DEFAULT 1 NOT NULL
,  [RowStartDate]  datetime  DEFAULT '12/31/1899' NOT NULL
,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
,  [RowChangeReason]  nvarchar(200)   NULL
, CONSTRAINT [PK_fudgemartg2.DimProduct] PRIMARY KEY CLUSTERED 
( [ProductKey])
) ON [PRIMARY]
;

SET IDENTITY_INSERT fudgemartg2.DimProduct ON
;
INSERT INTO fudgemartg2.DimProduct (ProductKey, ProductID, ProductName, IsActive, SupplierName, CategoryName,SourceType, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
VALUES (-1, -1, 'None', '?', 'None', 'None','None', 1, '12/31/1899', '12/31/9999', 'N/A')
;
SET IDENTITY_INSERT fudgemartg2.DimProduct OFF
;

-- User-oriented view definition
GO
IF EXISTS (select * from sys.views where object_id=OBJECT_ID(N'[fudgemartg2].[Product]'))
DROP VIEW [fudgemartg2].[Product]
GO
CREATE VIEW [fudgemartg2].[Product] AS 
SELECT [ProductKey] AS [ProductKey]
, [ProductID] AS [ProductID]
, [ProductName] AS [ProductName]
, [IsActive] AS [IsActive]
, [SupplierName] AS [SupplierName]
, [CategoryName] AS [CategoryName]
, [SourceType] AS [SourceType]
, [RowIsCurrent] AS [Row Is Current]
, [RowStartDate] AS [Row Start Date]
, [RowEndDate] AS [Row End Date]
, [RowChangeReason] AS [Row Change Reason]
FROM fudgemartg2.DimProduct
GO

--/* Drop table fudgemartg2.DimEmployee */----------------------------------------------------------------------------------------------------
--IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudgemartg2.DimEmployee') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
--DROP TABLE fudgemartg2.DimEmployee 
--;

--/* Create table fudgemartg2.DimEmployee */
--CREATE TABLE fudgemartg2.DimEmployee (
--   [EmployeeKey]  int IDENTITY  NOT NULL
--,  [EmployeeID]  int  DEFAULT -1 NOT NULL
--,  [EmployeeName]  nvarchar(50)  DEFAULT 'NoEmpName' NOT NULL
--,  [EmployeeTitle]  nvarchar(20)  DEFAULT 'NoEmpTitle' NOT NULL
--,  [RowIsCurrent]  bit   DEFAULT 1 NOT NULL
--,  [RowStartDate]  datetime  DEFAULT '12/31/1899' NOT NULL
--,  [RowEndDate]  datetime  DEFAULT '12/31/9999' NOT NULL
--,  [RowChangeReason]  nvarchar(200)   NULL
--, CONSTRAINT [PK_fudgemartg2.DimEmployee] PRIMARY KEY CLUSTERED 
--( [EmployeeKey] )
--) ON [PRIMARY]
--;


--SET IDENTITY_INSERT fudgemartg2.DimEmployee ON
--;
--INSERT INTO fudgemartg2.DimEmployee (EmployeeKey, EmployeeID, EmployeeName, EmployeeTitle, RowIsCurrent, RowStartDate, RowEndDate, RowChangeReason)
--VALUES (-1, -1, 'None', 'None', 1, '12/31/1899', '12/31/9999', 'N/A')
--;
--SET IDENTITY_INSERT fudgemartg2.DimEmployee OFF
--;

---- User-oriented view definition
--GO
--IF EXISTS (select * from sys.views where object_id=OBJECT_ID(N'[fudgemartg2].[Employee]'))
--DROP VIEW [fudgemartg2].[Employee]
--GO
--CREATE VIEW [fudgemartg2].[Employee] AS 
--SELECT [EmployeeKey] AS [EmployeeKey]
--, [EmployeeID] AS [EmployeeID]
--, [EmployeeName] AS [EmployeeName]
--, [EmployeeTitle] AS [EmployeeTitle]
--, [RowIsCurrent] AS [Row Is Current]
--, [RowStartDate] AS [Row Start Date]
--, [RowEndDate] AS [Row End Date]
--, [RowChangeReason] AS [Row Change Reason]
--FROM fudgemartg2.DimEmployee
--GO



/* Drop table fudgemartg2.FactSales */-------------------------------------------------------------------------------------------------------
IF EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'fudgemartg2.FactSales') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE fudgemartg2.FactSales 
;

/* Create table fudgemartg2.FactSales */
CREATE TABLE fudgemartg2.FactSales (
   [ProductKey]  int   NOT NULL
,  [CustomerKey]  int   NOT NULL
--,  [EmployeeKey]  int   NOT NULL
,  [OrderDateKey]  int   NOT NULL
,  [OrderID]  int   NOT NULL
,  [Quantity]  int   NOT NULL
,  [ExtendedPriceAmount]  money   NOT NULL
,  [UnitPrice]  money   NOT NULL
,  [SourceType] nvarchar(10) NOT NULL
, CONSTRAINT [PK_fudgemartg2.FactSales] PRIMARY KEY NONCLUSTERED 
( [ProductKey], [OrderID] )
) ON [PRIMARY]
;


-- User-oriented view definition
GO
IF EXISTS (select * from sys.views where object_id=OBJECT_ID(N'[fudgemartg2].[Sales]'))
DROP VIEW [fudgemartg2].[Sales]
GO
CREATE VIEW [fudgemartg2].[Sales] AS 
SELECT [ProductKey] AS [ProductKey]
, [CustomerKey] AS [CustomerKey]
--, [EmployeeKey] AS [EmployeeKey]
, [OrderDateKey] AS [OrderDateKey]
, [OrderID] AS [OrderID]
, [Quantity] AS [Quantity]
, [ExtendedPriceAmount] AS [ExtendedPriceAmount]
, [UnitPrice] AS [UnitPrice]
, [SourceType] AS [SourceType]
FROM fudgemartg2.FactSales
GO


ALTER TABLE fudgemartg2.FactSales ADD CONSTRAINT
   FK_fudgemartg2_FactSales_ProductKey FOREIGN KEY
   (
   ProductKey
   ) REFERENCES fudgemartg2.DimProduct
   ( ProductKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
ALTER TABLE fudgemartg2.FactSales ADD CONSTRAINT
   FK_fudgemartg2_FactSales_CustomerKey FOREIGN KEY
   (
   CustomerKey
   ) REFERENCES fudgemartg2.DimCustomer
   ( CustomerKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
--ALTER TABLE fudgemartg2.FactSales ADD CONSTRAINT
--   FK_fudgemartg2_FactSales_EmployeeKey FOREIGN KEY
--   (
--   EmployeeKey
--   ) REFERENCES fudgemartg2.DimEmployee
--   ( EmployeeKey )
--     ON UPDATE  NO ACTION
--     ON DELETE  NO ACTION
--;
 
ALTER TABLE fudgemartg2.FactSales ADD CONSTRAINT
   FK_fudgemartg2_FactSales_OrderDateKey FOREIGN KEY
   (
   OrderDateKey
   ) REFERENCES fudgemartg2.DimDate
   ( DateKey )
     ON UPDATE  NO ACTION
     ON DELETE  NO ACTION
;
 
