window.onload = function init() {
    let buttonID = "1-holder";
    let textID = "1";

    if (localStorage.clickedButton != "0") {
        buttonID = localStorage.clickedButton + "-holder";
        textID = localStorage.clickedButton;
    }

    button = document.getElementById(buttonID);
    text = document.getElementById(textID);
    button.style.backgroundColor = "#db1430";
    text.style.color = "#fff";

    localStorage.clickedButton = "0";
}

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

function clicked(button)
{
    localStorage.clickedButton = button.id;

    if (storageAvailable('localStorage')) {
      console.log("storage works");
    }
    else {
      console.log("storage dows not work");
    }
    console.log("clicked");
}

function storageAvailable(type) {
    let storage;
    try {
        storage = window[type];
        const x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch (e) {
        return e instanceof DOMException && (
            // everything except Firefox
            e.code === 22 ||
            // Firefox
            e.code === 1014 ||
            // test name field too, because code might not be present
            // everything except Firefox
            e.name === 'QuotaExceededError' ||
            // Firefox
            e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
            // acknowledge QuotaExceededError only if there's something already stored
            (storage && storage.length !== 0);
    }
}

function filterToDo() {
  // Declare variables
  var input, filter, table, row, courseName, courseID, i, courseTxtValue, idTxtValue;
  input = document.getElementById("filter_input");
  filter = input.value.toUpperCase();
  table = document.getElementById("filtered_list");
  row = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < row.length; i++) {
    courseName = row[i].getElementsByTagName("td")[0];
    courseID = row[i].getElementsByTagName("td")[1];
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