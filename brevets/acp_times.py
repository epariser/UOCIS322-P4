"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


speed_table = [(200, 15, 34),
               (200, 15, 32),
               (200, 15, 30),
               (400, 11.428, 28)]
               #(control location, Max Speed, Min Speed)


def calc_time(control_dist_km, open):
   
   index = 1 # 1 if open 2 if closed
   if open:
      index = 2

   time = 0
   for i in range(len(speed_table)):
      speed = speed_table[i][index]
      control_location = speed_table[i][0]
      if control_dist_km >= control_location:
         time += control_location/speed
         control_dist_km -= control_location
      else:
         time += control_dist_km/speed

   return time


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  A date object (arrow)
   Returns:
      A date object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """
   if control_dist_km > brevet_dist_km:
       control_dist_km = brevet_dist_km
   
   if control_dist_km > 1000:
      return

   time = calc_time(control_dist_km, True)
   timeM = int(round((time % 1) * 60))
   timeH = math.floor(time)

   opening_time = brevet_start_time.shift(hours=+timeH, minutes=+timeM)
    
   return opening_time



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  A date object (arrow)
   Returns:
      A date object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km
   
   if control_dist_km > 1000:
      return
    
   if control_dist_km <= 60:
      time = control_dist_km/20 + 1
   else:
      time = calc_time(control_dist_km, False)
   timeM = int(round((time % 1) * 60))
   timeH = math.floor(time)

   opening_time = brevet_start_time.shift(hours=+timeH, minutes=+timeM)
    
   return opening_time

def main():
   control_dist = 60
   brevet_dist = 200
   brevet_start = arrow.get('2013-01-01 00:00')
   print(brevet_start)
   print(open_time(control_dist, brevet_dist, brevet_start))
   print(close_time(control_dist, brevet_dist, brevet_start))
   print(calc_time(control_dist, True))
   print(calc_time(control_dist, False))

main()


