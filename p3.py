def print_student_info(**kwargs):
  if not kwargs:
      print("Немає інформації про студента")
  else:
      for key, value in kwargs.items():
          up_key = key.capitalize()
          print(f"{up_key}: {value}")

if __name__ == '__main__':
        print_student_info(name="Ярослав", age=17, course=3, group="КІПЗс-22-3")
        print_student_info()