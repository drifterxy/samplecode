# samplecodes



generate_table_dict.py
working python3 code to generate database tables dictionaries

TABLE ADDONITEMS 
Field,Type,Null,Key,Default,Extra
Id,char(36),NO,PRI,,
CategoryId,char(36),YES,MUL,,
CreatedAt,datetime(6),NO,,,
CreatedByUserId,char(36),NO,,,
Image,longtext,YES,,,
MaximumQty,int(11),NO,,,
MinimumQty,int(11),NO,,,
Name,longtext,YES,,,
Price,"decimal(65,30)",NO,,,
Unit,longtext,YES,,,
UpdatedAt,datetime(6),NO,,,
UpdatedByUserId,char(36),NO,,,
SupplierId,char(36),YES,MUL,,
Description,longtext,YES,,,
