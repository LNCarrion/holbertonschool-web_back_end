export default function getStudentsByLocation(students, city){
  return students.filter(student.location === city);
}