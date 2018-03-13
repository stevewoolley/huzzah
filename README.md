## Goal
Enable ESP8266/ESP8285 devices using MicroPython to play on the AWS IoT platform.

##### Problems connecting to AWS IoT?
The horsepower and memory constraints of the feather micro-controllers limits what can be run. 
AWS IoT uses server-side and client-side certs. Unfortunately the horsepower required to deal with the certs is too much (right now) for these size machines. 
So will have to follow another path to use AWS IoT.

## Sub Projects
### Whole house humidifier
Purchased: [Whole house humidifier](http://a.co/2FSgxHa) 

I keep forgetting to refill the damn thing with water. 
It uses about 2 gallons of water a day during dry months, and runs dry constantly.
It also is very poor at detecting the humidity. 
Maybe because the sensor is built into the unit and therefore is too close to get a realistic sample?
* want to be able to read settings (like water level) from the humidifier and be able to remotely start and stop it 
* some machine learning, metrics, and alerting 
* the fan on the humidifier has a variable speed fan, so let's play with that as well
* save my sanity and probably marriage....it has to be cheap
* as is the usual on all my home projects...manual control has to be enabled and take priority

## Connecting MicroControllers
* [Install ESP8266 Hardware](ESP8266.md) (Examples: Feather Huzzah, HiLetgo ESP8266 NodeMCU, etc.)
* [Install ESP8285 Hardware](ESP8285.md) (Examples: Wemos D1 Mini, etc.)
