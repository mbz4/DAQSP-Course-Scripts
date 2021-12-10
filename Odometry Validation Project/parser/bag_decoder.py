import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

b = bagreader('optitrack_data_playground_2.bag')

#s = b.std_data()
#data = pd.read_csv(s[0])

odom = b.odometry_data()
odomdata = pd.read_csv(odom[0])

b.plot_odometry()

# replace topic name as per need

#LASER_MSG = b.message_by_topic('/vehicle/front_laser_points')

#LASER_MSG

#df_laser = pd.read_csv(LASER_MSG)

#df_laser

