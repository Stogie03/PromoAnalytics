'''
Created on Jul 12, 2016

@author: Adam
'''
#test
import numpy as np
import pandas as pd
from scipy.special import comb
from numpy import nonzero, where


class DataPrep(object):
    '''
    classdocs
    '''
    global stdColNames
    global limit
    stdColNames=np.array(['geography', 'date', 'revenue', 'gc', 'margin', 'holiday', 'year', 'week_of_year', 'day_of_year', 'quarter', 'month', 'week_of_month', 'day_of_month', 'day_of_week', 'weekend'])
    limit=10
    
    def __init__(self,dataLocation, dataConn, dataConnType):

        self.dataLocation= dataLocation
        self.dataConn=dataConn
        self.dataConnType=dataConnType
        self.validateInputData()

    def getDataFrame(self):
        if self.dataConnType=='CSV':
            try:
                self.df= pd.read_csv(self.dataLocation)
            except NameError:
                print "Error in reading in the CSV"
        if self.dataConnType=='DB':
            a=6   #THIS NEEDS TO BE FILLED IN LATER
        
        if self.dataConnType=='Hadoop':
            a=6 #THIS NEEDS TO BE FILLED IN LATER
            #insert Hadoop/Pysprk Connection code here

    def validateInputData(self):
        
        self.getDataFrame()
        
        #check if dataframe -> df exists
        df_exists = 'self.df' in locals() or 'self.df' in globals()
        try:
            self.df
        except NameError:
            df_exists=False
        else:
            df_exists=True
            
        if df_exists==True:
            df_names= self.df.columns.values
        else:
            print("There was an error loading the Data frame")
            
        #test the non promo column names
        if df_exists==True:
            
            if (np.array_equal(stdColNames,df_names[0:15])):    #need to fix this as it errors out
                stColNamesPass=True
            else:
                stColNamesPass=False
            
            #test the number of promo columns
            
            df_pnames=df_names[15:df_names.size]  #get the promo columns from the dataframe
            possibleValues=np.zeros((limit,limit))
            
            for x in range(1,limit):
            
                for z in range(1,limit):
                    if z<2 and x < 2:
                       possibleValues[x,z] = int(comb(z,1,exact=False)) 
                    if z >= 2 and z >= x:
                        possibleValues[x,z] = int(possibleValues[x-1,z] + comb(z,x,exact=False))
                       
            if df_pnames.size in possibleValues[:, :]:
                print ("VALUE FOUND")
                print df_pnames.size
                possiblePromoFormat=self.returnIndex2DArray(possibleValues, df_pnames.size)
                print possiblePromoFormat
            else:
                print ("VALUE NOT FOUND. Promos not set up correctly in input file")
                print df_pnames.size
                    
            #print df_pnames
            #print df_names
            #print possibleValues
            self.findSoloPromos(df_pnames, possiblePromoFormat)
            print ('Do the standard variables pass? %s' % (stColNamesPass))
        
        #this is the boolean to say the validation passed
        objInitDataVal = True
        
    def returnIndex2DArray(self,ArrayName,searchVal):
        arrayIndices=[[0,0]]
        for idx, val in enumerate(ArrayName):
          
            if searchVal in val[:]:
                for idx2, val2 in enumerate(val):
                    if val2==searchVal:
                        arrayIndices.insert(0,[idx,idx2])
        return arrayIndices
                
    def findSoloPromos(self,columnNames, arrayIndex):  
        
        for element in arrayIndex:
            if element !=[0,0]:
                singlePromoList=[]
                numPromo=element[1]
                pCombinations=element[0]
                print ("number of promos:%d and the possible combinations:%d" % (numPromo,pCombinations))
                for i in range(1,numPromo+1):
                    singlePromoList.append('p'+str(i))
                singlePromoPass=False
                falseMatch=False
                #Test to see if the single P columns in the file match what is expected
                try:
                    singlePromoPass=(singlePromoList[0:(numPromo)]==columnNames[0:(numPromo)].tolist())
                except NameError:
                    print ("Fail in single promo comparison")
                if singlePromoPass==True:
                    print ('Promo+1= %d' % (numPromo+1))
                    if columnNames[numPromo]==['p' + str(numPromo+1)]:
                        falseMatch=True
                    print ('FalseMatch= %s columnName= %s' % (falseMatch, columnNames[numPromo]))    
                print ('The file values: %s' % (columnNames[0:(numPromo)].tolist()))
                print ('singlePromoPass: %s' % (singlePromoPass))
                    
#TEST THE CLASS here
testClass=DataPrep('C:\Users\\astokes\Desktop\Analytic Solutions\mldata_2012_to_2016.csv',None,'CSV')    

'''
for idx, val in enumerate(possibleValues):
    if 3 in val[:]:
        for idx2, val2 in enumerate(val):
            if val2==3:
                print(idx,idx2)

    #ALL Functions below here will probably be part of another package/class
    def formatTS(self,inpu_df):
        a=6
        #insert code to format raw input data into the time series format requires for Dave's TS model
        #should return some sort of data frame object

    def formatML(self,input_df):
        a=6
        #insert code to format raw input data into the Machine Learning format required for non-TS modeling
        #should return some sort of data frame object

    def seasonalDecomposition(self,df_timeSeries):
        ts_dataframe=self.formatTS(df_timeSeries)
        #This is where the code for Dave's seasonal decomp model would go
        #This would create several objects for the PromoAnalytics Class - Seasonality, Trend, baseline

    def SeasDecompFcst(self,seas,trend,baseline,fcstStart, fcstEnd, PromoInfoDataFrame):
        #build a forecast by piecing together the components of the seasonalDecomposition() method
        #PromoInfoDataFrame would be the promotion information that would be used to assign some type of lift
    '''
