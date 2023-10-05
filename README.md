# EI_assignment

Smart Home System Programming Exercise:

Problem Statement
Create a simulation for a Smart Home System that allows the user to control different smart devices such as lights, thermostats, and door locks via a central hub. The user should be able to set schedules, automate tasks, and view the status of each device.
Functional Requirements
1.
Initialize the Smart Home System with different devices, each having their own unique ID and type (light, thermostat, door lock).
2.
Implement features to:
Turn devices on/off
Schedule devices to turn on/off at a particular time
Automate tasks based on triggers (e.g., turning off lights when the thermostat reaches a certain temperature)
3.
Optional: Provide the ability to add or remove devices dynamically.
Key Focus
1.
Behavioral Pattern: Use the Observer Pattern to update all devices when a change occurs in the system.
2.
Creational Pattern: Use the Factory Method for creating instances of different smart devices.
3.
Structural Pattern: Use the Proxy Pattern to control access to the devices.
4.
OOP: Ensure strong encapsulation, modularity, and the application of inheritance and polymorphism.
Possible Inputs
Devices:
[{id: 1, type: 'light', status: 'off'}, {id: 2, type: 'thermostat', temperature: 70}, {id: 3, type: 'door', status: 'locked'}]
Commands:
['turnOn(1)', 'setSchedule(2, "06:00", "Turn On")', 'addTrigger("temperature", ">", 75, "turnOff(1)")']
Possible Outputs
Status Report:
"Light 1 is On. Thermostat is set to 70 degrees. Door is Locked."
Scheduled Tasks:
"[{device: 2, time: "06:00", command: "Turn On"}]"
Automated Triggers:
"[{condition: "temperature > 75", action: "turnOff(1)"}]"
