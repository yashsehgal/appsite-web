code = (
  '<p id="title">Text</p>'
)

codeProperties = {
  "codeLength": 0,
  "innerHTML": {
    "parentTag": '',
    "childTag": '',
    "TagData": '',
    "tagID": '',
    "tagClass": [],
    "tagIsValid": ''
  }
}

class RunTestCaseToCheckParsingMethods:
  def __init__(self):
    self.checkCodeProperties()
  
  def checkCodeProperties(self):
    self.code = code
    
    if self.code != None:
      self.codeLength = 0
      self.innerHTML = {}
      self.parentTag = ''
      self.childTag = '' 
      self.TagData = '' 
      self.tagID = '' 
      self.tagClass = ''
      self.tagIsValid = False
      self.tagID = ''
      for text in code:
        if self.code != None:
          # codeProperties.get('codeLength').update(len(self.code))
          codeProperties.setdefault('codeLength', len(self.code))
        if code[0] == '<' and code[-1] == '>':
          self.parentTag = code[1]
          self.childTag = None
          for count in range(len(code)):
            if code[count] == '>' or code[count] == '</':
              self.TagData.join(code[count])
            
          if "id" in code:
            pointHandler = code.find("id")
            for count in range(len(code)):
              if count == pointHandler and code[count+1] == "=" and code[count+2] != None and code[count] != '>':
                self.tagID.join(code[count])

              
          # codeProperties.get('innerHTML').get('parentTag').update(self.parentTag)
          codeProperties.setdefault('parentTag', self.parentTag)
          # codeProperties.get('innerHTML').get('childTag').update(self.childTag)
          codeProperties.setdefault('childTag', self.childTag)
          # codeProperties.get('innerHTML').get('TagData').update(self.TagData)
          codeProperties.setdefault('TagData', self.tagID)
      
if __name__ == '__main__':
  runTestCaseToCheckParsingMethods = RunTestCaseToCheckParsingMethods()