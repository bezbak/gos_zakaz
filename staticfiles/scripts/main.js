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