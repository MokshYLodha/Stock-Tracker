import mysql.connector as m
mydb = m.connect(host="localhost",user="root",password="moksh24",database="stock")
mycursor = mydb.cursor()
sql = "INSERT INTO product (pcode, pname, pprice, pqty, cat) VALUES (%s, %s, %s, %s, %s)"
product_data = [
    (500325, 'Relaince Industries Ltd                                     ', 1292.24,250000, 'Oil & Gas Telecom'),
    (532540, 'Tata Consultancy Servies Ltd                          ', 4273.33,300000,'IT Services'),
    (500180, 'HDFC Bank Ltd                                                 ', 1797.65,230000, 'Banking'),
    (532454, 'Bharti Airtel Ltd                                                    ', 1627.45,100000, 'Telecom'),
    (500209, 'Infosys Ltd                                                            ', 1858.45,200000, 'IT Services'),
    (532174, 'ICIC Bank Ltd                                                       ', 1300.64,150000, 'Banking'),
    (500875, ' ITC Ltd                                                                  ', 477.05,120000, 'FMCG,Hotes,Paper'),
    (500696, 'Hindustan Unilever Ltd                                        ', 2496.25,100000, 'FMCG'),
    (500510, 'Larsen & Turbo Ltd                                              ', 3725.9,220000, 'Engineering & Construction'),
    (532281, 'HCL Technologies Ltd                                         ', 1858.45,200000, 'IT Services'),
    (524715,'Sun Pharmaceutical Industries Ltd                      ',1781.65,75000,'Pharmaceuticals'),
    (500520,"Mahindra & Mahindra Ltd                                     ",2698.95,135000,"Automobiles, Farm Equipment"),
    (532555,"NTPC Ltd.                                                              ",363.85,100000,"Power Generation"),
    (532215,"Axis Bank Ltd.                                                       ",1136.7,75000,"Banking"),
    (500247,"Kotak Mahindra Bank Ltd.                                   ",1766.8,80000,"Banking"),
    (532500,"Maruti Suzuki India Ltd.                                       ",11072.5,120000,"Automobiles"),
    (532538,"UltraTech Cement Ltd.                                        ",11199.5,250000,"Cement"),
    (532898,"Power Grid Corporation of India Ltd.               ",329.6,50000,"Power Transmission"),
    (507685,"Wipro Ltd.                                                            ",577.95,135000,"IT Services"),
    (500570,"Tata Motors Ltd.                                                  ",786.85,300000,"Automobiles"),
    (532868,"Adani Enterprises Ltd.                                       ",2462.25,250000,"Infrastructure, Ports, Power"),
    (500550,"Siemens Ltd.                                                       ",7560.95,65000,"Engineering"),
    (532921,"Adani Ports and Special Economic Zone Ltd.",1189.65,200000,"Ports, Logistics"),
    (533278,"Coal India Ltd.                                                      ",416.55,185000,"Coal Mining"),
]
try:
    mycursor.executemany(sql, product_data)
    mydb.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as error:
    print(f"Failed to insert data: {error}")

mydb.close()




