'''
Created on Jul 12, 2016

@author: Adam
'''
import numpy
import pandas as pd


class DataPrep(object):
    '''
    classdocs
    '''

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
            a=6
        
        if self.dataConnType=='Hadoop':
            a=6
            #insert Hadoop/Pysprk Connection code here

    def validateInputData(self):
        self.getDataFrame()
        stdColNames=['geography' 'date' 'revenue' 'gc' 'margin' 'holiday' 'year' 'week_of_year' 'day_of_year' 'quarter' 'month' 'week_of_month' 'day_of_month' 'day_of_week' 'weekend']
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
        print self.df.columns.values  
        
        #test the non promo column names
        if stdColNames==df_names:    #need to fix this as it errors out
            stColNamesPass=True
        else:
            stColNamesPass=False
        print(stdColNames)
        #this is the boolean to say the validation passed
        objInitDataVal = True
            
    
#TEST THE CLASS
testClass=DataPrep('C:\Users\Adam\Downloads\mldata_2012_to_2016.csv',None,'CSV')    

'''
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