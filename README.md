# capstone
This was my capstone project for my college Computer Science degree. There were a lot of hours spent and a lot of lessons learned but I will try to explain everything in a way that makes sense. I apologize in advance for my wacky vernacular.

## The Concept
If a company has, lets say three lots of land. The company has two parking lots A and B, and one building. The building being where they make some high speed widgets. The company wants to know more information about the parking lots for future projects. Does parking lot A use 100% of the land designated to the parking lot? Can we repave part of the parking lot, allowing the workers to park in the remaining portions of the parking lot? What if we decide we want to repurpose the land for parking lot A entirely to make another widget factory, can parking lot B handle the extra traffic?

## The Separate Entities
### The Spot
The whole system comes down to two separate entities, the spot and the lot. The individual spot houses almost all of the information necessary for the whole project.
The spot houses:
      - Name: string for identification purposes (name stucture is "elevation-group-row-spot" ex: "1-1-1-21"),
      - isOpen: a boolean to see if the spot is currently in use (cannot track time used if we try to use a spot and it is already used),
      - start: a starting time (total time used is measure by taking the time now minus the time taken),
      - total time taken: for how used is a particular spot,
      - time taken per year: to measure efficiency by dividing the time taken by the time in a year,
      - time taken per month: same concept as the per year,
      - efficiency per month: the product of the math per month,
      - efficiency per year: the prdocut of the math per year

Given the analytics of getting the information per spot we can paint a bigger picture of a parking spots use. We can then find out if a parking spot has a spot that is taken less than three percent of the time. If a parking lot is a parking garage we can change the spot elevation to correspond to it's level.

### The Parking Lot
Now we have each spot and the information, we need a useful means to collect and iterate through them. We aren't going to shine a light on how long it took me to come up with a solid idea on how to do this. I settled on a dynamic list. We can store the spots as an object and then append the spot the the lot. Now it is a matter of iterating through the lot to get the information needed. Not to get too technical it can be boiled down to this in a function to output the time taken of the year of a certain spot: do a for loop, if query equals the spots name, output the spots time taken per year.

## Conclusion
The project was a monster of ideas colliding over and over again. I decided early on that I was going to do it in a new language I have never used, python. I started college with absolutely no programming knowledge, then college taught me C++. I learned everything needed for the project via google and youtube, and I loved every minute of it.
Another use case for the project was to use it for my Army buddies to track tool uses, I worked on helicopters in the Army. This project could be used by replacing the items that weren't used, to ask Uncle Sam to get more useful tools.

As always, I wish you the best.
