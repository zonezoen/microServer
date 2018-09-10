struct Student{
1: string name,
2: string age
}
    service UserService{
     void addStu(1: Student stu),
     Student getStu(1: string name)
}

