function filterTable() {
  // Declare variables
  var input, filter, table, row, courseName, courseID, i, courseTxtValue, idTxtValue;
  input = document.getElementById("filter_input");
  filter = input.value.toUpperCase();
  table = document.getElementById("filtered_list");
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

function toggleButtons(button, count) {
    let button_id = button.id;
    let element;
    let hidden;

    for ( let id = 1; id <= count; id++ )
    {
        element = document.getElementById("toggle-element-" + id.toString());
        hidden = element.getAttribute("hidden");

        if ( id.toString() == button_id )
            element.removeAttribute("hidden");
        else
            element.setAttribute("hidden", "hidden");
    }
    console.log(button_id);
}