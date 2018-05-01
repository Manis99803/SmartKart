import sqlite3
db_conn = sqlite3.connect('db.sqlite3')
cursor = db_conn.cursor()
def deleteall():
	cursor.execute("DELETE * FROM product")
	db_conn.commit()
def showdata():
	cursor.execute("SELECT * FROM product")
def fun(idd,name,prod_type,prod_id,processor,ram,external_harddrive,os_name):
	cursor.execute("INSERT INTO electronics(id,name,prod_type,prod_id,processor,ram,external_harddrive,os_name) VALUES(?,?,?,?,?,?,?,?)",(idd,name,prod_type,prod_id,processor,ram,external_harddrive,os_name))
	db_conn.commit()
def addbooks(idd,name,typee,pid,pub,aut,lan):
	cursor.execute("INSERT INTO books(id,name,prod_type,prod_id,publisher,author,Langauage) VALUES(?,?,?,?,?,?,?)",(idd,name,typee,pid,pub,aut,lan))
	db_conn.commit()
def addshipper(idd,name,phno,add):
	cursor.execute("INSERT INTO shipper(id,name,phno,address) VALUES(?,?,?,?)",(idd,name,phno,add))
	db_conn.commit()
def addshipment(idd):
	cursor.execute("INSERT INTO shipment(id) VALUES(?)",(idd))
	db_conn.commit()
def addclothes(idd,nam,typee,pid,color,size):
	cursor.execute("INSERT INTO clothes(id,name,prod_type,prod_id,color,size) VALUES(?,?,?,?,?,?)",(idd,nam,typee,pid,color,size))
	db_conn.commit()
def addproducts(idd,price,typee,brand,color,size):
	cursor.execute("INSERT INTO product(id,price,type,brand,Color,size) VALUES(?,?,?,?,?,?)",(idd,price,typee,brand,color,size))
	db_conn.commit()
def addstock(sid,pid,quan):
	cursor.execute("INSERT INTO stock(sup_id,prod_id,quantity) VALUES(?,?,?)",(sid,pid,quan))
	db_conn.commit()
def addorder(idd,dat,cid,pri,stat):
	cursor.execute("INSERT INTO order(id,date,cust_id,price,status) VALUES(?,?,?,?,?)",(idd,dat,cid,pri,stat))
	db_conn.commit()
def addsupplier(sid,name,phno,add):
	cursor.execute("INSERT INTO supplier(id,name,phno,address) VALUES(?,?,?,?)",(sid,name,phno,add))
	db_conn.commit()
books=[[12,'A handbook on civil engineering','Engineering','0101','Made Easy Publications','Made Easy Editorial Board','English'],
	[23,'A Handbook on Electronics','Engineering','0102','Upkar Prakashan','Kishan Chandana', 'English'],
	[3,'The C Programming Language','Engineering','0103','Upkar Prakashan', 'Tejpal Suman', 'English'],
	[4,'The C Programming Language','Engineering','0104','Pearson Education India', 'Dennis Ritchie', 'English'],
	[5,'Basic Automobile Engineering','Engineering','0105','Dhanpat Rai Publishing Company', 'Nakara CP', 'Hindi'],
	[6,'Civil Engineering(Objective Type)','Engineering','0106','Laxmi Publications', 'PJ Rami Reddy', 'English'],
	[7,'RRR Objective Electrical Engineering Hindi 2018','Engineering','0107','Arihant Publications', 'Arihant Experts', 'Hindi'],
	[8,'Objective Electrical Engineering','Engineering','0108','Upkar Prakashan','PK Mishra','English'],
	[9,'The Business School','Management','0109','Manjul Publishing House', 'Robert Kiyosaki', 'English'],
	[10,'Beyond the MBA Hype','Management','0110','Collins', 'Sameer Kamat', 'English']]
for i in books:
	addbooks(*i)
shipper=[[11111,'Crystal Plewa',7373048147,'9, 51st Street, 7th Avenue'],
	[42527,'Sharee Manley',7373146476,'211, 2nd Floor, Mahavir Commercial Comple, M G Road, Derasar Lane Corner, Ghatkoper (east)'],
	[40041,'Gisele Mata',7373214519,'11, Somaiya Shopping Cen, Sainath Rd, Nr Pawan Hotel, Malad(w)'],
	[25154,'Drew Popovich',7373333920,'E1/a, Midc Shopping Centre, Turbhe Naka, Pfizer Road, Turbhe, Navi Mumbai'],
	[11487,'Clair Knee',7373436334,'14 Goabagan Street, Beadon Street'],
	[32103,'Gerry Coogan',7373513670,'201-a, Vertex Vikas, Mv Road, Andheri (e)'],
	[80837,'Elaina Thatch',7373633473,'202, 1, Jaihind Bldg, Kalbadevi'],
	[49949,'Percy Koons',7373793904,'Preyas Bldg, 20 Dadyseth Rd, Grant Road'],
	[18820,'Claudette Camarillo',7373852255,'268, Shiv Rd, Opp Bus Stop, Ulhasnagar'],
	[68275,'Blossom Hammel',7373966718,'10, D Konddeo Cross Marg, Nr Sussx Indl Est, Byculla, Byculla']]
for i in shipper:
	addshipper(*i)
shipment=[[98353],[67902],[34887],[76132],[19409],[90975],[48418],[59809],[73087],[93350]]
# for i in shipment:
	# addshipment(*i)
supplier=[[69630,'Energy Lighting',8553041145,'Shop No 9, Nr Udipi Hotel, Opp Haveli, M G Rd,jalaram Nagar, Ghatkopar (e)'],
	[90496,'Tide Sports',8553125873,'Link Palace, A/703 Ciba Giegy Rd, Saibaba Complex, Goregaon (east)'],
	[40134,'Jungle Coms',8553249468,'Plot No 11, Shop No 3, Gurushri Bldg, Tarun Bhar, Chakala, Andheri (e)'],
	[63695,'Imaginavigations',8553389220,'124, Yashwant Shopping, Carter Rd No 7, Borivli (e)'],
	[94445,'Spiritechnologies',8553493948,'4-5, Mukund Apartment, Manpada Road, Dombivli(e)'],
	[86070,'Cavernetworks',8553590609,'1st Floor, 3, Purshottam Bldg., 23 Tribhuvan Road, Girgaon'],
	[79252,'Auraking',8553645888,'51/b,lansdown Terrace, Kalighat'],
	[96270,'Spidershade',8553757486,'941, Haines Road, Opp Khatau Mill Main Gate, Byculla'],
	[18038,'Webworld',8553870883,'Shop No 22, Sec 1, Belapur (cbd), Navi Mumbai'],
	[18589,'Fairy Records',8553996815,'Opp Chand Society, Juhu Church Road, Juhu']]
for i in supplier:
	addsupplier(*i)

electronics=[[1,'One Plus 5T','Mobile','0001','Qualcomm Snapdragon 835','6GB','64GB','Android 7.1 Nougat'],
             [2,'Samsung Galaxy A8+','Mobile','0002','Exynos 7885','6GB','64GB','Android 7.1.1 Nougat'],
             [3,'Moto G5s Plus','Mobile','0003', 'Qualcomm Snapdragon 625', '4GB', '64GB', 'Android 7.1 Nougat'],
             [4,'Redmi 4','Mobile','0004', 'Qualcomm Snapdragon 435', '3GB', '32GB', 'Android 7.1.1 Nougat'],
             [5,'Lenovo Ideapad','Laptop','0005','i3 6th gen', '4GB', '1TB', 'DOS'],
             [6,'Asus Vivobook','Laptop','0006', 'Intel core i3 7100U', '4GB', '1TB', 'Windows 10'],
             [7,'Dell Inspiron 15 1567','Laptop','0007', 'Core i3 6006U', '4GB', '1TB', 'Windows 10'],
             [8,'Apple Macbook Air MQD32HN','Laptop','0008', 'Core i5', '8GB', '256GB', 'MacOS'],
             [9,'Apple Macbook Air MQD32HN','Laptop','0009', 'Core i5', '8GB', '512GB', 'MacOS'],
             [10,'Vivo V9','Mobile','0010','Qualcomm Snapdragon 626','4GB','64GB','Android 7.1 Nougat'],
             [11,'Moto G5 Plus','Mobile','0011','Qualcomm Snapdragon 625','4GB','64GB','Android'],
             [12,'Acer Aspire E5-576','Laptop','0012','i7 7th gen','4GB','1TB','Windows 10'],
             [13,'Dell Inspiron 15 3567','Laptop','0013','i3 core','4GB','1TB','Windows 10']]

for item in electronics:
	fun(*item)

clothes=[[1,'Mens T-Shirt','Mens Clothing','0201','Indigo','Medium'],
         [2,'Mens Polo Shirt','Mens Clothing','0202', 'Red', 'Small'],
         [3,'Mens Casual Shirt','Mens Clothing','0203','Light blue', 'Large'],
         [4,'Mens Cotton Kurta','Mens Clothing','0204','Red', 'Medium'],
         [5,'Mens Regular Fit Denim Jeans','Mens Clothing','0205','Sky blue','32'],
         [6,'Womens Salwar Suit','Womens Clothing', '0206', 'Red','34'],
         [7,'Womens Polyester Dress','Womens Clothing','0207','Navy blue','Small'],
         [8,'Womens Skinny Jeans', 'Womens Clothing', '0208', 'Dark Blue', '26'],
         [9,'Saree','Womens Clothing','0209','Yellow','None'],
         [10,'Mens Polo Shirt','Mens Clothing','0210', 'Green', 'Medium'],
         [11,'Mens Casual Shirt','Mens Clothing','0211','Black', 'Small'],
         [12,'Mens T-Shirt','Mens Clothing','0212','Brown','Large']]
for item in clothes:
	addclothes(*item)

products=[['0101',289,'Engineering','Made Easy Publications','blue','medium'],
	['0102',99,'Engineering','Upkar Prakashan','orange','small'],
	['0103',189,'Engineering','Upkar Prakashan','red','small'],
	['0104',250,'Engineering','Pearson Education India','green','big'],
	['0105',399,'Engineering','Dhanpat Rai Publishing Company','white','big'],
	['0106',167,'Engineering','Laxmi Publications','black','small'],
	['0107',199,'Engineering','Arihant Publications','purple','small'],
	['0108',299,'Engineering','Upkar Prakashan','maroon','medium'],
	['0109',140,'Management','Manjul Publishing House','blue','small'],
	['0110',67,'Management','Collins','red','small'],
	['0001',35000.00,'Electronics','One Plus','Black','11'],
          ['0002',32000.00,'Electronics','Samsung','White','12'],
          ['0003',21500.00,'Electronics','Moto','Grey','13'],
          ['0004',16000.00,'Electronics','Redmi','Black','14'],
          ['0005',57000.00,'Electronics','Lenovo','White','12'],
          ['0006',48000.00,'Electronics','Asus','White','13'],
          ['0007',42000.00,'Electronics','Dell','Black','13'],
          ['0008',65000.00,'Electronics','Apple','White','15'],
          ['0009',85000.00,'Electronics','Apple','Gold','18'],
          ['0010',9500.00,'Electronics','Vivo','Gold','11'],
          ['0011',18000.00,'Electronics','Moto','Silver','19'],
          ['0012',39000.00,'Electronics','Acer','Black','16'],
          ['0013',50000.00,'Electronics','Dell','Grey','14'],
          ['0201',99.00,'Mens Clothing','GAP','Indigo','Medium'],
          ['0202',490.00,'Mens Clothing','Wrangler','Red','Small'],
          ['0203',6550.00,'Mens Clothing','Lee','Light blue','Large'],
          ['0204',3400.00,'Mens Clothing','Peter England','Red','Medium'],
          ['0205',560.00,'Mens Clothing','Peter England','Sky Blue','32'],
          ['0206',620.00,'Womens Clothing','BIBA','Red','34'],
          ['0207',900.00,'Womens Clothing','Lee','Navy Blue','Small'],
          ['0208',325.00,'Womens Clothing','Levis','Dark Blue','26'],
          ['0209',990.00,'Womens Clothing','Anand','Yellow','None'],
          ['0210',125.00,'Mens Clothing','GAP','Green','Medium'],
          ['0211',250.00,'Mens Clothing','Ben Martin','Black','Small'],
          ['0212',85.00,'Mens Clothing','Lee','Brown','Large']]
for i in products:
	addproducts(*i)
stock=[[19409,'0001',50],
	[90975,'0001',40],
	[34887,'0002',67],
	[48418,'0003',2],
	[67902,'0004',180],
	[69630,'0005',500],
	[48418,'0005',4],
	[73087,'0006',40],
	[76132,'0007',9],
	[19409,'0007',40],
	[90975,'0008',99],

	[19409,'0101',50],
	[34887,'0102',67],
	[48418,'0102',1],
	[48418,'0103',2],
	[67902,'0104',180],
	[76132,'0104',14],
	[67902,'0108',45],
	[69630,'0105',500],
	[73087,'0106',40],
	[76132,'0107',9],
	[76132,'0108',45],
	[90975,'0108',99],

	[19409,'0201',50],
	[34887,'0202',67],
	[48418,'0203',2],
	[67902,'0204',180],
	[69630,'0205',500],
	[73087,'0206',40],
	[76132,'0207',9],
	[19409,'0208',1],
	[76132,'0208',6],
	[90975,'0208',99],
	]
for i in stock:
	addstock(*i)
order=[[1,"2013-12-04",5,50099,'D'],
	[2,"2013-11-12",3,6550,'ND'],
	[3,"2013-05-28",4,375,'D'],
	[4,"2013-08-11",2,67000,'D']]
# for i in order:
	# addorder(*i)




