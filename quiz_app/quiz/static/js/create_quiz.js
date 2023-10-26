let addBtn = document.querySelector(".addBtn");
let question_box = document.querySelector('.question_box');
let questions_container = document.querySelector('.questions__container');
let question_no = 1

addBtn.addEventListener("click", () => {
  let copy = question_box.cloneNode(true);
  copy.querySelectorAll("input[type='text']").forEach(element => {
    element.value='';
  });
  question_no++;
  copy.querySelectorAll("input[type='radio']").forEach(element => {
    element.name = `correct-${question_no}`;
    element.checked = false;
  });
  questions_container.appendChild(copy);
});
