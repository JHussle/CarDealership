import connection as c
import mysql.connector

def readVehicleInfo():
    conn = c.returnConnection()
    try:
        table = conn.cursor()
        table.execute("use dealershipapp")
        table.execute('SELECT * FROM product')
        for column in table:
            print(f'''
            Make ........... {column[0]}
            Model .......... {column[1]}
            Model Year ..... {column[2]}
            Color .......... {column[3]}
            Price .......... {column[4]}
            ''')
        table.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)
        

# fName, lName, phone, email, vetDisabled
def insertCustomerInfo(customer):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("use dealershipapp")
        cursor.execute(
            f"INSERT INTO customer (fName, lname, email, phone, vetdisabled) VALUES ('{customer.fName}', '{customer.lName}', '{customer.email}', '{customer.phone}', {customer.vetDisabled})")
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)