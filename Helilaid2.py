class myClass():
  def method1(self):
      print("Daniil")
        
  def method2(self,someString):    
      print("Helilaid")
  
      
def main():           
  # exercise the class methods
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")
  
if __name__== "__main__":
  main()