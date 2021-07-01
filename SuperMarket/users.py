import csv


class Users:
    def login(self, username, password):
        """

        @type password: str
        @type username: str
        @rtype: dict
        """
        with open('dataFiles/users.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if row[0] == username and row[1] == password:
                    return {'username': row[0],
                            'type': row[2]}
            return None

    def changePassword(self, username, password):
        """

        @type password: str
        @type username: str
        """
        lines = []
        with open('dataFiles/users.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == username:
                    lines[-1][1] = password
        with open('dataFiles/users.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def addUser(self, username, password):
        """

        @type password: str
        @type username: str
        """
        if self.isUsernameAvailable(username):
            with open('dataFiles/users.txt', 'a', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow([username, password,'user'])
        else:
            raise

    def isUsernameAvailable(self, username):
        """

        @type username: str
        """
        with open('dataFiles/users.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                if row[0] == username:
                    return False
        return True
