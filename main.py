#!/usr/local/bin/python3

from sys import argv
import cal_course_alerts

def main():
  if len(argv) < 3:
    email = input("Email: ")
    courses = input("List course id separated by comma: ")
  else:
    email = argv[1]
    courses = argv[2]

  cal_course_alerts.alert(email, courses)

if __name__ == '__main__':
  main()
