import csv


# noinspection PyMethodMayBeStatic
class Brands:
    def getBrandsData(self, b_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/brands.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if b_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [b_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getBrandId(self, brand):
        """
        :returns brand id of specified brand
        :type brand: str
        """
        if brand is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == brand:
                        return row[0]

    def getBrandName(self, brandId):
        """
        :returns brand name of specified brand
        :type brandId: str
        """
        if brandId is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == brandId:
                        return row[1]

    def addBrand(self, brand):
        with open('dataFiles/brands.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/brands.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, brand])

    def deleteBrand(self, b_id):
        lines = []
        with open('dataFiles/brands.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == b_id:
                    lines.remove(row)
        with open('dataFiles/brands.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def updateBrand(self, b_id, new_name):
        lines = []
        with open('dataFiles/brands.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == b_id:
                    lines[-1][1] = new_name
        with open('dataFiles/brands.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)
