window.addEventListener("DOMContentLoaded", function () {
  var taskDeadline = document.getElementById("taskDeadline");
  var taskInput = document.getElementById("taskInput");
  var addButton = document.getElementById("addButton");
  var taskList = document.getElementById("taskList");
 

  addButton.addEventListener("click", function () {
    
    var task = new Array(taskDeadline.value,taskInput.value);
    "var deadline = taskDeadline.value;"

    if (task) {
      addTaskToList(task);
      taskDeadline.value = "";
      taskInput.value = "";
    }
  });

  function addTaskToList(task) {

    var data = {
      deadline: task[0],
      task: task[1]
    };
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "Example.py/process_data", true);
    xhr.setRequestHeader("Content-Type", "application/json");

   xhr.onreadystatechange = function () {
     if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
       var response = JSON.parse(xhr.responseText);
       console.log(response);
     }
   };

   xhr.send(JSON.stringify(data));

    var li = document.createElement("li");
    li.textContent = task;

    li.addEventListener("click", function () {
      li.classList.toggle("completed");
    });

    taskList.appendChild(li);
  }
});

