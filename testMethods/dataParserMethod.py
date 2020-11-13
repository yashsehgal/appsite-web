# testing data parsing methods and functions

import uuid

datasetForUniqueID = []

def generateNewUniqueID():
  return uuid.uuid1()

sampleDataset = {
  "id": "{}".format(generateNewUniqueID()),
  
  "componentName": "HeaderCleanComponent_CleanShadow_01",
  "componentID": "kjfhij-vfbgf987veru8-vfnvjnf",
  
  "componentProperties": {
    "logo": "assets/pathname/filename.png",
    "headerOptions": {
      "options": {
        "home": "/index.htm",
        "about_us": "/about.htm",
        "help": "/help.htm",
        "contact": "/contact.htm",
        "download": "https://randomSiteName.someDomainID/someRandomUniqueAddress/downloadLink/demoFile.zip"
      }
    }
  }
}

metaPropertiesData = {
  "metaProperties": {
    "componentID": None,
    "componentAvailability": None,
    "componentType": None,
    "componentName": None,
    "componentProperties": None,
  }
}

class TestMethodsToCheckComponentDataProperties:
  def __init__(self):
    self.sampleDataObject = []
    
  def checkComponentProperties(self):
    self.sampleDataObject.append(sampleDataset)
    # print(self.sampleDataObject)
    
    for keyObject, valueObject in sampleDataset.items():
      print(keyObject, ':', valueObject)
      
    self.sampleDataObject.clear()


if __name__ == "__main__":
  testMethodsToCheckComponentDataProperties = TestMethodsToCheckComponentDataProperties()
  testMethodsToCheckComponentDataProperties.checkComponentProperties()