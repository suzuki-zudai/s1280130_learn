class heatMapItemsFrequencies():
  """
   To show the heat map by using the dictionary.
  """
  def __init___(self,dic):
    """
    dic:dictionary
      To store the point as key and how many time is it in data as value
    fd:pandas dataframe
      To store the location(lat,lon) and count  
    """
    dic=dic
    fd="None"
    self.getCountDataset()
    self.showFigure()
  def getCountDataset(self):
            """
            make dataset has location and how many time it is in dataset
            """
            ##make fd to store the location.
            self.fd=pd.DataFrame(columns=['Lat', 'Lon',"num"])
            ## get the location from dataset[Location] and separate to lat and lon
            for loc ,count in self.dic.items():
                loc=loc.replace("POINT(",'')
                loc=loc.replace(")",'')
                loc=loc.split(' ')
                lat=loc[0]
                lon=loc[1]
                self.fd.loc[fd.shape[0]] =[lon,lat,count]
    
  def showFigure(self):
    """
    To show the figure by using pandas dataframe
    """
        fig = px.density_mapbox(df, lat = 'Lat', lon = 'Lon', z = 'num',
                        radius = 8,
                        center = dict(lat = 37.51, lon =139.89),
                        zoom = 3,
                        mapbox_style = 'open-street-map')
        fig.show()
  
