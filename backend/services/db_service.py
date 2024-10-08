import pymysql

def check_virus_database(file_hash):
    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='password',  # Replace with your actual MySQL password
                                 db='safescan')  # The name of your MySQL database

    try:
        with connection.cursor() as cursor:
            # SQL query to check if the hash exists in the virus_hashes table
            sql = "SELECT virus_name FROM virus_hashes WHERE hash=%s"
            cursor.execute(sql, (file_hash,))
            result = cursor.fetchone()

            # If a virus hash is found, return its details
            if result:
                return {'status': 'infected', 'virus_name': result[0]}
            else:
                return {'status': 'clean'}
    
    finally:
        # Ensure the database connection is closed after the query
        connection.close()