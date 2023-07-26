from tools.venmo_tools import monthlyRequest

if __name__=='__main__':
    monthMessage = input('Enter Month: ')
    include = bool(input('Include Yourself? (True/False): '))
    monthlyRequest(monthMessage, include, term=True)