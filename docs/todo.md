Add manual override pseudocode for Later
```
previous is equal to the display brightness set in the last interval
if previous does not match current brightness:
    # brightness changed due to external input

    if current is above previous:
        # brightness was manually increased
        expect increase (1)

    if current is below previous:
        # brightness was manually decreased
        expect decrease (-1)
```