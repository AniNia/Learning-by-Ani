function Student() {
    this.firstName = " ";
    this.lastName = " ";
    this.class=" ";
}

var student = new Student();
student.firstName = "Ani";
student.lastName = "Mishra";
student.class = 10;
console.log(student.firstName + " " + student.lastName +" And her class is "+ student.class);
