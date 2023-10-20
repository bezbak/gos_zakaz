const accordionItems = document.querySelectorAll('.accordion-itembek');

accordionItems.forEach(item => {
  const header = item.querySelector('.accordion-headerbek');
  const content = item.querySelector('.accordion-contentbek');

  header.addEventListener('click', () => {
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
  });
});

document.addEventListener('DOMContentLoaded',()=>{
  document.getElementById('oso').addEventListener('click',()=>{
    document.querySelector('.apparat2').classList.toggle('apparat2__active')
  })
  document.getElementById('burger').addEventListener('click',()=>{
    document.querySelector('.one').classList.toggle('top_span')
    document.querySelector('.two').classList.toggle('m_span')
    document.querySelector('.three').classList.toggle('b_span')
    document.querySelector('.burgerMenu').classList.toggle('burgerMenu__active')
  })
  document.getElementById('app').addEventListener('click',()=>{
    document.querySelector('.apparat').classList.toggle('apparat__acitve')
})
    document.getElementById('pagelinkBtn').addEventListener('click',()=>{
        document.querySelector('.fixedNav').classList.toggle('fixedNav__avtive')
    })
    document.querySelector('.banner').addEventListener('click',()=>{
        document.querySelector('.fixedNav').classList.remove('fixedNav__avtive')
    })
    // document.querySelector('.container').addEventListener('click',()=>{
    //     document.querySelector('.fixedNav').classList.remove('fixedNav__avtive')
    // })
 
})
let docTitle = document.title;
window.addEventListener('blur',()=>{
    docTitle.title = 'Hа родину!';
});
window.addEventListener('focus',()=>{
    document.title = docTitle;
})



const slider = document.querySelector('.slider'); 
 
let isDown = false; 
let startX; 
let scrollLeft; 

slider.addEventListener('mousedown', (e) => { 
  isDown = true; 
  startX = e.pageX - slider.offsetLeft; 
  scrollLeft = slider.scrollLeft; 
}); 

slider.addEventListener('mouseleave', () => { 
  isDown = false; 
}); 

slider.addEventListener('mouseup', () => { 
  isDown = false; 
}); 

slider.addEventListener('mousemove', (e) => { 
  if (!isDown) return; 
  e.preventDefault(); 
  const x = e.pageX - slider.offsetLeft; 
  const walk = (x - startX) * 2; // adjust scrolling speed here 
  slider.scrollLeft = scrollLeft - walk; 
}); 

function txt_pilus() {
  let elements = document.querySelectorAll('*'); 

  for (let i = 0; i < elements.length; i++) {
      let currentFontSize = window.getComputedStyle(elements[i], null).getPropertyValue('font-size');
      let newSize = (parseFloat(currentFontSize) + 2) + 'px'; 

      elements[i].style.fontSize = newSize;
  }
}

function txt_minus() {
  let elements = document.querySelectorAll('*'); 

  for (let i = 0; i < elements.length; i++) {
      let currentFontSize = window.getComputedStyle(elements[i], null).getPropertyValue('font-size');
      let newSize = (parseFloat(currentFontSize) - 2) + 'px'; 

      elements[i].style.fontSize = newSize;
  }
}

function img_minus() {
  let img = document.querySelectorAll('img')
  img.forEach(e=>{
      e.classList.add('img_none')
      e.classList.remove('img_gray')
  })
}

function img_gray() {
  let img = document.querySelectorAll('img')
  img.forEach(e=>{
      e.classList.remove('img_none')
      e.classList.add('img_gray')
  })
}

function img_default() {
  let img = document.querySelectorAll('img')
  img.forEach(e=>{
      e.classList.remove('img_none')
      e.classList.remove('img_gray')
  })
}
document.addEventListener("DOMContentLoaded", function() {
  // Функция для получения текущей даты и времени на русском языке
  function getCurrentDateTime() {
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      weekday: "long",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    };
    const locale = "ru-RU";
    const dateTimeString = new Date().toLocaleDateString(locale, options);
    return dateTimeString;
  }

  // Обновляем элемент с датой и временем каждую секунду
  function updateDateTime() {
    const datetimeElement = document.getElementById("datetime");
    const currentDateTime = getCurrentDateTime();
    datetimeElement.textContent = currentDateTime;
  }

  // Обновляем дату и время сразу после загрузки страницы
  updateDateTime();

  // Обновляем дату и время каждую секунду
  setInterval(updateDateTime, 1000);
});
function txt_pilus() {
  let elements = document.querySelectorAll('*');

  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {
          let currentFontSize = window.getComputedStyle(elements[i], null).getPropertyValue('font-size');
          let newSize = (parseFloat(currentFontSize) + 2) + 'px';

          elements[i].style.fontSize = newSize;
      }
  }
}

function txt_minus() {
  let elements = document.querySelectorAll('*');

  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {

          let currentFontSize = window.getComputedStyle(elements[i], null).getPropertyValue('font-size');
          let newSize = (parseFloat(currentFontSize) - 2) + 'px';

          elements[i].style.fontSize = newSize;
      }
  }
}

function txt_letter(e) {
  let elements = document.querySelectorAll('*');
  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {

          let newSize;
          if (e == 1) {
              newSize = 'normal';
          }
          if (e == 2) {
              newSize = 2 + 'px';
          }
          if (e == 3) {
              newSize = 4 + 'px';
          }
          elements[i].style.letterSpacing = newSize;
      }
  }
}

function txt_line(e) {
  let elements = document.querySelectorAll('*');
  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {
          let newSize;
          if (e == 1) { newSize = 'normal'; }
          if (e == 2) { newSize = 2; }
          if (e == 3) { newSize = 2.5; }
          elements[i].style.lineHeight = newSize;
      }
  }
}

function txt_family(e) {
  let elements = document.querySelectorAll('*');
  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {

          let newSize;
          if (e == 1) {
              newSize = 'serif';
          }
          if (e == 2) {
              newSize = 'sans-serif';
          }

          elements[i].style.fontFamily = newSize;
      }
  }
}

function body_bg(e) {
  let elements = document.querySelectorAll('*');
  for (let i = 0; i < elements.length; i++) {
      if (elements[i] === document.querySelector('html') || elements[i] === document.querySelector('head') || elements[i] === document.querySelector('body') || elements[i].classList.contains('editorBtn')) {
      } else {

          let newBg;
          let newColor;
          if (e == 1) {
              newBg = '#FFF'
              newColor = '#000'
          }
          if (e == 2) {
              newBg = '#000'
              newColor = '#FFF'
          }
          if (e == 3) {
              newBg = '#9dd1ff'
              newColor = '#063462'
          }
          if (e == 4) {
              newBg = '#f7f3d6'
              newColor = '#4d4b43'
          }
          if (e == 5) {
              newBg = '#3b2716'
              newColor = '#a9e44d'
          }

          document.body.style.background = newBg;
          elements[i].style.color = newColor;
      }
  }
}

function img_minus() {

  let img = document.querySelectorAll('img')
  img.forEach(e => {
      if (e === document.querySelector('html') || e === document.querySelector('head') || e === document.querySelector('body') || e.classList.contains('editorBtn')) {
      } else {
          e.classList.add('img_none')
          e.classList.remove('img_gray')
      }
  })
}

function img_gray() {

  let img = document.querySelectorAll('img')
  img.forEach(e => {
      if (e === document.querySelector('html') || e === document.querySelector('head') || e === document.querySelector('body') || e.classList.contains('editorBtn')) {
      } else {
          e.classList.remove('img_none')
          e.classList.add('img_gray')
      }
  })
}

function img_default() {

  let img = document.querySelectorAll('img')
  img.forEach(e => {
      if (e === document.querySelector('html') || e === document.querySelector('head') || e === document.querySelector('body') || e.classList.contains('editorBtn')) {
      } else {
          e.classList.remove('img_none')
          e.classList.remove('img_gray')
      }
  })
}

window.addEventListener('click',e=>{
  if(e.target.hasAttribute('settings_open')){
      document.querySelector('.editorSettingsBG').classList.toggle('active')
  }
  if(e.target.hasAttribute('settings_default')){
      let alll = document.querySelectorAll('*')
      alll.forEach(e=>{
          e.style=null
          e.classList.remove('img_none')
          e.classList.remove('img_gray')
      })
      document.querySelector('.editPanel').classList.remove('active')
      document.querySelector('.header').classList.remove('active')

  }
  if(e.target.hasAttribute('settings_deactive')){
      document.querySelector('.editPanel').classList.remove('active')
      document.querySelector('.header').classList.remove('active')
  }
  if(e.target.hasAttribute('settings_active')){
    document.querySelector('.editPanel').classList.add('active')
    document.querySelector('.header').classList.add('active')
  }

})

