let addBtn = document?.querySelector(".addBtn");
let submitBtn = document?.querySelector('.submit');

let form = document.querySelector('.create_form');
let question_box = document.querySelector('.question_box');
let form_data_input = document.querySelector('.data');

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

submitBtn.addEventListener('click', (event)=>{
    event.preventDefault();
    data = []
    Array.from(questions_container.children).forEach(
        (question_box) => {
            let question_data = {}
            question_data['text'] = question_box.querySelector('.question').value;
            data.push(question_data);

            let options = [];
            question_box.querySelectorAll(".option").forEach(
                (option) => {
                    options.push(
                        {text:option.querySelector("input[type='text']").value, isCorrect:option.querySelector("input[type='radio']").checked}
                        
                    )
                }
            );
            question_data['options'] = options;
        }
    )
    let stringified_data = JSON.stringify(data);
    form_data_input.value = stringified_data;
    form.submit();

})