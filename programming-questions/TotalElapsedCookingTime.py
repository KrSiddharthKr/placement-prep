numberOfLayers = int(input())
totalTimeCooking = int(input())

if ((1<=numberOfLayers)<=20) and ((0<=totalTimeCooking)<=40):
    total_time = (numberOfLayers*2) + totalTimeCooking
    print(total_time)