function myFunction() {
  // Declare variables
  var input, filter, table, row, courseName, courseID, i, courseTxtValue, idTxtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("course_list_table");
  row = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < row.length; i++) {
    courseName = row[i].getElementsByTagName("td")[1];
    courseID = row[i].getElementsByTagName("td")[2];
    if (courseName) {
      courseTxtValue = courseName.textContent || courseName.innerText;
      idTxtValue = courseID.textContent || courseID.innerText;
      if (courseTxtValue.toUpperCase().indexOf(filter) > -1 || idTxtValue.toUpperCase().indexOf(filter) > -1) {
        row[i].style.display = "";
      } else {
        row[i].style.display = "none";
      }
    }
  }
}

let toggle1 = button => {
            let tableElement = document.getElementById("course_table");
            let takenCoursesTableElement = document.getElementById("taken_courses_table_merge");
            let formElement = document.getElementById("myform");

            let hidden = tableElement.getAttribute("hidden");
            formElement.setAttribute("hidden", "hidden");
            takenCoursesTableElement.setAttribute("hidden", "hidden");

            if (hidden) {
                tableElement.removeAttribute("hidden");
            } /*else {
               tableElement.setAttribute("hidden", "hidden");
              }*/
        }

        let toggle2 = button => {
            let tableElement = document.getElementById("course_table");
            let takenCoursesTableElement = document.getElementById("taken_courses_table_merge");
            let formElement = document.getElementById("myform");

            let hidden = formElement.getAttribute("hidden");
            tableElement.setAttribute("hidden", "hidden");
            takenCoursesTableElement.setAttribute("hidden", "hidden");

            if (hidden) {
                formElement.removeAttribute("hidden");
            } /*else {
               formElement.setAttribute("hidden", "hidden");
               }*/
        }

        let toggle3 = button => {
            let tableElement = document.getElementById("course_table");
            let takenCoursesTableElement = document.getElementById("taken_courses_table_merge");
            let formElement = document.getElementById("myform");

            let hidden = takenCoursesTableElement.getAttribute("hidden");
            tableElement.setAttribute("hidden", "hidden");
            formElement.setAttribute("hidden", "hidden");

            if (hidden) {
                takenCoursesTableElement.removeAttribute("hidden");
            } /*else {
             formElement.setAttribute("hidden", "hidden");
            }*/
        }