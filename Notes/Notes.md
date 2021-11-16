
# Suggestions
* Consider putting the webcam capture mechanism in a function
# Known Issues
* "time.sleep" causes program to freeze and be unable to close
  * Could potentially be solved by comparing time from previous timeout or using the "timeit" module rather than using "time.sleep"
  * Threading could solve this issue

* Average is unreliable for getting the brightness
  * Needs a bias towards extreme values
    * Histogram Approach
  * Geometric Mean?