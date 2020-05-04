import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# handled in resourceHandler, may need to add stuff there
class RequestDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == "ResourceName":
            return "order by resource_name "
        elif attribute == "RequestID":
            return "order by request_id "
        # elif attribute == "":
            # return "order by "
        else:
            return ""
