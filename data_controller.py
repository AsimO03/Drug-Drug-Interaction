import csv

class DataController():
    def __init__(self, csvPath):
        # read in the csv file into a list (takes a little bit to do ~20sec in tests)
        self.csv_data = []
        with open(csvPath, "r") as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter="\t")
            next(csv_reader)
            for row in csv_reader:
                self.csv_data.append(row)
        print("CSV lines parsed:", len(self.csv_data))


    def findDrugInteractionsByTwo(self, drug1, drug2):
        # find interactions in the list where either object or precipitant are the two drugs
        return [entry for entry in self.csv_data if (entry['object'] == drug1 and entry['precipitant'] == drug2) or \
                                                    entry['precipitant'] == drug1 and entry['object'] == drug2]

    def find_drug_interactions_by_list(self, drug_list):
        # try every combination of the drugs in drug_list using findDrugInteractionsByTwo()
        return_list = []
        for i in range(len(drug_list)):
            for j in range(i + 1, len(drug_list)):
                return_list.extend(self.findDrugInteractionsByTwo(drug_list[i], drug_list[j]))
        return return_list
        
    

    
    