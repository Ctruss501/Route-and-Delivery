# Corey Trussell, ID: 001366871

import loadDeliver
import readCSV
import datetime


def main():
    hashTable = readCSV.getHashTable()
    print('\033[1;4;36m' + 'Western Governors University Parcel Service' + '\033[0m')
    print('\n' + '\033[32m' + 'Select one of the following:' + '\033[0m')
    print('\033[1;35m' + '1) ' + '\033[0m' + 'View status and info of packages at a specified time.')
    print('\033[1;35m' + '2) ' + '\033[0m' + 'View total miles traveled by all trucks along with status and info of all packages at days '
                                             'end.')
    print('\033[1;35m' + '3) ' + '\033[0m' + 'Close.')
    selection = input('\n' + '\033[3;30;43m' + 'Below, type the number of your selection:' + '\033[0m')

    if selection == '1':
        trucks = (loadDeliver.loadTruckPacks())
        timeInput = input('Below, type the time ' + '\033[33m' '(hh:mm:ss)' '\033[0m' + ' for which you would like the status update:')
        try:
            (h, m, s) = timeInput.split(':')
        except ValueError:
            print('\n\n' + '\033[1;31;47m' + 'Please enter time in (hh:mm:ss) format.' + '\033[0m')
            return main()
        timeConvert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        loadDeliver.truckDeliverPackages(trucks, hashTable)
        print('Status of packages at ' + '\033[32m' + timeInput + '\033[0m')
        for i in range(1, 41):
            pack = hashTable.search(i)
            timeDelivered = pack.packDelivered
            timeToLeave = pack.toLeave
            if timeConvert < timeDelivered and timeConvert < timeToLeave:
                pack.packStatus = 'At the Hub'
            if timeDelivered > timeConvert >= timeToLeave:
                pack.packStatus = 'En Route'
            if timeConvert >= timeDelivered:
                pack.packStatus = 'Delivered'
            print(pack)

        print('\n' + 'What would you like to do next?')
        print('\033[1;35m' + '1) ' + '\033[0m' + 'Return to Main Menu')
        print('\033[1;35m' + '2) ' + '\033[0m' + 'Close.')
        selected = input('\n' + '\033[3;30;43m' + 'Below, type the number of your selection:' + '\033[0m')
        if selected == '1':
            main()
        elif selected == '2':
            quit()

    elif selection == '2':
        trucks = loadDeliver.loadTruckPacks()
        loadDeliver.truckDeliverPackages(trucks, hashTable)
        loadDeliver.report(trucks)
        print('\n' + 'What would you like to do next?')
        print('\033[1;35m' + '1) ' + '\033[0m' + 'Return to Main Menu')
        print('\033[1;35m' + '2) ' + '\033[0m' + 'Close.')
        selected = input('\n' + '\033[3;30;43m' + 'Below, type the number of your selection:' + '\033[0m')
        if selected == '1':
            main()
        elif selected == '2':
            quit()

    elif selection == '3':
        quit()

    elif selection != '1' or selection != '2' or selection != '3':
        print('\n\n' + '\033[1;31;47m' + 'Your selection must be either 1, 2, or 3.' + '\033[0m')
        main()


main()
