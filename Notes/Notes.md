
# Suggestions
* Consider putting the webcam capture mechanism in a function
# Known Issues
* "time.sleep" causes program to freeze and be unable to close
  * Could potentially be solved by comparing time from previous timeout or using the "timeit" module rather than using "time.sleep"
  * Threading

* Average is unreliable for getting the brightness
  * Needs a bias towards extreme values
    * Histogram Approach
  * Geometric Mean

* Need to find a way for the program to keep getting webcam data while waiting for the display brightness change to finish before calling the function again
  * Async Functions
  * Threading