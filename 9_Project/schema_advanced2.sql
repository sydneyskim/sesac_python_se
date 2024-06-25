CREATE TABLE IF NOT EXISTS "users"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Gender" TEXT, 
    "Age" INTEGER,
    "Birthdate" DATE, 
    "Address" TEXT);

-- CONSTRAINT를 설정하는 과정

CREATE TABLE IF NOT EXISTS "stores"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Type" TEXT, 
    "Address" TEXT);

CREATE TABLE IF NOT EXISTS "orders"(
    "Id" TEXT PRIMARY KEY, 
    "OrderAt" DATETIME NOT NULL CHECK(OrderAt <= CURRENT_TIMESTAMP), 
    "StoreId" TEXT NOT NULL, 
    "UserId" TEXT NOT NULL
    FOREIGN KEY ('StoreId') REFERENCES "Store"("Id"), -- "Store"("Id") => "stores.Id" (대체가능)
    FOREIGN KEY ('UserId') REFERENCES "users"("Id") -- "users"("Id") => "users.Id" (대체가능)
    );

CREATE TABLE IF NOT EXISTS "items"(
    "Id" TEXT PRIMARY KEY, 
    "Name" TEXT NOT NULL, 
    "Type" TEXT, 
    "UnitPrice" INTEGER CHECK(UnitPrice >= 0)
    ); -- 미국 달러면 REAL 을 통한 소수점 지원

CREATE TABLE IF NOT EXISTS "orderitems"(
    "Id" TEXT PRIMARY KEY, 
    "OrderId" TEXT NOT NULL, 
    "ItemId" TEXT NOT NULL
    FOREIGN KEY ('OrderId') REFERENCES "orders"("Id") ON DELETE CASCADE, 
    FOREIGN KEY ('ItemId') REFERENCES "items"("Id")
    );