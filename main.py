import os
import platform
import shutil

class LocalManageer:
  def __init__(self):
    if self.checkConfig():
      # 存在する時
      with open(os.getcwd()+"/config", "r") as f:
        configRaw = f.read()
    else:
      userName = os.getlogin()
      # if u use windows return "Windows"
      useOS = platform.system()
      if useOS == "Windows":
        defaultPath = "C:/Users/"+userName+"/AppData/Roaming/7DaysToDie/"
      elif useOS == "Mac":
        defaultPath = "C:/Users/"+userName+"/Application Support/Library/7DaysToDie/"
      self.savePath = defaultPath
      self.backupPath = os.getcwd()+"/backup"
    
    self.backupToSave("hoge")
  
  def backupToSave(self, saveFolderName):
    if os.path.isfile(self.savePath+"/"+saveFolderName):
      # 存在する
      print(saveFolderName+" is exist.\nRewrite the filder right?\nOK:0\nNO:1")
      rewriteOK = input()
      if int(rewriteOK):
        # NO
        pass
      else:
        # YES
        os.rmdir(self.savePath+"/"+saveFolderName)
        shutil.copytree(self.backupPath+"/"+saveFolderName, self.savePath+"/"+saveFolderName)
        
    else:
      # しない
      shutil.copytree(self.backupPath+"/"+saveFolderName, self.savePath+"/"+saveFolderName)
    
  def checkConfig(self):
    return os.path.isfile(os.getcwd()+"/config")
  
  def writer(self):
    # write savefile and config
    return 0

LL = LocalManageer()