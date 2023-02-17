def numToMonth(num): #helper function
    numMonth = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }
    try:
        return numMonth[num]
    except:
        print("No Month with that Index")

def largestRainfall(months):
    max = months[0]
    month = 0
    for i in range(len(months)):
        if months[i] > max:
            max = months[i]
            month = i

    return(numToMonth(month), max)

def smallestRainfall(months):
    min = months[0]
    month = 0
    for i in range(len(months)):
        if months[i] < min:
            min = months[i]
            month = i

    return(numToMonth(month), min)

def meanRain(months):
    sum = 0
    for i in months:
        sum += i
    return (sum / len(months)) * 2.54

def largerThanMean(months):
    mean = (meanRain(months)) / 2.54
    count = 0
    for i in months:
        if i > mean:
            count+= 1
    return count

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range((len(list)-i)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list







testList = [
        133.5,
        64.3,
        104.4,
        86.3,
        48.5,
        35.4,
        55.3,
        84.9,
        104.5,
        104.4,
        122.6,
        119.5
    ]

print(smallestRainfall(testList))
print(largestRainfall(testList))
print(meanRain(testList))
print(largerThanMean(testList))
print(bubbleSort(testList))

    


    
