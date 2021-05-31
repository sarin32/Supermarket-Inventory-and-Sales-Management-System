import csv


# noinspection PyMethodMayBeStatic
class Categories:
    def getCategoriesData(self, c_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/categories.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if c_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [c_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getCategoryId(self, category):
        """
        :returns category id of specified category
        :type category: str
        """
        if category is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == category:
                        return row[0]

    def getCategoryName(self, catId):
        if catId is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == catId:
                        return row[1]

    def addCategory(self, category):
        with open('dataFiles/categories.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/categories.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, category])

    def deleteCategory(self, c_id):
        lines = []
        with open('dataFiles/categories.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == c_id:
                    lines.remove(row)
        with open('dataFiles/categories.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def updateCategory(self, c_id, new_name):
        lines = []
        with open('dataFiles/categories.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == c_id:
                    lines[-1][1] = new_name
        with open('dataFiles/categories.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)
