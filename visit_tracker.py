import hashlib
import datetime

def track_visit(db_connection, request, page: str):
    # get the sql cursor
    cursor = db_connection.cursor()

    # get the datetime of the visit
    time = datetime.datetime.now()

    # get the ip address of the user
    ip_address = request.remote_addr

    # hash the ip address to anonymize it
    ip_address_hash = hashlib.sha256(ip_address.encode()).hexdigest()

    # get the id of the page
    cursor.execute("SELECT id_page FROM PAGE WHERE page = %s", (page))
    id_page = cursor.fetchone()

    if id_page is None:
        # the page does not exist in the database
        raise Exception("The page does not exist in the database")
    else:
        id_page = id_page["id_page"]

    # insert the visit in the database
    cursor.execute("INSERT INTO VISIT (datetime, ip_hash, id_page) VALUES (%s, %s, %s)", (time, ip_address_hash, id_page))

    # commit the changes
    db_connection.commit()

    # close the cursor
    cursor.close()
