const begin_btn = document.getElementsByClassName('begin_btn');
const rules_box = document.getElementsByClassName('rules_box');
const exit_btn = document.getElementsByClassName('quit');
const continue_btn = document.getElementsByClassName('restart');
const container_box = document.getElementsByClassName('container_box');
const option_list = document.querySelector('.option_list');
const timeCount = document.querySelector('.timer .sec');
const timeoff = document.querySelector('.timer .text');
const restart_quiz = document.querySelector('.play_again');
const quit_quiz = document.querySelector('.stop_game');

// If begin button is clicked
begin_btn[0].addEventListener('click', () => {
  begin_btn[0].style.display = 'none'; // Hide begin button
  rules_box[0].classList.add('activeInfo'); // Show rules box
});

// If exit button is clicked
exit_btn[0].addEventListener('click', () => {
  begin_btn[0].style.display = 'block'; // Show begin button
  rules_box[0].classList.remove('activeInfo'); // Hide rules box
});

// If continue button is clicked
continue_btn[0].addEventListener('click', () => {
  rules_box[0].classList.remove('activeInfo'); // Hide rules box
  container_box[0].classList.add('activeContainer'); // Show quiz box
  showQuestion(0); // Show question
  que_counter(1); // Show question counter
  startTimer(10); // Start timer

});

// Questions section by creating an array and passing the number, questions, option and answers
const Questions = [
  {
    numb: 1,
    question: "What is the name of the Curse occupying Yuji Itadori's body in 'Jujutsu Kaisen'?",
    options: ['Jogo', 'Gojo Satoru', 'Mahito', 'Ryomen Sukuna'],
    correctAnswer: 'Ryomen Sukuna',
    incorrectAnswers: ['Jogo', 'Gojo Satoru', 'Mahito']
  },
  {
    numb: 2,
    question: "What is All Might's Quirk called in 'My Hero Academia'?",
    options: ['One For All', 'Sugar Rush', 'Tail', 'Pop Off'],
    correctAnswer: 'One For All',
    incorrectAnswers: ['Sugar Rush', 'Tail', 'Pop Off']
  },
  {
    numb: 3,
    question: "What powers and abilities does Envy possess in 'Fullmetal Alchemist'?",
    options: ['Immortality', 'Shapeshifting', 'Regeneration', 'All of Them'],
    correctAnswer: 'All of Them',
    incorrectAnswers: ['Immortality', 'Shapeshifting', 'Regeneration']
  },
  {
    numb: 4,
    question: "Which person in Naruto is a 'kunoichi'?",
    options: ['Sakura', 'Kiba', 'Naruto', 'Shino'],
    correctAnswer: 'Sakura',
    incorrectAnswers: ['Kiba', 'Naruto', 'Shino']
  },
  {
    numb: 5,
    question: "How many executions did Gabimaru undergo in the first episode of 'Hell Paradise'?",
    options: ['5', '8', '2', '3'],
    correctAnswer: '5',
    incorrectAnswers: ['8', '2', '3']
  },
  {
    numb: 6,
    question: "What is the one beverage that ghouls can consume without getting sick in 'Tokyo Ghoul'?",
    options: ['Orange Juice', 'Grape Soda', 'Coffee', 'Alcohol'],
    correctAnswer: 'Coffee',
    incorrectAnswers: ['Orange Juice', 'Grape Soda', 'Alcohol']
  },
  {
    numb: 7,
    question: "Which village are Asta and Yuno from in 'Black Clover'?",
    options: ['Alubarna', 'Castle Town', 'Hage', 'Ecbatana'],
    correctAnswer: 'Hage',
    incorrectAnswers: ['Alubarna', 'Castle Town', 'Ecbatana']
  },
  {
    numb: 8,
    question: "Which anime series revolves around a boy who sells his soul to a demon?",
    options: ['Blue Exorcist', '3x3 Eyes', 'Black Butler', 'Noragami'],
    correctAnswer: 'Black Butler',
    incorrectAnswers: ['Blue Exorcist', '3x3 Eyes', 'Noragami']
  },
  {
    numb: 9,
    question: "What is the name Gabimaru’s enemies call him in 'Hell Paradise'?",
    options: ['Hollow', 'Demon', 'Zero', 'Killer'],
    correctAnswer: 'Hollow',
    incorrectAnswers: ['Demon', 'Zero', 'Killer']
  },
  {
    numb: 10,
    question: "Which one is a wall on Paradise Island that protected the remnants of Eldia in 'Attack on Titan'?",
    options: ['Maria', 'Rose', 'Sina', 'All of Them'],
    correctAnswer: 'All of Them',
    incorrectAnswers: ['Maria', 'Rose', 'Sina']
  }
];


let que_count = 0;
let que_numb = 1;
let counter;
let timeValue = 10;
let userScore = 0;
const next_que = document.querySelector('.next_que');
const result_box = document.querySelector('.result_box');

restart_quiz.addEventListener('click', function() {
  result_box.classList.remove('activeResult');
  container_box[0].classList.add('activeContainer');
  que_count = 0;
  que_numb = 1;
  userScore = 0;
  timeValue = 10;
  showQuestion(que_count);
  que_counter(que_numb);
  clearInterval(counter);
  startTimer(timeValue);
  next_que.style.display = 'none';
  timeoff.textContent = 'Time Left';
});

quit_quiz.addEventListener('click', function() {
  window.location.reload();
});


// If next question button is clicked
next_que.addEventListener('click', () => {
  if (que_count < Questions.length - 1) {
    que_count++;
    que_numb++;
    showQuestion(que_count);
    que_counter(que_numb);
    clearInterval(counter);
    startTimer(timeValue);
    next_que.style.display = 'none';
    timeoff.textContent = 'Time Left';
  } else {
    clearInterval(counter);
    showResults();
  }
});

// getting questions and options from array
function showQuestion(index) {
  const que_title = document.querySelector('.question_title');


  // question title tag
  let que_tag = '<span>' + Questions[index].numb + '.' + Questions[index].question + '</span>';

  // options tags
  let option_tag = '';
  for (let i = 0; i < Questions[index].options.length; i++) {
    option_tag += '<div class="option">' + Questions[index].options[i] + '<span></span></div>';
  }

  // question title and options
  que_title.innerHTML = que_tag;
  option_list.innerHTML = option_tag;

  // Selecting all options after they have been added to option_list
  const options = option_list.querySelectorAll('.option');
  options.forEach((options, i) => {
    options.setAttribute('onclick', 'optionSelected(this)');
  });
}

// If an option is selected by the user check if it is correct or wrong
function optionSelected(answer) {
  clearInterval(counter);
  let userAns = answer.textContent.trim();
  let correctAns = Questions[que_count].correctAnswer;
  let allOptions = option_list.children.length;

  if (userAns === correctAns) {
    userScore++;
    answer.classList.add('correct');
    answer.insertAdjacentHTML('beforeend', '<i class="fas fa-check"></i>');
  } else {
    answer.classList.add('incorrect');
    answer.insertAdjacentHTML('beforeend', '<i class="fas fa-times"></i>');
  }

  // Show the correct answer if the user's answer is wrong
  for (let i = 0; i < allOptions; i++) {
    if (option_list.children[i].textContent.trim() === correctAns && userAns !== correctAns) {
      option_list.children[i].classList.add('correct');
      option_list.children[i].insertAdjacentHTML('beforeend', '<i class="fas fa-check"></i>');
    }
  }

  // Disable all options after selecting one
  for (let i = 0; i < allOptions; i++) {
    option_list.children[i].classList.add('disabled');
  }
  next_que.style.display = 'block';
}

function showResults() {
  container_box[0].classList.remove('activeContainer');
  rules_box[0].classList.remove('activeInfo');
  result_box.classList.add('activeResult');

  const scoreText = result_box.querySelector('.score_text');
  let message;
  if (userScore > 7) {
    message = 'Congrats! \u{1F604}'; 
} else if (userScore > 5) {
    message = 'Nice! \u{1F642}'; 
} else {
    message = 'Sorry! \u{1F641}'; 
}

  scoreText.innerHTML = `<span>${message} You scored <p>${userScore}</p> out of <p>${Questions.length}</p></span>`;
}

function que_counter(index) {
  const scoreareaElement = document.querySelector('.score_area');
  scoreareaElement.innerHTML = '<span><p>' + index + '</p> of <p>' + Questions.length + '</p> Questions</span>';
}

// Timer function
function startTimer(time) {
  let timeValue = time;
  timeCount.textContent = timeValue;
  counter = setInterval(timer, 1000);
  function timer() {
    timeValue--;
    timeCount.textContent = timeValue;

    if (timeValue <= 0) {
      clearInterval(counter);
      timeoff.textContent = 'Time Off';
  

      let correctAns = Questions[que_count].correctAnswer;
      let allOptions = option_list.children.length;

      for (let i = 0; i < allOptions; i++) {
        option_list.children[i].classList.remove('correct');
        option_list.children[i].classList.add('disabled');
      }

      for (let i = 0; i < allOptions; i++) {
        if (option_list.children[i].textContent.trim() === correctAns) {
          option_list.children[i].classList.add('correct');
          option_list.children[i].insertAdjacentHTML('beforeend', '<i class="fas fa-check"></i>');
        }
      }
      next_que.style.display = 'block';
    }
  }
}