import time

class SmartDevice:
    def __init__(self, id, type, status):
        self.id = id
        self.type = type
        self.status = status
        self.trigger = None

    def turnOn(self):
        self.status = "on"

    def turnOff(self):
        self.status = "off"

    def schedule(self, time, command):
        def task():
            self.executeCommand(command)

        time.scheduler.schedule(at=time, do=task)

    def update(self):
        # Take the appropriate action based on the trigger.
        if isinstance(self.trigger, TemperatureTrigger) and self.trigger.evaluate():
            self.turnOff()

class Trigger:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()

class TemperatureTrigger(Trigger):
    def __init__(self, temperature):
        super().__init__()
        self.temperature = temperature

    def evaluate(self):
        # Get the current temperature.
        currentTemperature = getTemperature()

        # Return True if the current temperature is greater than or equal to the trigger temperature, False otherwise.
        return currentTemperature >= self.temperature

class SmartHomeSystem:
    def __init__(self):
        self.devices = []
        self.triggers = []

    def executeCommand(self, command):
        # Split the command into parts.
        commandParts = command.split("(")

        # Get the command name.
        commandName = commandParts[0]

        # Get the arguments for the command.
        commandArguments = []
        for i in range(1, len(commandParts) - 1):
            commandArguments.append(commandParts[i].split(")")[0])

        # Execute the command.
        if commandName == "turnOn":
            deviceId = int(commandArguments[0])
            self.devices[deviceId].turnOn()
        elif commandName == "turnOff":
            deviceId = int(commandArguments[0])
            self.devices[deviceId].turnOff()
        elif commandName == "schedule":
            deviceId = int(commandArguments[0])
            time = commandArguments[1]
            command = commandArguments[2]
            self.devices[deviceId].schedule(time, command)
        elif commandName == "addTrigger":
            triggerType = commandArguments[0]
            condition = commandArguments[1]
            action = commandArguments[2]
            self.addTrigger(triggerType, condition, action)
        elif commandName == "removeTrigger":
            triggerType = commandArguments[0]
            self.removeTrigger(triggerType)
        elif commandName == "viewStatus":
            for device in self.devices:
                print(f"{device.type} {device.id} is {device.status}.")
        else:
            print("Invalid command.")

    def addDevice(self, device):
        self.devices.append(device)

    def removeDevice(self, device):
        self.devices.remove(device)

    def addTrigger(self, triggerType, condition, action):
        trigger = Trigger()
        trigger.condition = condition
        trigger.action = action

        if triggerType == "temperature":
            trigger = TemperatureTrigger(float(condition))

        self.triggers.append(trigger)

        for device in self.devices:
            device.trigger = trigger

    def removeTrigger(self, triggerType):
        for trigger in self.triggers:
            if triggerType == trigger.type:
                self.triggers.remove(trigger)
                break

        for device in self.devices:
            device.trigger = None
    
def takeInputs():
    """Takes inputs from the user and parses them into commands."""

    print("Smart Home System Menu")
    print("1. Turn on/off a device")
    print("2. Schedule a device to turn on/off at a particular time")
    print("3. Add a trigger")
    print("4. Remove a trigger")
    print("5. View the status of all devices")

    userChoice = int(input("Enter your choice: "))

    # Parse the user's choice into a command.
    if userChoice == 1:
        deviceId = int(input("Enter the ID of the device to turn on/off: "))
        command = "turnOn({})".format(deviceId)
    elif userChoice == 2:
        deviceId = int(input("Enter the ID of the device to schedule: "))
        time = input("Enter the time to schedule the device: ")
        command = "schedule({}, '{}', 'turnOn({})')".format(
            deviceId, time, deviceId)
    elif userChoice == 3:
        triggerType = input("Enter the type of trigger: ")
        condition = input("Enter the condition for the trigger: ")
        action = input("Enter the action for the trigger: ")
        command = "addTrigger('{}', '{}', '{}')".format(
            triggerType, condition, action)
    elif userChoice == 4:
        triggerType = input("Enter the type of trigger to remove: ")
        command = "removeTrigger('{}')".format(triggerType)
    elif userChoice == 5:
        command = "viewStatus()"
    else:
        print("Invalid choice.")
        return command

    # Execute the command.
command = takeInputs()
SmartHomeSystem.executeCommand(command)



