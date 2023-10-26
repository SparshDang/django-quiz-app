let questions_box = document.querySelectorAll(".question");

let subBtn = document.querySelector('.subBtn');
let name = document.querySelector('#name');
let form = document.querySelector('.form');
let data_element = document.querySelector('.form__data');

subBtn?.addEventListener(
    "click",
    (event) => {
        event.preventDefault();
        data = []
        questions_box.forEach(
            (question) => {
                let question_data = { 'question' :question.dataset.id, 'choice' : question.querySelector(".choice__input > input[type='radio']:checked")?.value}
                data.push(question_data);
            }
        )
        let form__data = {
            "questions":data,
            "name":name.value,
            'id':form.dataset.quiz
        }

        data_element.value = JSON.stringify(form__data);
        form.submit();
    }

)