"""
Classes for I/O

writer and reader

Author: vddoan
24/05/2012

"""

class Writer(object):
    def __init__(self,file_name):
        self.file_name = file_name

    def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

    def transforme_to_csv(self):
        
        
    def write_to_csv(self,csv_filename):
        with open(csv_filename,'w') as f:
          f.write(self.transforme_to_csv())

    def write_to_xls(self,xls_filename,sheet_name):
        """ Create a new workbook object """
        rb = xlrd.open_workbook(xls_filename,formatting_info=True)
        workbook = copy(rb) #a writable copy (I can't read values out of this, only write to it)

        ''' get all sheetnames '''
        list_of_sheetnames = []
        list_of_sheetnames = rb.sheet_names()
        ''' make a set of sheetnames without duplication '''
        sheet_names = set(list_of_sheetnames)
        ''' verify if a given ticker existed or not '''
        if (sheet_name in sheetnames) == True:
          flag = True
        else:
          flag = False

        if flag == True:
          print "The data sheet named " + ticker_name + " existed."
        else:
          print "No data sheet named " + ticker_name + ", created new"
          w_sheet = workbook.add_sheet(ticker_name)
          w_sheet.write(0,0,'Eod_C_Action')
          w_sheet.write(0,1,'Eod_I_Version')
          w_sheet.write(0,2,'UsrId')
          w_sheet.write(0,3,'Eod_D_Creation')
          w_sheet.write(0,4,'Eod_D_Quote')
          w_sheet.write(0,5,'InsId')
          w_sheet.write(0,6,'Eod_I_ProviderId')
          w_sheet.write(0,7,'Eod_N_Open')
          w_sheet.write(0,8,'Eod_N_High')
          w_sheet.write(0,9,'Eod_N_Low')
          w_sheet.write(0,10,'Eod_N_Close')
          w_sheet.write(0,11,'Eod_I_Volume')
    
          for row_index in range(1,len(self.close)+1):
              w_sheet.write(row_index,0,'A')
              w_sheet.write(row_index,1,0)
              w_sheet.write(row_index,2,8)
              w_sheet.write(row_index,3,datetime.datetime.now().strftime('%Y-%m-%d'))
              w_sheet.write(row_index,4,self.date[row_index-1].strftime('%Y-%m-%d'))
              w_sheet.write(row_index,5,1)
              w_sheet.write(row_index,6,1)
              w_sheet.write(row_index,7,self.open_[row_index-1])
              w_sheet.write(row_index,8,self.high[row_index-1])
              w_sheet.write(row_index,9,self.low[row_index-1])
              w_sheet.write(row_index,10,self.close[row_index-1])
              w_sheet.write(row_index,11,self.volume[row_index-1])

        workbook.save(xls_filename)

        
    
class Reader:
    def __init__(self,file_name):
        self.file_name = file_name
