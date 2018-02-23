# Huzzah!
### Goal
Provide distance measurement, temperature, humidity, and alerting for a [feather huzzah with Wifi](https://www.adafruit.com/product/2821) using [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview).
### Real Goal
Have a [whole house humidifier](http://a.co/2FSgxHa) at home. 
I keep forgetting to refill the damn thing with water. 
It uses about 2 gallons of water a day during dry months, and runs dry constantly.
It also is very poor at detecting the humidity. 
Maybe because the sensor is built into the unit and therefore is too close to get a realistic sample?
* want to be able to read settings (like water level) from the humidifier and be able to remotely start and stop it 
* some machine learning, metrics, and alerting 
* the fan on the humidifier has a variable speed fan, so let's play with that as well
* save my sanity and probably marriage....it has to be cheap
* as is the usual on all my home projects...manual control has to be enabled and take priority

##### What about IoT?
Good question....so that was my initial goal. With most of my home projects, I try to enable [AWS IoT](https://aws.amazon.com/iot/).
But the horsepower and memory constraints of the feather micro-controllers limits what can be run. 
AWS IoT uses server-side and client-side certs. Unfortunately the horsepower required to deal with the certs is too much (right now) for these size machines. 
I read that they are working on a version of MQTT that will support client side certs, but will have to wait on that one.

_That's enough for now._


