import socket

class Assignment2:
    
    def __init__(self, year):
        self.year = year
    
    def tellAge(self, currentYear):
        print(f"Your age is {currentYear - self.year}")
    
    def listAnniversaries(self):
        
        l = []
        curr_year = 2022
        diff = curr_year - self.year

        num_anniversaries = diff // 10

        for i in range(1, num_anniversaries + 1):
            l.append(i * 10)
        return l
    
    def modifyYear(self, n):
        final_str = ""
        first_two_chars = str(self.year)[:2]
        final_str = first_two_chars * n
        product_str = str(n * self.year)
        for i,num in enumerate(product_str):
            if (i + 1) % 2 == 1:
                final_str += num
        return final_str
    
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        
        if not string[0].islower():
            return False

        number_found = False

        for char in string:
            if char.isdigit():
                if number_found:
                    return False
                else:
                    number_found = True
        return True
    
    @staticmethod
    def connectTcp(host, port):
        try:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_obj.connect((host, port))
            return True
        except Exception as e:
            print(e)
            return False