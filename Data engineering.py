    feature_vector_df['time'] = pd.to_datetime(feature_vector_df['time'])
    feature_vector_df['time'] = pd.to_datetime(feature_vector_df['time'])
    feature_vector_df['time'] = pd.to_datetime(feature_vector_df['time'])

    feature_vector_df['Year'] = feature_vector_df['time'].dt.year
    feature_vector_df['Month'] = feature_vector_df['time'].dt.month
    feature_vector_df['Day'] = feature_vector_df['time'].dt.day
    feature_vector_df['Hour'] = feature_vector_df['time'].dt.hour
    feature_vector_df['Minute'] = feature_vector_df['time'].dt.minute
    feature_vector_df['Second'] = feature_vector_df['time'].dt.second

    # replacing null values with median
    feature_vector_df['Valencia_pressure'] = feature_vector_df['Valencia_pressure'].fillna(feature_vector_df['Valencia_pressure'].median())

    # Changing Object dtypes to int
    feature_vector_df['Valencia_wind_deg_level']=feature_vector_df.Valencia_wind_deg.map({'level_5':5, 'level_10':10, 'level_9':9, 'level_8':8, 
                                                                    'level_7':7, 'level_6':6, 'level_4':4, 'level_3':3, 
                                                                    'level_1':1, 'level_2':2})


    feature_vector_df['Seville_pressure_category']=feature_vector_df.Seville_pressure.map({'sp25':25, 'sp23':23, 'sp24':24, 'sp21':21, 'sp16':16, 'sp9':9, 'sp15':15, 'sp19':19, 'sp22':22, 'sp11':11,
                                                                     'sp8':8, 'sp4':4, 'sp6':6, 'sp13':13, 'sp17':17, 'sp20':20, 'sp18':18, 'sp14':14, 'sp12':12, 'sp5':5, 'sp10':10,
                                                                     'sp7':7, 'sp3':3, 'sp2':2, 'sp1':1})

    feature_vector_df = feature_vector_df.drop(['Valencia_wind_deg','Seville_pressure', 'Barcelona_temp', 'Barcelona_temp_max', 'Barcelona_temp_min', 'Bilbao_temp', 'Bilbao_temp_max', 'Bilbao_temp_min', 'Madrid_temp', 'Madrid_temp_max', 'Madrid_temp_min', 'Seville_temp', 'Seville_temp_min', 'Valencia_temp', 'Valencia_temp_min','time'],axis=1)

    predict_vector = feature_vector_df