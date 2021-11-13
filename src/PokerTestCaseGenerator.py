import random
test_cases_count = int(input("How many test cases do you want to generate?"))
cards = {2: "S2", 3: "S3", 4: "S4", 5: "S5", 6: "S6", 7: "S7", 8: "S8", 9: "S9", 10: "S10", 11: "SJ", 12: "SQ",
         13: "SK", 14: "SA",
         22: "C2", 23: "C3", 24: "C4", 25: "C5", 26: "C6", 27: "C7", 28: "C8", 29: "C9", 30: "C10", 31: "CJ", 32: "CQ",
         33: "CK", 34: "CA",
         42: "H2", 43: "H3", 44: "H4", 45: "H5", 46: "H6", 47: "H7", 48: "H8", 49: "H9", 50: "H10", 51: "HJ", 52: "HQ",
         53: "HK", 54: "HA",
         62: "D2", 63: "D3", 64: "D4", 65: "D5", 66: "D6", 67: "D7", 68: "D8", 69: "D9", 70: "D10", 71: "DJ", 72: "DQ",
         73: "DK", 74: "DA"}
for x in range(test_cases_count):

